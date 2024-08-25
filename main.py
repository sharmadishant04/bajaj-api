from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    try:
        with open("index.html") as file:
            return HTMLResponse(file.read())
    except FileNotFoundError:
        return HTMLResponse("File not found", status_code=404)

@app.post("/bfhl")
async def bfhl(data: dict):
    # Extract data from the request
    numbers = [item for item in data.get("data", []) if item.isdigit()]
    alphabets = [item for item in data.get("data", []) if item.isalpha()]
    highest_lowercase_alphabet = [char for char in alphabets if char.islower()]
    highest_lowercase_alphabet.sort()
    if highest_lowercase_alphabet:
        highest_lowercase_alphabet = [highest_lowercase_alphabet[-1]]
    else:
        highest_lowercase_alphabet = []
    
    return {
        "is_success": True,
        "user_id": "sharmadishant04",
        "email": "sharmadishant04@gmail.com",
        "roll_number": "21BIT0365",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

@app.get("/bfhl")
async def bfhl_get():
    return {"operation_code": 1}
