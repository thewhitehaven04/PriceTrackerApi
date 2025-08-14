from fastapi import FastAPI


app = FastAPI()


@app.get("/healthcheck")
def healtcheck():
    return {"status": "ok"}
