from fastapi import FastAPI
from Vansh.skills import handle_command
import uvicorn

app = FastAPI(title="Vansh Remote API")


@app.get("/command")
def run_command(text: str):
    reply = handle_command(text)
    if reply == "__EXIT__":
        reply = "Okay, bye!"
    return {"reply": reply}


@app.get("/")
def health_check():
    return {"status": "Vansh is online"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)