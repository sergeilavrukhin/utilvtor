build:
	@docker-compose up --build -d

up:
	@docker-compose up -d

django:
	@python src/backend/manage.py runserver 127.0.0.1:3030

start:
	@docker-compose start

stop:
	@docker-compose stop

down:
	@docker-compose down

restart: down up

logs:
	@docker-compose logs backend

devbuild:
	@docker-compose -f docker-compose.dev.yml up --build -d

dev:
	@npm --prefix ./src/front/client run dev

open:
	@docker exec -it uv_$(app) /bin/sh

gen_api_client:
	@raml2html -o "./src/front/client/public/api.html" "./src/front/client/raml/api.raml"

front_client:
	@npm --prefix ./src/front/client run dev

front_start:
	./runclient.sh

front_build:
	./buildclient.sh

front_stop:
	@pm2 stop 0

makemigration:
	@./venv/bin/python ./src/backend/manage.py makemigrations

front_client_install:
	@npm --prefix ./src/front/client install

front_client_build:
	@npm --prefix ./src/front/client run build

front_client_start:
	@npm --prefix ./src/front/client run start

front_admin_install:
	@npm --prefix ./src/front/admin install

front_admin_build:
	@npm --prefix ./src/front/admin run build

front_admin_start:
	@npm --prefix ./src/front/admin run start