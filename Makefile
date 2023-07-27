build:
	docker compose build
up:
	docker compose up
createdb:
	docker compose exec web python manage.py create_db
down:
	docker compose down -v
test:
	docker compose run app python manage.py test
db:
	docker compose exec db psql --username=$(USERNAME) --dbname=$(DBNAME)
