# DevOps-SRE Project Progress

## Project Summary

This project implements a secure DevSecOps delivery pipeline and a Site Reliability Engineering (SRE) workflow for a Python application with deliberately increasing memory consumption. The objective is to containerize the application, deploy it to Kubernetes using GitOps, and establish monitoring, centralized logging, and alerting.

## Completed Work

### 1. Application Testing
- Set up a Python virtual environment for local development.
- Installed pytest as a development dependency.
- Executed the existing test suite successfully: **6 tests passed**.

### 2. Docker Containerization
- Created a Dockerfile based on `python:3.12-slim`.
- Configured a dedicated non-root user to run the application.
- Set Python environment variables for container-friendly logging and bytecode behavior.
- Built the `memory-app:v1` image successfully.
- Ran the application in a container with a 400 MiB memory limit.
- Verified the `/healthcheck` endpoint returned HTTP 200 OK.
- Monitored resource consumption using `docker stats`.
- Confirmed the container's out-of-memory termination using Docker inspection (`OOMKilled=true`).

### 3. Repository Configuration
- Added `.gitignore` to exclude local Python environments, cache files, test artifacts, and local environment files.
- Added `requirements-dev.txt` for development and testing dependencies.
- Created a dedicated GitHub repository for this project.

## Work in Progress

- Kubernetes application deployment and resource configuration.
- Secure CI/CD workflows, including code quality and vulnerability scanning.
- GitOps deployment automation using Argo CD.
- Prometheus and Grafana monitoring, centralized logging, and alerting.
- Kubernetes security controls and resource governance.

## Technology Stack

**Implemented:** Python, pytest, Docker, Git, GitHub.

**Planned:** GitHub Actions, Kubernetes, Argo CD, Helm, Prometheus, Grafana, and a centralized logging solution.

## Project Status

The application has been tested locally and containerized successfully. Kubernetes deployment, secure CI/CD, GitOps automation, and observability remain to be implemented and validated.

---

