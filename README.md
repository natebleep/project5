Run the following command to build the container:
docker build --tag=flask-api:v1 .

Run the following command to run the container:
docker run -p 5000:5000 flask-api:v1