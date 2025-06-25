from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes, analyze

app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:3000"], # frontend
allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)
app.include_router(auth_routes.router)
app.include_router(analyze.router)
