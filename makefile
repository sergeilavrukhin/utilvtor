start:
	@docker-compose start

devstart:
	@docker-compose -f docker-compose.dev.yml start

stop:
	@docker-compose stop

devstop:
	@docker-compose -f docker-compose.dev.yml stop

up:
	@docker-compose up -d

devup:
	@docker-compose -f docker-compose.dev.yml up -d

devdown:
	@docker-compose -f docker-compose.dev.yml down

open:
	@docker exec -it mshc_$(app) /bin/sh

gen_api_client:
	@raml2html -o "./src/front/client/public/api.html" "./src/front/client/raml/api.raml"

front_client:
	@npm --prefix ./src/front/client run build