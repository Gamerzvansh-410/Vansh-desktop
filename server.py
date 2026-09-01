from fastapi import FastAPI
from Vansh.skills import handle_command

app = FastAPI()

@app.get("/")
def home():
    return {
"message": "Vansh Desktop API is running"
}

@app.get("/command")
def command(text: str):
    response = handle_command(text)

    return {
        "command": text,
        "response": response
    }
