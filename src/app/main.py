from fastapi import FastAPI
from . import models
from .db import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def read_root():
    return {'Hello': 'World'}
