from fastapi import FastAPI

APP_NAME: str = 'demo_sonarqube'

app = FastAPI(title=APP_NAME)


def sumar(a: int, b: int) -> int:
    """Suma dos números enteros.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: Resultado de la suma.
    """
    return a + b


@app.get('/saludo')
def saludo() -> dict:
    """Endpoint de ejemplo con saludo.

    Returns:
        dict: Mensaje de saludo.
    """
    return {'msg': 'Hola, SonarQube!'}
