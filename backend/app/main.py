from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes
from app.routes import analyze_debug 
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["*"], # frontend
allow_credentials=True,allow_methods=["*"],allow_headers=["*"],)
app.include_router(auth_routes.router)
app.include_router(analyze_debug.router) 