## SparkleSlap API (YEET!)

#### Get a dev environment setup
Get the repo and start the containers.

    git clone https://github.com/wroscoe/sparkle_api
    make web
    
    
Now go inside the docker container create a superuser.

    make shell-web
    python manage.py createsuperuser    
    
    
    
#### Things that work:

* ```localhost:8000``` to see the api explorer.
* ```localhost:8000/admin``` to add quizes


#### Things that are still a mess.
* deploying requires manually chaning the port to 80 in docker compose
* docker doesn't autorebuild when changes are made. 
* making migrations requires getting a shell in the web container
* there is zero code documentation