from fastapi import FastAPI

APP_NAME: str = "demo_sonarqube"

app = FastAPI(title=APP_NAME)


def sumar(a: int, b: int) -> int:
    
    return a + b


@app.get("/saludo")
def saludo() -> dict:
    
    return {"msg": "Hola, SonarQube!"}
