import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer

# Configurando a engine do BD
engine = create_engine("sqlite:///database.db")

# Configurando a sessão
Session = sessionmaker(engine)

# Criando a tabela
Base = declarative_base()

# Mapeando da classe usuario para o banco de dados
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

# Inserindo dados na tabela
def insert_usuario(name_usuario, type_usuario):
    session = Session()

    # Tratamento de erros
    try:
        if all([name_usuario, type_usuario]):
            usuario = Usuario(name=name_usuario, type=type_usuario)
            session.add(usuario)
            session.commit()
            print(f'Usuário {name_usuario} cadastrado com sucesso!')
        else:
            print('Os espaço "name" e "type" não podem ficar em branco.')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao tentar cadastrar o usuário {name_usuario}: {e}')
    finally:
        session.close()


if __name__ == '__main__':
    os.system('cls') # limpa o terminal
    Base.metadata.create_all(engine)
    insert_usuario('Eryck', "Programador")