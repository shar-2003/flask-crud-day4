


https://github.com/rcoem-devops/flask-crud


docker login -u rahulmr
(docker hub password)

docker images
docker image ls

docker pull nginx

docker container ls -a
docker ps -a

docker run -it --name web -p 8080:80 -d nginx

docker ps -a

docker exec -it web /bin/bash

cat /etc/os-release 


docker build -t rahulmr/flask-crud:v1 .

docker image ls

docker push rahulmr/flask-crud:v1



docker run -it --name flask -p 8090:5000 -d rahulmr/flaskcrud:v1

docker ps -a

docker exec -it flask /bin/sh



docker rm -f flask
docker rm -f web


docker compose version

docker compose help > help_commands_compose.txt

docker ps -a

docker compose up

docker-compose up



docker ps -a
docker stop flask
docker ps 

docker compose up

docker compose down

docker compose -f docker-compose.1.yml up -d
docker compose logs -f 
control + c

docker compose down

docker-compose up

docker compose down

docker co

docker run -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:alpine


java -jar jenkins.war --httpPort=8090

Testing the trigger


