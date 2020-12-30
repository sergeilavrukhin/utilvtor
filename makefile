build:
	@docker-compose up --build -d

up:
	@docker-compose up -d

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