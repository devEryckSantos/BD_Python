from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

# Configurando a engine do BD
engine = create_engine("sqlite:///database.db")

# Criando a tabela
Base = declarative_base()

# Mapeando da classe usuario para o banco de dados
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(engine)