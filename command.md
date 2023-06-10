

docker login -u rahulmr
(docker hub password)

docker images
docker image ls

docker pull nginx

docker container ls -a
docker ps -a

docker run -it --name web -p 8080:80 -d nginx

docker ps -a