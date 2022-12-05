# Introduction
This is a simple flask web app with one route "/" supported.
The app will have a uuid associated with it.
When you hit the route it will return the uuid of the application.

# Deploying this in minikube
Build the docker image: docker build -t my-flask-app .
start your minikube cluster: minikube start
upload the built docker image to minikube: minikube upload my-flask-app
apply the deployment: kubectl apply -f k8/flask-deployment.yaml
apply the service for the deployment: kubectl apply -f k8/flask-service.yaml
apply the Ingress for the service: kubectl apply -f k8/flask-ingress.yaml
on mac start the minikube tunnel: minikube tunnel
access the application on 127.0.0.1

There are 5 replicas. once on 127.0.0.1 hit refresh multiples times to see the uuid change indication you are getting response from different replicas/pods.