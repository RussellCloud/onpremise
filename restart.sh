docker-compose stop \
	&& docker-compose rm \
	&& docker-compose rebuild
docker-compose run --rm web upgrade
docker-compose up -d