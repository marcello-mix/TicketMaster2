from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    from flask import Flask
    
    app = Flask(__name__)
    
    # Configurar caminho absoluto para o banco de dados
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(os.path.dirname(basedir), 'instance', 'chamados.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'gestor_chamados_secret_key'
    
    db.init_app(app)
    
    return app
