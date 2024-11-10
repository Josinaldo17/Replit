from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

usuario = 'postgres'
senha = 'C2Fjz9tGnr3yTTHv'
porta = '5432'
host = 'sensually-happening-nyala.data-1.use1.tembo.io'
banco_de_dados = 'postgres'


class Config:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{usuario}:{senha}@{host}:{porta}/{banco_de_dados}' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Sempreemforma'