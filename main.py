from typing import Optional

import fastapi

app = fastapi.FastAPI()


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
