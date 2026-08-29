import asyncio
import os
import tempfile
import edge_tts
from playsound import playsound
from jarvis.config import EDGE_VOICE, EDGE_RATE
 
_AUDIO_FILE = os.path.join(tempfile.gettempdir(),"jarvis_voice.mp3")

async def _generate_audio(text: str):
    communicate = edge_tts.Communicate(text, voice=EDGE_VOICE, rate=EDGE_RATE)
    await communicate.save(_AUDIO_FILE)


async def speak(text: str):
    print(f"jarvis: {text}")
    try:
        asyncio.run(_generate_audio(text))
        playsound(_AUDIO_FILE)
    except Exception as e: 
        print(f"Error generating or playing audio please check your internet connection and the edge_tts library. Error: {e}")
        