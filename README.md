# Music-Recommendation-System

# Problem and Solution
Problem: Create a Music recommendation Streamlit -WebApp to Deploy on AWS-ECS, having CICD. A Streamlit web-app which can be used to get recommendations of song, the app recommends a list of media according to the input.
Solution:
  •	The Streamlit application is developed, clusters are made for all songs based on different parameters (Modeling) and tested on a local development environment.
  •	Based on those, whenever a song is choose/write in input. We run the model and place that song in an existing cluster and top 10/15 songs on popularity will be display to the user.
  •	GitHub actions are executed to build and deploy the application to production environment (CICD).
  •	Docker image is created for web-app and pushed to ECR and then image deployed to ECS that for final deployment (use: Docker is used to create a container image of the application, which can be easily deployed on any system that supports Docker).

# Architectural Diagram 
The Streamlit application is developed and tested on a local development environment. GitHub actions are executed to build and deploy the application to production environment. Docker image is created for web-app and pushed to ECR and then to ECS that for final deployment (use: Docker is used to create a container image of the Flask application, which can be easily deployed on any system that supports Docker).

## User flow 
The code of web-app is in VsCode and tested on local environment before pushing to GitHub repository. After pushing to GitHub repo, a docker image is created and push to AWS-ECR using GitHub actions (For CICD). Then docker-image is deployed on AWS-ECS as final production environment.
The application is accessible through AWS-ECS exposed port on the host machine.
