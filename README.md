# Insurance Management System

A microservices-based Insurance Management System built using Flask, Docker, and Kubernetes.

## Services

### Auth Service
- Register Users
- Login Users

### User Service
- Manage User Information

### Policy Service
- Fetch Available Insurance Policies

### Claim Service
- Manage Insurance Claims

### Recommendation Service
- Recommend Insurance Policies Based on Age

## Project Structure

```text
insurance-project/
│
├── services/
│   ├── auth-service/
│   ├── user-service/
│   ├── policy-service/
│   ├── claim-service/
│   └── recommendation-service/
│
├── k8s/
│   ├── mysql-deployment.yaml
│   ├── mysql-service.yaml
│   ├── user-deployment.yaml
│   ├── policy-deployment.yaml
│   ├── claim-deployment.yaml
│   ├── recommendation-deployment.yaml
│   └── loadbalancer-service.yaml
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── Dockerfile
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Build Docker Images

```bash
docker-compose build
```

## Run Project

```bash
docker-compose up -d
```

## Check Running Containers

```bash
docker ps
```

## APIs

### Auth Service

Register:

```http
POST http://localhost:5000/register
```

Login:

```http
POST http://localhost:5000/login
```

### User Service

```http
GET http://localhost:5001/users
```

### Policy Service

```http
GET http://localhost:5002/policies
```

### Claim Service

```http
GET http://localhost:5003/claims
```

### Recommendation Service

```http
GET http://localhost:5004/recommend/30
```

Expected Response:

```json
{
  "age": 30,
  "recommendation": "Health Insurance"
}
```

## Stop Project

```bash
docker-compose down
```