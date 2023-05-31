import validators
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import LocalSession, engine
from shorten import generate_key

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


@app.post("/shorten_url")
def root(url: schemas.BaseURL, db: Session = Depends(get_db)):
    is_url = validators.url(url.target_url)
    if not is_url:
        raise_bad_request(message="Not a URL!")

    key = generate_key()
    db_url = models.URL(target_url=url.target_url, key=key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key

    return 


@app.get("/url/{key}")
def redirect(key: str):
    pass
