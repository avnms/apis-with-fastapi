from typing import Optional

import fastapi

app = fastapi.FastAPI()


@app.get("/")
def index():
    body = """
        <html>
            <body>
                <h1>Welcome to the Calculator API!</h1>
                <div>
                    "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>"
                </div>
            </body>
        </html>
    """

    return fastapi.responses.HTMLResponse(content=body)


@app.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
            {"error": "ERROR: Z cannot be zero."}, status_code=400
        )

    value = x + y

    if z is not None:
        value /= z

    return {
        "x": x,
        "y": y,
        "z": z,
        "value": value,
    }
