from sqlalchemy.orm import Session
from models.pessoa_model import Pessoa

class PessoaRepository:
    #listar todas as pessoas
    def listar(self, db: Session):
        return db.query(Pessoa).all()
    
    #cadastra Pessoa
    def cadastar(self, db: Session, pessoa):
        nova_pessoa = Pessoa(
            nome = pessoa.nome,
            sexo = pessoa.sexo,
            datanascimento = pessoa.datanascimento,
            peso = pessoa.peso,
            altura = pessoa.altura
        )

        db.add(nova_pessoa)
        db.commit()
        db.refresh(nova_pessoa)

        return nova_pessoa
    
    #listar pessoa por id
    def pessoa_id(self, db: Session, id: int):
        return db.query(Pessoa).filter(Pessoa.idpessoa == id).first()
    
    #alterar pessoa
    def alterar (self, db: Session, id: int, pessoa):
        pessoa_bd = self.pessoa_id(db, id)

        pessoa_bd.nome = pessoa.nome
        pessoa_bd.sexo = pessoa.sexo
        pessoa_bd.datanascimento = pessoa.datanascimento
        pessoa_bd.peso = pessoa.peso
        pessoa_bd.altura = pessoa.altura

        db.commit()
        db.refresh(pessoa_bd)
        
        return pessoa_bd
    
    #excluir pessoa
    def excluir (self, db: Session, id: int):
       pessoa_bd = self.pessoa_id(db, id)
       
       db.delete(pessoa_bd)
       db.commit()

       return{"Mensagem": "Pessoa Excluída com Sucesso!!"}