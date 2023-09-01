from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rotue import LoginRoute
from rotue import SignUpRoute
from rotue import SongsRoute

app = FastAPI(
    title="Musify",
    description="Free Music Site!🚀",
    version="0.0.1",
    docs_url="/api",
    redoc_url="/redoc",
    contact={
        "name": "API Details & Documentation",
        "url": "https://pending.com",
    },
)

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Example frontend URL
    "https://your-production-frontend-url.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(SignUpRoute.SignUp)
app.include_router(LoginRoute.Login)
app.include_router(SongsRoute.Songs)

@app.get("/")
def read_root():
    return {"🚀": "Musify is Live"}
