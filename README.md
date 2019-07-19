# Docker Container Flask Template

A python flask web service template running in a docker container.

## Getting Started

Firstly, you must install [Docker](https://www.docker.com/).

### Running app locally

```
virtualenv docker-flask-template-venv

# Windows
docker-flask-template-venv\Scripts\activate
# Or Linux
source docker-flask-template-venv/bin/activate
```

Clone the git repo:

```
git clone https://github.com/celikfatih/docker-flask-template.git
```

Build a Docker:

```
cd docker-flask-template/
docker build -t dockerflaskapp:latest .
```

Successfully build has been check: 

```
docker images
``` 

Run the Flask in Docker Container:

```
docker run -it dockerflaskapp

# Or specific port
docker run -it -d -p 5000:5000 dockerflaskapp
```

## In Addition

Open ```Dockerfile``` for change the ```Flask``` project port and changed this line:

```
EXPOSE 5000
``` 
 




