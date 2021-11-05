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
# Build and create docker containers.
# Run only once (or after changing docker/entrypoint.sh or docker/confetti.dockerfile).
CURRENT_USER=$(id -u):$(id -g) docker-compose up --build --no-start

# Start containers.
docker-compose start

# Create database sequence.
# Needed for user's username, which is auto generated on user creation.
# Run once per docker build.
docker exec -it myfolab_core_confetti_dev python app/manage.py create_db_sequence --name core_users_username_seq --start 100 --increment 3

# Create a superuser.
docker exec -it myfolab_core_confetti_dev python app/manage.py create_superuser --email <super_user_email> --password <super_user_password>
```

Navigate to [localhost:8000/admin](http://localhost:8000/admin/) if everything ran successfully. Login with superuser credentials and you should be able to get into the admin panel.

--

**Important**: Make sure to do the following everytime before pushing your changes to this repository:

Check source code issues and try to resolve them:

```bash
docker exec -it myfolab_core_confetti_dev bandit -r .
docker exec -it myfolab_core_confetti_dev flake8 .
# Or
make check
```

Finally format code:

```bash
docker exec -it myfolab_core_confetti_dev black .
docker exec -it myfolab_core_confetti_dev isort .
# Or
make fmt
```

Commit and push if everything is alright.

--

To install a new pip package:

```bash
docker exec -it myfolab_core_confetti_dev pip install tox
```

Sync _requirements.txt_ after installing new packages:

```bash
docker exec -it myfolab_core_confetti_dev pip freeze > requirements.txt
```

--

Generate/Update Translation Files:
```bash
docker exec -it myfolab_core_confetti_dev python app/manage.py makemessages --ignore "venv/**/*.py" --ignore "docker/**/*.py" --ignore "requirements.txt" --locale <locale_code>
```

--

Generate Migrations:
```bash
docker exec -it myfolab_core_confetti_dev python app/manage.py makemigrations
```

--

Generate OpenAPI schema file:
```bash
docker exec -it myfolab_core_confetti_dev python app/manage.py spectacular --file schema.yml
```

Visualize the schema using redoc:
```bash
docker run -it -p 0.0.0.0:8081:80 -v $(pwd)/:/usr/share/nginx/html/swagger/ -e SPEC_URL=swagger/schema.yml redocly/redoc
```

--
