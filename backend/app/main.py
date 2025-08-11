from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes import auth_routes, analyze_debug
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allowed origins (no "*" here if using credentials)
origins = [
    "https://codexguru.vercel.app",
    "https://codexguru-md5xty3nc-koustub-maktals-projects.vercel.app",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # explicit list
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fallback handler for OPTIONS requests
@app.options("/{rest_of_path:path}")
async def preflight_handler(rest_of_path: str):
    return JSONResponse(content={}, status_code=200)

app.include_router(auth_routes.router)
app.include_router(analyze_debug.router)
