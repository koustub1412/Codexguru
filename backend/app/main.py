from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth_routes, analyze_debug
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allowed origins
origins = [
    "https://codexguru.vercel.app",
    "https://codexguru-md5xty3nc-koustub-maktals-projects.vercel.app",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_routes.router)
app.include_router(analyze_debug.router)
