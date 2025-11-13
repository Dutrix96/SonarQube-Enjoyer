# Demo SonarQube + Clean Code (Python)

## Requisitos
- Docker y Docker Compose
- Python 3.11 (opcional para desarrollo local)

## Ejecutar la app con Docker
```bash
docker compose up -d app
# Abrir http://localhost:8000/docs
```

## Analizar con SonarQube (local)
1. Levanta SonarQube:
   ```bash
   docker compose up -d sonarqube
   # http://localhost:9000  (admin/admin) → crea un TOKEN
   ```
2. Ejecuta el escáner:
   ```bash
   docker run --rm          -e SONAR_HOST_URL="http://host.docker.internal:9000"          -e SONAR_TOKEN="TU_TOKEN"          -v "${PWD}:/usr/src"          sonarsource/sonar-scanner-cli          "-Dsonar.projectKey=demo-local"          "-Dsonar.sources=."
   ```

## Buenas prácticas seguidas
- Nombres `snake_case`, clases `PascalCase`, constantes `MAYÚSCULAS`.
- Docstrings con autoDocstring (estilo Google).
- Límite de 80 columnas (Black + EditorConfig).
- Linter con Ruff e import sorting (isort).
- Hooks `pre-commit` (formato, lint, tests, archivos grandes).
- CI en GitHub Actions (black/ruff/isort/pytest+coverage).
