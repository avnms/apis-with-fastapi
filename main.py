from fastapi import FastAPI

app = FastAPI()


@app.get("/api/calculate")
def calculate():
    value = 2 + 2
    return {"value": value}
