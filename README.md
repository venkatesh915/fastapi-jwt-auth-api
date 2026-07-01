# 🚀 FastAPI JWT Auth API (Docker + PostgreSQL)

A production-ready backend API built with **FastAPI**, featuring **JWT authentication**, **PostgreSQL database**, and fully containerized using **Docker & Docker Compose**.

---

## 📌 Features

- 🔐 User Registration & Login
- 🧑 JWT Authentication (Access Token)
- 🔒 Password Hashing (bcrypt)
- 🐘 PostgreSQL Database Integration
- 🐳 Docker & Docker Compose Support
- ⚡ FastAPI Swagger UI (/docs)
- 📦 Production-ready backend structure
- 🧾 Clean modular code architecture

---

## 🛠 Tech Stack

- FastAPI
- Python 3.12
- PostgreSQL
- SQLAlchemy
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn
- Docker
- Docker Compose

---

## 📁 Project Structure

fastapi-jwt-auth-api/
│
├── main.py
├── models.py
├── database.py
├── auth.py
├── schemas.py
├── routes/
│ ├── auth.py
│ └── user.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md


---

## 🚀 Setup & Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/venkatesh915/fastapi-jwt-auth-api.git
cd fastapi-jwt-auth-api


2️⃣ Run with Docker (Recommended)
docker compose up --build

2️⃣ Run with Docker (Recommended)
docker compose up --build
