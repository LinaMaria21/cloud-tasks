# Cloud Tasks Architecture
# Notes to explain how forntend and backend works

Backend Flow

text
Developer: developer write code and push it to Github
   ↓
GitHub
   ↓
GitHub Actions: Github actions can automatically build and deploy the application
   ↓
Docker: Docker packages the Fast API aaplication into a container
   ↓
Amazon ECR: ECR stores the docker image
   ↓
Amazon ECS / Fargate: ECS/Fargate runs the docker container
   ↓
FastAPI: the FastAPI application runs inside that container
   ↓
PostgreSQL / RDS: the API saves and reads task data from the postgreSQL database

Frontend Flow

User
 ↓
CloudFront
 ↓
Amazon S3
 ↓
React + TypeScript

User opens the website, Cloudfront delivers the website, s3 stores the website files and React and Typescript is what creates the website the user sees.