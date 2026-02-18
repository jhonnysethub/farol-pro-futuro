import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime, timezone
import random
from config import Config

PALAVRAS_PARTE_1 = [
    'FAROL', 'MAR', 'JORNADA', 'CAMINHO', 'PONTE', 'ESTRELA', 'SOL', 'RIO',
    'TRILHA', 'VENTO', 'PORTO', 'HORIZONTE', 'NORTE', 'NAVEGAÇÃO',
    'DESTINO', 'ROTA', 'ESFERA', 'BRUMA', 'VELA', 'FONTE', 'ASTRO', 'MAPA'
    ]

PALAVRAS_PARTE_2 = [
    'LUZ', 'CALMO', 'FORTE', 'NOVO', 'GUIA', 'BRILHO', 'FUTURO', 'SEGURO',
    'CLARO', 'LONGE', 'SABER', 'CALOR', 'ALVO', 'SUAVE', 'VIVO', 'ALTO',
    'AMPLITUDE', 'SABEDORIA', 'ESPERANÇA', 'FOCO', 'PAZ', 'MUDANÇA'
    ]

def gerar_chave_amigavel():
    palavra1 = random.choice(PALAVRAS_PARTE_1)
    palavra2 = random.choice(PALAVRAS_PARTE_2)
    numero = random.randint(100, 999)
    return f'{palavra1}-{numero}-{palavra2}'

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Desabafo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False,)
    data_criacao = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    chave_secreta = db.Column(db.String(30), unique=True, nullable=False, default=gerar_chave_amigavel)

class Universidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    sigla = db.Column(db.String(10), unique=True, nullable=False)
    cursos = db.relationship('Curso', back_populates='universidade', lazy=True)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.String(100), nullable=False)
    campus = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    nota_corte = db.Column(db.Float, nullable=False)
    area = db.Column(db.String(50), nullable=False)
    universidade_id = db.Column(db.Integer, db.ForeignKey('universidade.id'), nullable=False)
    universidade = db.relationship('Universidade', back_populates='cursos')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar-desabafo', methods=['POST'])
def enviar_desabafo():
    texto_desabafo = request.form.get('desabafo')
    if texto_desabafo:
        novo_desabafo = Desabafo(texto=texto_desabafo)
        db.session.add(novo_desabafo)
        db.session.commit()
        session['nova_chave'] = novo_desabafo.chave_secreta
    
    return redirect(url_for('gps'))

@app.route('/relembrar', methods=['GET', 'POST'])
def relembrar():
    desabafo_encontrado = None
    chave_buscada = None
    if request.method == 'POST':
        chave_buscada = request.form.get('chave')
        if chave_buscada:
            desabafo_encontrado = Desabafo.query.filter_by(chave_secreta=chave_buscada).first()
    return render_template('relembrar.html', desabafo=desabafo_encontrado, chave_buscada=chave_buscada)

@app.route('/gps', methods=['GET', 'POST'])
def gps():
    resultados = None
    if request.method == 'POST':
        print("\n--- DEBUG: Formulário Enviado ---")
        try:
            nota_usuario = float(request.form.get('nota'))
            area_usuario = request.form.get('area')

            print(f"Dados recebidos do formulário -> Nota: {nota_usuario}, Área: '{area_usuario}'")

            # Vamos ver todos os cursos no banco para comparar
            todos_os_cursos = Curso.query.all()
            print(f"Total de cursos no banco: {len(todos_os_cursos)}")

            # A busca real
            resultados = Curso.query.filter(
                Curso.area == area_usuario
            ).order_by(Curso.nota_corte.desc()).all()
            
            print(f"Cursos encontrados pela busca: {len(resultados)}")
            if resultados:
                print("Cursos encontrados:")
                for curso in resultados:
                    print(f"- {curso.nome_curso} (Nota: {curso.nota_corte}, Área: {curso.area})")

        except (ValueError, TypeError):
            print(f"!!!!!!!!!! OCORREU UM ERRO !!!!!!!!!!!")
            area_usuario = request.form.get('area')
            
            # ✅ CORREÇÃO: "filter" escrito corretamente e ".all()" no lugar certo
            resultados = Curso.query.filter(
                Curso.area == area_usuario
            ).order_by(Curso.nota_corte.desc()).all()
            
    return render_template('gps.html', resultados=resultados)

@app.route('/admin')
def admin_list():
    cursos = db.session.query(Curso).join(Universidade).order_by(Universidade.sigla, Curso.nome_curso).all()
    return render_template('admin_list.html', cursos=cursos)

@app.route('/admin/add', methods=['GET', 'POST'])
def admin_add():
    if request.method == 'POST':
        universidade_id = request.form.get('universidade_id')
        universidade = Universidade.query.get(universidade_id)
        novo_curso = Curso(
            nome_curso=request.form['nome_curso'],
            campus=request.form['campus'],
            cidade=request.form['cidade'],
            nota_corte=float(request.form['nota_corte']),
            area=request.form['area'],
            universidade=universidade
        )
        db.session.add(novo_curso)
        db.session.commit()

        return redirect(url_for('admin_list'))
    universidades = Universidade.query.all()
    return render_template('admin_form.html', action='Adicionar', curso=None, universidades=universidades)

@app.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
def admin_edit(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
        universidade_id = request.form['universidade_id']
        curso.nome_curso = request.form['nome_curso']
        curso.universidade_id = universidade_id
        curso.campus = request.form['campus']
        curso.cidade= request.form['cidade']
        curso.nota_corte = float(request.form['nota_corte'])
        curso.area = request.form['area'] 
        db.session.commit()
        return redirect(url_for('admin_list'))
    universidades = Universidade.query.all()
    return render_template('admin_form.html', action='Editar', curso=curso, universidades=universidades)

@app.route('/admin/delete/<int:id>', methods=['GET', 'POST'])
def admin_delete(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('admin_list'))

if __name__ == '__main__':   
    with app.app_context():
        db.create_all()
    app.run(debug=True)