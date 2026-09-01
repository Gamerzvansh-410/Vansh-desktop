from fastapi import FastAPI
from jarvis.skills import handle_command
import uvicorn

app = FastAPI(title="Jarvis Remote API")


@app.get("/command")
def run_command(text: str):
    reply = handle_command(text)
    if reply == "__EXIT__":
        reply = "Theek hai, bye!"
    return {"reply": reply}


@app.get("/")
def health_check():
    return {"status": "Jarvis online hai"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)