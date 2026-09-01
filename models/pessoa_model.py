from sqlalchemy import Column, Integer, String, DECIMAL, Date

from database import Base

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(60))
    cpf = Column(Integer)
    data_nascimento = Column(Date)
    peso = Column(Integer)
<<<<<<< HEAD
    altura = Column(DECIMAL(10,2))
=======
    altura = Column(DECIMAL(10,2))
    sexo = Column(String(1))
    cep = Column(Integer)
    rua_logradouro = Column(String(100))
    bairro = Column(String(20))
    cidade = Column(String(70))
    uf = Column(String(2))
    
    
    

>>>>>>> b665605abf3c2ab94ac33438a9a6624152c0a130
