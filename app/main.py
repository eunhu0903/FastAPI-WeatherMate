from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core import weather
from db.database import engine, Base
from routers import auth, weather

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(weather.router)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}