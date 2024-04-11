import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def index():
    return "Hello Weather app!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
