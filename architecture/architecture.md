# Cloud Tasks Architecture

## Backend Flow

Developer
↓
GitHub
↓
GitHub Actions
↓
Docker
↓
Amazon ECR
↓
Amazon ECS / Fargate
↓
FastAPI
↓
PostgreSQL / RDS

## Frontend Flow

User
↓
CloudFront
↓
Amazon S3
↓
React + TypeScript

## How It Works

The developer writes code and pushes it to GitHub.

GitHub Actions automatically builds and deploys the application.

Docker packages the FastAPI application into a container.

Amazon ECR stores the Docker image.

Amazon ECS / Fargate runs the Docker container.

FastAPI handles API requests and communicates with PostgreSQL.

CloudFront delivers the frontend to users.

Amazon S3 stores the React website files.