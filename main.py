from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"body": "This is the / endpoint"}
