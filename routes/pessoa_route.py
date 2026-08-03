from fastapi import APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal

from controllers.pessoa_controller import PessoaController
from schemas.pessoa_schema import PessoaSchema

router = APIRouter(
    prefix="/pessoa",
    tags=["Pessoa"]
)
controller = PessoaController()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar():
    db = next(get_db())

    return controller.listar(db)

@router.post("/")
def cadstrar(pessoa: PessoaSchema):
    db = next(get_db())
    return controller.cadastrar(db, pessoa)


# =========================
# ALTERAR PESSOA
# =========================

@router.put("/{id}")
def alterar(id: int, pessoa: PessoaSchema):

    db = next(get_db())

    return controller.alterar(
        db,
        id,
        pessoa
    )



# =========================
# EXCLUIR PESSOA
# =========================

@router.delete("/{id}")
def excluir(id: int):

    db = next(get_db())

    return controller.excluir(
        db,
        id
    )