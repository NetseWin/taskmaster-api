from app.schemas import Usuario

u2 = Usuario(nombre="Hugo", email="hugo@gmail.com")
print(u2.model_dump(exclude_none=True))