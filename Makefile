APP_NAMESPACE="sparkle.app=api"

web:
		docker-compose up --build -d

migrate_db:
	docker-compose exec web \
		/bin/sh -c 'python manage.py migrate'

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti nz01 /bin/sh

shell-web:
	docker exec -ti web /bin/sh

shell-db:
	docker exec -ti pz01 /bin/sh

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db

collectstatic:
	docker exec web /bin/sh -c "python manage.py collectstatic --noinput"

stop_all_containers: # Do not change name without changing mworker.service ExecStop in AMI
	-docker stop $$(docker ps -q --filter label=${APP_NAMESPACE})

clean:
	-docker system prune -f -a --filter label=${APP_NAMESPACE}