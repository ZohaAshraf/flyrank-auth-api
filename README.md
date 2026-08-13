# FlyRank Auth API

A secure REST API built with FastAPI and Supabase Auth. Handles user signup, login, logout, and protects routes using JWT verification — built as part of FlyRank's Backend Development Track (Week 2, Assignment 4).

## What this project does

- Users sign up and log in through Supabase Auth (Identity Provider)
- Supabase issues a JWT (access token) on login
- Protected routes verify that token via a reusable auth dependency before granting access
- Public routes remain open to everyone
- Fully documented and testable through Swagger UI with Bearer auth

## Setup

1. Clone this repo:
```bash
   git clone https://github.com/ZohaAshraf/flyrank-auth-api.git
   cd flyrank-auth-api
```

2. Create a virtual environment and activate it:
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
```

3. Install dependencies:
```bash
   pip install fastapi uvicorn supabase python-dotenv
```

4. Create a `.env` file (use `.env.example` as a template) and fill in your own Supabase project URL and anon key.

## Run it

```bash
uvicorn main:app --reload --port 8000
```

Server runs at `http://localhost:8000`. Interactive docs available at `http://localhost:8000/docs`.

## API Reference

| Method | Route | Description | Auth required |
|--------|-------|-------------|----------------|
| POST | `/auth/signup` | Create a new user account | No |
| POST | `/auth/login` | Log in and receive a JWT | No |
| POST | `/auth/logout` | End the current session | Yes |
| GET | `/protected/profile` | Get the logged-in user's profile | Yes |
| GET | `/protected/dashboard` | Example second protected route | Yes |
| GET | `/public/info` | Open, unauthenticated info | No |

## Swagger UI

![Swagger screenshot](<img width="713" height="415" alt="Screenshot 2026-08-13 115758" src="https://github.com/user-attachments/assets/bc9091dc-51e6-4c9d-9e22-6c0d410d157d" />
)

Bearer auth is fully wired up — click **Authorize**, paste your access token, and test any protected route directly from the browser.
