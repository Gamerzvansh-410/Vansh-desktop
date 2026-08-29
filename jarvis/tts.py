import asyncio
import os
import tempfile
import edge_tts
from playsound import playsound
from jarvis.config import EDGE_VOICE, EDGE_RATE
 
_AUDIO_FILE = os.path.join(tempfile.gettempdir(),"jarvis_voice.mp3")

async def _generate_audio(text: str):
    communicate = edge_tts.Communicate

