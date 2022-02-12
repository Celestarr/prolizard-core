# confetti

MyFoLab's primary backend service.

### Technical stack

- **Programming language:** Python `3.9.7`
- **Framework:** Django `3.2.7`
- **Primary database:** PostgreSQL `13.4`

### Development instructions

#### Pre-requisites:
1. [Docker Engine](https://docs.docker.com/engine/install/) `19.03.0+`
2. [Docker Compose](https://docs.docker.com/compose/install/) `1.28.3+`
3. Editor or IDE of choice (Recommendation: [Visual Studio Code](https://code.visualstudio.com/download) or [PyCharm](https://www.jetbrains.com/pycharm/download/))

--

Run the following commands to get your development services up and running:

```bash
# Create a .env from provided sample
cp .env.sample .env

# Start containers with docker compose
docker-compose up
```

Navigate to [localhost:8000/admin](http://localhost:8000/admin/) if everything ran successfully. Login with superuser credentials (email: `su@myfolab.com`, password: `suadmin`) and you should be able to get into the admin panel.

--

**Important**: Make sure to do the following everytime before pushing your changes to this repository:

Check source code issues and try to resolve them:

```bash
docker exec -it myfo__confetti make check
```

Finally format code:

```bash
docker exec -it myfo__confetti make fmt
```

Commit and push if everything is alright.

--

To install a new pip package:

```bash
docker exec -it myfo__confetti pip install <new-package>
```

Sync _requirements.txt_ after installing new packages:

```bash
docker exec -it myfo__confetti pip freeze > requirements.txt
```

--

Generate/Update Translation Files:
```bash
docker exec -it myfo__confetti python app/manage.py makemessages --ignore "venv/**/*.py" --ignore "dev/**/*.py" --ignore "requirements.txt" --locale <locale_code>
```

--

Generate Migrations:
```bash
docker exec -it myfo__confetti python app/manage.py makemigrations
```

--

Generate OpenAPI schema file:
```bash
docker exec -it myfo__confetti python app/manage.py spectacular --file schema.yml
```

Visualize the schema using redoc:
```bash
docker run -it -p 0.0.0.0:8081:80 -v $(pwd)/:/usr/share/nginx/html/swagger/ -e SPEC_URL=swagger/schema.yml redocly/redoc
```

--
