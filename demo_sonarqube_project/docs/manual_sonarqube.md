# Manual de SonarQube (Práctica)

## ¿Para qué sirve?
SonarQube analiza la **calidad del código** y reporta:
- **Bugs** y **vulnerabilidades**.
- **Code smells** (mantenibilidad).
- **Duplicación**.
- **Complejidad**.
- **Cobertura de tests** (si subimos `coverage.xml`).

## Flujo de uso en el equipo
1. Levantar servidor SonarQube local en Docker.
2. Crear el **token** personal (usuario `admin` al iniciar).
3. Configurar `sonar-project.properties`.
4. Ejecutar el **escáner** con Docker apuntando al servidor.
5. Revisar el tablero en `http://localhost:9000`.

## Instalación (Docker)
```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:latest
```
Login inicial: `admin / admin`.

## Análisis del código
```bash
docker run --rm       -e SONAR_HOST_URL="http://host.docker.internal:9000"       -e SONAR_TOKEN="TOKEN"       -v "${PWD}:/usr/src"       sonarsource/sonar-scanner-cli       "-Dsonar.projectKey=demo-local"       "-Dsonar.sources=."
```

## Métricas clave (ejemplos sobre el proyecto)
- **Bugs**: p. ej., acceso a índice fuera de rango.
- **Vulnerabilidades**: p. ej., uso de eval/exec con entrada externa.
- **Code Smells**: funciones demasiado largas, nombres poco claros.
- **Duplicación**: bloques repetidos en `src/`.
- **Complejidad**: métodos con demasiados caminos (ciclomática alta).
- **Cobertura**: generado por `pytest --cov=src --cov-report=xml`.

## Buenas prácticas derivadas del informe
- Reducir funciones > 30 líneas o con múltiples responsabilidades.
- Extraer funciones reutilizables para eliminar duplicaciones.
- Añadir tests donde la cobertura sea < 80%.
- Añadir tipos (hints) para mejorar mantenibilidad.
- Limitar la complejidad (refactorizar condicionales profundos).

## Integración con CI
- En GitHub Actions se valida **formato** y **tests** en cada push.
- El análisis de Sonar se ejecuta **localmente** contra el servidor
  (los runners de GitHub no pueden acceder a tu `localhost`).
- Alternativas: desplegar SonarQube accesible públicamente o usar
  SonarCloud.

## Decisiones del equipo
- Estándares: Black (80 col), Ruff, isort, docstrings Google.
- Commit convention: `feat|fix|chore|docs|refactor|test|ci|perf|build`.
- Pre-commit obligatorio (formato, lint, tests, límite 5MB/archivo).
