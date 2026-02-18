from app import app, db, Universidade, Curso

def seed_database():
    with app.app_context():
        # Limpa as tabelas na ordem correta (cursos primeiro por causa da dependência)
        Curso.query.delete()
        Universidade.query.delete()
        db.session.commit()

        # 1. Cria as Universidades
        upe = Universidade(nome='Universidade de Pernambuco', sigla='UPE')
        ufpe = Universidade(nome='Universidade Federal de Pernambuco', sigla='UFPE')
        ufrpe = Universidade(nome='Universidade Federal Rural de Pernambuco', sigla='UFRPE')
        ifpe = Universidade(nome='Instituto Federal de Pernambuco', sigla='IFPE')
        
        db.session.add_all([upe, ufpe, ufrpe, ifpe])
        db.session.commit()

        # 2. Cria os Cursos e os associa com as Universidades
        cursos_data = [
           {'nome_curso': 'Ciência da Computação', 'universidade': ufpe, 'campus': 'CIn', 'cidade': 'Recife', 'nota_corte': 785.5, 'area': 'Exatas'},
            {'nome_curso': 'Engenharia da Computação', 'universidade': ufpe, 'campus': 'CIn', 'cidade': 'Recife', 'nota_corte': 770.1, 'area': 'Exatas'},
            {'nome_curso': 'Análise e Desenv. de Sistemas', 'universidade': ufpe, 'campus': 'CIn', 'cidade': 'Recife', 'nota_corte': 730.0, 'area': 'Exatas'},
            {'nome_curso': 'Medicina', 'universidade': ufpe, 'campus': 'CCS', 'cidade': 'Recife', 'nota_corte': 815.0, 'area': 'Biomédicas'},
            {'nome_curso': 'Enfermagem', 'universidade': ufpe, 'campus': 'CCS', 'cidade': 'Recife', 'nota_corte': 715.2, 'area': 'Biomédicas'},
            {'nome_curso': 'Direito', 'universidade': ufpe, 'campus': 'CCJ', 'cidade': 'Recife', 'nota_corte': 760.8, 'area': 'Humanas'},
            {'nome_curso': 'Psicologia', 'universidade': ufpe, 'campus': 'CFCH', 'cidade': 'Recife', 'nota_corte': 740.2, 'area': 'Humanas'},
            {'nome_curso': 'Pedagogia', 'universidade': ufpe, 'campus': 'CAA', 'cidade': 'Caruaru', 'nota_corte': 610.5, 'area': 'Humanas'},
            {'nome_curso': 'Engenharia Civil', 'universidade': ufpe, 'campus': 'CAT', 'cidade': 'Caruaru', 'nota_corte': 710.0, 'area': 'Exatas'},
            
            # UPE
            {'nome_curso': 'Medicina', 'universidade': upe, 'campus': 'FCM', 'cidade': 'Recife', 'nota_corte': 802.1, 'area': 'Biomédicas'},
            {'nome_curso': 'Engenharia de Software', 'universidade': upe, 'campus': 'POLI', 'cidade': 'Recife', 'nota_corte': 735.0, 'area': 'Exatas'},
            {'nome_curso': 'Sistemas de Informação', 'universidade': upe, 'campus': 'Garanhuns', 'cidade': 'Garanhuns', 'nota_corte': 680.0, 'area': 'Exatas'},
            {'nome_curso': 'Fisioterapia', 'universidade': upe, 'campus': 'Petrolina', 'cidade': 'Petrolina', 'nota_corte': 695.0, 'area': 'Biomédicas'},

            # UFRPE
            {'nome_curso': 'Medicina Veterinária', 'universidade': ufrpe, 'campus': 'Sede', 'cidade': 'Recife', 'nota_corte': 715.4, 'area': 'Biomédicas'},
            {'nome_curso': 'Ciência da Computação', 'universidade': ufrpe, 'campus': 'UAST', 'cidade': 'Serra Talhada', 'nota_corte': 670.0, 'area': 'Exatas'},
            {'nome_curso': 'Gastronomia', 'universidade': ufrpe, 'campus': 'Sede', 'cidade': 'Recife', 'nota_corte': 655.8, 'area': 'Humanas'},

            # IFPE
            {'nome_curso': 'Design Gráfico', 'universidade': ifpe, 'campus': 'Recife', 'cidade': 'Recife', 'nota_corte': 640.0, 'area': 'Humanas'},
            {'nome_curso': 'Gestão de Turismo', 'universidade': ifpe, 'campus': 'Recife', 'cidade': 'Recife', 'nota_corte': 605.1, 'area': 'Humanas'},
            {'nome_curso': 'Análise e Desenv. de Sistemas', 'universidade': ifpe, 'campus': 'Jaboatão', 'cidade': 'Jaboatão', 'nota_corte': 650.0, 'area': 'Exatas'},
            {'nome_curso': 'Radiologia', 'universidade': ifpe, 'campus': 'Recife', 'cidade': 'Recife', 'nota_corte': 660.0, 'area': 'Biomédicas'},
        ]


        for data in cursos_data:
            curso = Curso(**data)
            db.session.add(curso)
            db.session.add(curso)
        
        db.session.commit()
        print("Banco de dados populado com Universidades e Cursos relacionados!")

if __name__ == '__main__':
    seed_database()
