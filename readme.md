# Memory App — DevOps & SRE Project

<p align="center">
  <strong>A hands-on project to learn Kubernetes monitoring, alerting, and incident investigation.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?logo=kubernetes&logoColor=white" alt="Kubernetes">
  <img src="https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus&logoColor=white" alt="Prometheus">
  <img src="https://img.shields.io/badge/Grafana-Dashboards-F46800?logo=grafana&logoColor=white" alt="Grafana">
</p>

## About the Project

I'm building this project to improve my hands-on skills in DevOps and Site Reliability Engineering (SRE).

I wanted to work on a project where I could bring different tools together and understand how they work in a real environment, rather than learning each tool separately.

I started with a simple Python application that intentionally consumes increasing amounts of memory. I containerized it using Docker and deployed it to Kubernetes with resource limits.

The goal is to understand what happens when an application runs out of memory, how Kubernetes handles the failure, and how monitoring and alerting help identify and investigate the issue.

This is a work in progress, and I'm building it step by step as I learn.

## Project Architecture

The current monitoring workflow looks like this:

```text
                 Python Memory App
                         |
                         v
                       Docker
                         |
                         v
                     Kubernetes
                         |
             +-----------+-----------+
             |                       |
             v                       v
        App Metrics             HTTP Health Check
             |                       |
             v                       v
        Prometheus             Blackbox Exporter
             |                       |
             +-----------+-----------+
                         |
                         v
                       Grafana
                         |
                +--------+--------+
                |                 |
                v                 v
             Dashboard          Alerts
                                   |
                                   v
                              Email Alerts
```

The application runs in Kubernetes. Prometheus collects monitoring metrics, while Blackbox Exporter checks whether the application's HTTP health endpoint is responding. Grafana brings this information together through dashboards and alert rules.

## What I've Implemented

### 1. Python Application and Testing

- Created a Python application with a `/healthcheck` endpoint.
- Set up a Python virtual environment.
- Added automated tests using `pytest`.
- Ran the test suite successfully, with all 6 tests passing.

The health-check endpoint gives me a simple way to check whether the application is responding to HTTP requests.

### 2. Docker Containerization

- Created a Dockerfile using `python:3.12-slim`.
- Configured the container to run as a non-root user.
- Built the `memory-app:v1` Docker image.
- Ran the application with a memory limit of 400 MiB.
- Verified that the health-check endpoint returned HTTP 200 OK.
- Monitored memory consumption using `docker stats`.
- Confirmed an out-of-memory termination using Docker inspection.

This helped me understand Docker images, containers, port mapping, resource limits, and OOMKilled behavior.

### 3. Kubernetes Deployment

- Set up a local Kubernetes environment using Docker Desktop.
- Deployed multiple versions of the Memory App.
- Configured a Kubernetes Service to expose the application inside the cluster.
- Observed pod readiness, container restarts, and memory-related failures.

The memory consumption is intentional. I'm using this behavior to understand how Kubernetes responds when a container exceeds its memory limit and how application availability is affected.

### 4. Monitoring with Prometheus and Grafana

I configured Prometheus, Grafana, and Blackbox Exporter to monitor the application.

**Prometheus** collects metrics that help me understand the state of the application and its Kubernetes resources.

**Grafana** lets me visualize these metrics in dashboards and evaluate alert rules.

**Blackbox Exporter** checks the application's HTTP health endpoint from outside the application process.

#### Grafana Dashboard

I've created a dashboard named **Memory App - SRE Overview** with four panels:

| Panel | What it tells me |
|---|---|
| Ready Pods | How many application pods are ready |
| Memory Usage by Pod | How much memory each application pod is using |
| Pod Restarts | How frequently containers are restarting |
| HTTP Health Check | Whether the HTTP health check is succeeding |

These panels help me compare resource consumption with application availability and investigate failures.

### 5. Alerting and Email Notifications

I've configured Grafana alert rules for the following conditions:

| Alert | Purpose |
|---|---|
| Memory App Pod Unavailable | Detects when application pods are not ready |
| Memory App OOMKilled | Detects memory-related container terminations |
| Memory App Health Check Failed | Detects unsuccessful HTTP health checks |

I've also configured a Grafana contact point and verified that email notifications are reaching me.

I'm continuing to investigate alert states such as `Pending` and `NoData` so I can understand how they differ from normal and firing alerts.

## Technology Stack

| Technology | How I'm using it |
|---|---|
| Python | Application development |
| pytest | Automated testing |
| Docker | Building and running containers |
| Kubernetes | Deploying and managing application pods |
| kubectl | Interacting with Kubernetes |
| Helm | Managing Kubernetes chart installations |
| Prometheus | Collecting and querying metrics |
| Grafana | Dashboards and alerting |
| Blackbox Exporter | HTTP health checks |
| Git and GitHub | Version control and project tracking |
| WSL Ubuntu | Local development environment |

## What I'm Learning

Through this project, I'm working on understanding:

- How Docker packages and runs applications.
- How Kubernetes manages deployments, services, and pods.
- Why containers are OOMKilled and how memory limits affect them.
- How to monitor application health and resource consumption.
- How to build Grafana dashboards using Prometheus queries.
- How alert rules detect failures and trigger email notifications.
- How to troubleshoot pod readiness, restarts, and failed health checks.
- How to use monitoring data to investigate an incident instead of guessing at the cause.

My focus is on understanding **what happened, why it happened, and how to prove it using the available evidence**.

## What's Next?

I'm continuing to develop the project in the following areas:

- Investigate and validate the remaining alert-state issues.
- Perform a structured incident investigation using the intentional memory leak.
- Correlate memory usage, pod restarts, readiness, and HTTP health-check results.
- Document the incident, findings, and troubleshooting steps.
- Review the project setup and add clear instructions for reproducing it.
- Validate the GitOps workflow with Argo CD.
- Continue with CI/CD, security checks, and centralized logging.

These items will be marked complete once I've implemented and verified them.

## Project Status

The application, Docker containerization, Kubernetes deployment, Prometheus monitoring, Grafana dashboard, and alerting configuration are in place.

I'm currently focusing on validating the monitoring behavior and improving my incident investigation skills. I'll continue extending the project with additional DevOps and SRE practices as I progress.

This project is helping me connect the tools I've been learning and understand how monitoring and troubleshooting fit into day-to-day SRE work.
