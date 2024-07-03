# seoul

[![ci](https://github.com/MyfoLab/seoul/workflows/ci/badge.svg?branch=master)](https://github.com/MyfoLab/seoul/actions/workflows/ci.yml)

MyFoLab's primary backend service.

## Getting Started

### Using Docker

#### Pre-requisites:
1. [Docker Engine](https://docs.docker.com/engine/install/) `19.03.0+`
2. [Docker Compose](https://docs.docker.com/compose/install/) `1.28.3+`

Run the following commands to get your development services up and running:

```bash
# Create a .env from provided sample
cp .env.sample .env

# Start containers with docker compose
docker-compose up
```

Navigate to [localhost:8000/admin](http://localhost:8000/admin/) if everything ran successfully. Login with superuser credentials (email: `admin@myfolab.com`, password: `myfo1234`) and you should be able to get into the admin panel.

## Commands

```bash
# Check source code issues and try to resolve them:
docker exec -it myfo-seoul make check

# Format code:
docker exec -it myfo-seoul make fmt

# To install a new pip package:
docker exec -it myfo-seoul pip install <new-package>

# Generate/Update Translation Files:
docker exec -it myfo-seoul python manage.py makemessages --ignore "venv/**/*.py" --ignore "dev/**/*.py" --ignore "requirements.txt" --locale <locale_code>

# Generate Migrations:
docker exec -it docker-app-1 python manage.py makemigrations
docker exec -it docker-app-1 python manage.py migrate

# Generate OpenAPI schema file:
docker exec -it myfo-seoul python manage.py spectacular --file schema.yml

# Visualize the schema using redoc:
docker run -it -p 0.0.0.0:8081:80 -v $(pwd)/:/usr/share/nginx/html/swagger/ -e SPEC_URL=swagger/schema.yml redocly/redoc
```
