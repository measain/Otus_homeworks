from fastapi import FastAPI



app = FastAPI()


@app.get("/")
def zaglushka():
    return {"message": "Перейди на http://localhost:8000/ping/"}


@app.get("/ping")
def ping_pong():
    return {"message": "pong"}