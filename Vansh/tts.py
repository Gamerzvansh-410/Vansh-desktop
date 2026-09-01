import asyncio
import os
import tempfile

import edge_tts
from playsound import playsound

from Vansh.config import EDGE_VOICE, EDGE_RATE

_AUDIO_FILE = os.path.join(
tempfile.gettempdir(),
"Vansh_voice.mp3"
)

async def _generate_audio(text: str):
    communicate = edge_tts.Communicate(
        text,
        voice=EDGE_VOICE,
        rate=EDGE_RATE
    )   


await communicate.save(_AUDIO_FILE)


def speak(text: str):
    print(f"Vansh: {text}")


    try:
        asyncio.run(_generate_audio(text))
        playsound(_AUDIO_FILE)

    except Exception as e:
        print(
            "Error generating or playing audio. "
            f"Error: {e}"
        )

