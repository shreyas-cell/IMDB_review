IMDB Review is a fantastic and feature-rich application that does amazing things.

Installation required:- 
1. Python IDE
2. MySQL
3. Install any database administration and development tool (SQL Workbench preferred)
4. Docker



To run IMDB Review, follow these steps:
1. to deploy the pipeline on kubernetes you will need to create account on GCP by going to google and type google console and create and account which will you 300$ credits.
2. go to dashboard and create your project.
3. navigate to left pane go to IAM and admin -> manage resources and select your project.
4. open terminal and clone this project "git clone https://github.com/pycaret/pycaret-deployment-google.git" , after cloning change the directory to IMDB_review.
5. run this command to set project environment variable "export PROJECT_ID="replace-this-with-your-current instance"".
6. to build docker image "docker build -t gcr.io/${PROJECT_ID}/IMDB-app:v1 ."
7. check available images "docker images"
8. upload container image "gcloud auth configure-docker gcr.io"
authorise the popup prompt.
9. upload docker image to GCR "docker push gcr.io/${PROJECT_ID}/IMDB-app:v1"
10. create zone  
"gcloud config set project $PROJECT_ID 
gcloud config set compute/zone us-west1-c"
you can choose different zone by using "gcloud zones --help" and choose prefered zone.
11. create cluster "gcloud container clusters create insurance-cluster --num-nodes=1"
12. deploy app "kubectl create deployment IMDB-app --image=gcr.io/${PROJECT_ID}/IMDB-app:v1"
13. expose app to internet "kubectl expose deployment IMDB-app --type=LoadBalancer --port 80 --target-port 8080"
14. check service if IP is allocated "kubectl get service"
15. if external IP is allocated copy IP and test app in browser. 