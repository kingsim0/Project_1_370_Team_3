# Project 1 - Microservices with MongoDB

## Overview
This project is a Python-based microservice application consisting of:

- **User Service** (`userService.py`)
- **Order Service** (`orderService.py`)
- **Product Service** (`productService.py`)
- A shared **MongoDB** database for persistent data

Each service runs on its own port and communicates with MongoDB.

## Technologies
- Python 3.10
- Flask
- Docker + Docker Compose
- MongoDB
- Flask-CORS
- VS Code Insiders + WSL

## Running the Project

### 1. Prerequisites
- Docker & Docker Compose
- VS Code Insiders with WSL (optional, per class instructions)

### 2. Start the App
```bash
docker-compose up --build
