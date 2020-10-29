Run the following command to build the container:
docker build --tag=flask-api:v1 .

Run the following command to run the container:
docker run -p 5000:5000 flask-api:v1

Start redis server:
  docker run --rm -d --name redis-server --network redisnet redis
start flask server:
  docker run --rm --network redisnet -p 80:5000 
