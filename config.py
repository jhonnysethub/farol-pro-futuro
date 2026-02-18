import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Isso faz o Python ler o arquivo .env e carregar as variáveis
load_dotenv()

class Config:
    # Agora ele puxa a senha do arquivo .env escondido
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # O banco de dados pode continuar assim por enquanto, 
    # ou você pode preparar para o futuro puxando do .env também:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'database.db'))
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False