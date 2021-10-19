* Install Docker Compose following the tutorial: https://docs.docker.com/compose/install/
* Build image: docker-compose build
* Start services: docker-compose up -d
* Run migrations: docker-compose exec web python manage.py migrate
* Create Django admin user: docker-compose exec web python manage.py createsuperuser
* Url: http://0.0.0.0:8000/