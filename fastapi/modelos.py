from pydantic import BaseModel


class UsuarioBase(BaseModel):
    username : str
    email: str
    senha: str

class Usuario(UsuarioBase):
    id : int | None = None

#autenticacao
class Singup(UsuarioBase):
    pass 



class Singin:
    email : str
    senha : str

#tasks

class TaskBase(BaseModel):
    titulo : str
    descricao : str
    concluido: bool=False
    usuario_id : int

class Task(TaskBase):
    id : int

class TaskCreate(TaskBase):
    pass
