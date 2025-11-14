from fastapi import FastAPI

APP_NAME: str = "demo_sonarqube"

app = FastAPI(title=APP_NAME)


def sumar(a: int, b: int) -> int:
    """Suma dos variables que entren por parametros

    Args:
        a (int): primer numero
        b (int): segundo numero

    Returns:
        int: Devuelve la suma de ambos
    """
    return a + b


@app.get("/saludo")
def saludo() -> dict:
    """Crea un saludo en JSON con el mensaje que queramos

    Returns:
        dict: devuelve un objeto JSON con el mensaje en particular
    """
    return {"msg": "Hola, SonarQube!"}
