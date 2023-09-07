# docker_flask
```
git clone https://github.com/limelee85/docker_flask.git
cd docker_flask
docker build -t flasktest .
docker run -d -p 0.0.0.0:5000:5000/tcp --name sstitest flasktest:latest
```
