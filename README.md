# flask-ml

A template to start a web app and deploy to docker

## Build

```
docker build -t app .
docker run -d -p 5000:5000 app
```

Look for `app` when you `docker ps -a` and note the container ID. See the app on `localhost:5000`. Stop using `docker stop [CONTAINER ID]`.

## Run

```
docker-compose up
```
