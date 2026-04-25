# DevSecOps Kubernetes Security Project

This project demonstrates a progressive DevSecOps approach for securing a cloud-native application deployed on a Kubernetes k3s cluster.

The goal is to start from a basic vulnerable deployment, simulate a Kubernetes attack scenario, analyze the impact, and then apply security corrections to reduce the attack surface.

## Project Overview

The project is divided into three phases:

1. **DEV** — Build and understand the application attack surface  
2. **DEVOPS** — Automate deployment, observe the system, and correct weaknesses  
3. **DEVSECOPS** — Strengthen security, validate protections, and block the attack chain  

## Architecture

The application is based on a simple cloud-native architecture composed of:

- Frontend service
- Backend API
- Database
- Kubernetes k3s cluster
- Master node and worker node

## Attack Scenario

A vulnerable application was deployed in a Kubernetes namespace in order to simulate a compromise.

The attack scenario demonstrated how a compromised pod could:

- Access the ServiceAccount token
- Query the Kubernetes API
- List pods and secrets
- Decode sensitive data stored in Kubernetes secrets

This showed the risks of excessive RBAC permissions and automatic ServiceAccount token mounting.

## Security Corrections

Several security measures were applied after the attack simulation:

- Reduced RBAC permissions
- Removed access to Kubernetes secrets
- Disabled automatic ServiceAccount token mounting
- Added restrictive NetworkPolicy rules
- Verified that the token was no longer accessible
- Verified that the attack could no longer be reproduced

## DevSecOps Practices

The project also includes DevSecOps practices such as:

- Docker containerization
- Kubernetes manifests
- CI/CD pipeline logic
- Security scanning with Trivy
- Observability using logs, events, and metrics
- Progressive hardening of the Kubernetes environment

## Technologies Used

- Kubernetes / k3s
- Docker
- Python Flask
- YAML
- RBAC
- NetworkPolicy
- ServiceAccount
- kubectl
- Trivy
- GitHub

## Repository Structure

```text
devsecops-kubernetes-security-project/
├── app/
│   ├── app2/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── deployment.yaml
│   └── service.yaml
│
├── k8s/
│   ├── backend.yaml
│   ├── frontend.yaml
│   ├── db.yaml
│   ├── dvwa.yaml
│   ├── role.yaml
│   ├── rolebinding.yaml
│   ├── deny-all.yaml
│   └── network policy files
│
└── README.md
