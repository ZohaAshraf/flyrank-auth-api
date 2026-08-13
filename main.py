from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional
from auth import supabase

app = FastAPI(title="FlyRank Auth API")

class AuthRequest(BaseModel):
    email: str
    password: str

@app.get("/")
def root():
    return {"message": "Server running and connected to Supabase"}

@app.post("/auth/signup", status_code=201)
def signup(payload: AuthRequest):
    if not payload.email or not payload.password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    try:
        result = supabase.auth.sign_up({
            "email": payload.email,
            "password": payload.password
        })
        return result.user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/auth/login")
def login(payload: AuthRequest):
    if not payload.email or not payload.password:
        raise HTTPException(status_code=400, detail="Email and password are required")

    try:
        result = supabase.auth.sign_in_with_password({
            "email": payload.email,
            "password": payload.password
        })
        return {
            "access_token": result.session.access_token,
            "refresh_token": result.session.refresh_token
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid login credentials")


@app.get("/public/info")
def public_info():
    return {"message": "Welcome stranger! This info is public."}


@app.get("/protected/profile")
def protected_profile(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Access token required")

    token = authorization.split(" ")[1]
    # Not verifying yet — just checking a token was presented (Stage 3 does real verification)
    return {"message": "Token received (not yet verified)"}