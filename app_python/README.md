# Moscow Time Web Application

![CI Workflow Status](https://github.com/eeetaF/S24-devops-labs/actions/workflows/ci.yml/badge.svg)

## Overview

This is a simple Flask web application that displays the current time in Moscow. It uses Flask to handle routing, `pytz` to manage timezone conversions, and serves a static image from the `/static` folder. The app is lightweight and demonstrates basic Flask functionality.

## Run the project locally
### 1. Clone the repository
```bash
git clone https://github.com/eeetaF/S24-devops-labs/tree/lab2
```
### 2. Create local environment
```bash
python -m venv venv
```
### 3. Activate local environment
```bash
venv\Scripts\activate
```
### 4. Install requirements
```bash
pip install -r requirements.txt
```
### 5. Run application
```bash
python app.py
```
### 6. Follow http://127.0.0.1:5000/

## How to Build the Docker Image
### 1.1 Build the application
```bash
docker build -t <dockerhub_username>/moscow-time-app .
``` 
### 1.2 Or pull the application from dockerhub
you may use my public image by entering "Fatee" as <dockerhub_username>
```bash
docker pull <dockerhub_username>/moscow-time-app:latest
```
### 2. Run the Docker Container
```bash
docker run -p 5000:5000 <dockerhub_username>/moscow-time-app
```
### 3. Follow http://127.0.0.1:5000/
### *4. Stop the Docker Container
```bash
docker ps
```
```bash
docker stop <container_id>
```
### *5. Remove the Docker Container
```bash
docker rm <container_id>
```
### *6. Remove the Docker Image
```bash
docker rmi <dockerhub_username>/moscow-time-app
```

## Unit Tests
This application includes a suite of unit tests to ensure that it functions correctly and meets requirements. For more information, see `PYTHON.md`
### Running Unit Tests
```bash
python -m unittest discover -s tests
```

## CI Workflow
This project utilizes GitHub Actions for Continuous Integration (CI) to automate the development process. The CI workflow ensures code quality and automates Docker image deployment to Docker Hub.

### CI Workflow Overview
Look for `ci.yml` in `.github/workflows/ci.yml`
The CI workflow includes the following essential steps:
1. Dependencies: Sets up the Python environment and installs project dependencies.
2. Linter: Runs `flake8` to enforce code style and quality standards.
3. Tests: Executes unit tests to verify application functionality.
4. Docker Login: Authenticates with Docker Hub using secure credentials.
5. Build and Push Docker Image: Builds the Docker image and pushes it to Docker Hub for deployment.

### Secrets Configuration
To securely store sensitive information, the workflow uses GitHub Secrets:
- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password or access token.

### Workflow Badge
The workflow status badge at the top of this `README.md` provides real-time visibility into the CI pipeline status.

![CI Workflow Status](https://github.com/eeetaF/S24-devops-labs/actions/workflows/ci.yml/badge.svg)