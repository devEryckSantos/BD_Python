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
            print('Os espaços "name" e "type" não podem ficar em branco.')
    except Exception as e:
        session.rollback()
        print(f'Ocorreu um erro ao tentar cadastrar o usuário {name_usuario}: {e}')
    finally:
        session.close()

# Buscando usuários
def select_usuarios(name_usuario=''):
    session = Session()
    try:
        if name_usuario:
            data = session.query(Usuario).filter(Usuario.name == name_usuario) # consulta um usuário
        else: 
            data = session.query(Usuario).all() # retorna todos os usuários
        
        for i in data:
            print(f'Usuário: {i.name} - Tipo: {i.type}')
        
    except Exception as e:
        print('Ocorreu algum erro ao consutar o(s) usuário(s).')
    finally:
        session.close()

# Mudando o nome do usuário
def update_usuario(id_usuario, name_usuario):
    session = Session()

    try:
        if all([id_usuario, name_usuario]):
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            usuario.name = name_usuario
            session.commit()
            print('Nome do usuário alterado com sucesso!')
        else:
            print('Os blocos "id" e "name" não podem ficar em branco.')
    except Exception as e:
        session.rollback()
        print('Ocorreu um erro ao atualizar o usuário')
    finally:
        session.close()

def delete_usuario(id_usuario):
    try:
        session = Session()
        
        if id_usuario:
            usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
            session.delete(usuario)
            session.commit()
            print("Usuário deletado!")
        else:
            print('O campo "ID" não pode ficar em branco.')

    except Exception as e:
        session.rollback()
        print('Ocorreu um erro ao deletar o usuário.')
    finally:
        session.close()

if __name__ == '__main__':
    os.system('cls') # limpa o terminal
    Base.metadata.create_all(engine)
    # insert_usuario('Robson', "Gerente de vendas")
    # select_usuarios('Eryck')
    # update_usuario(2, 'Eduardo')
    delete_usuario(2)