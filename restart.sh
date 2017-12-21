docker-compose stop \
	&& docker-compose rm \
	&& docker-compose build
docker-compose run --rm web upgrade
docker-compose up -d