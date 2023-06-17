


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


