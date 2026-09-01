import asyncio
import os
import platform
import subprocess
import tempfile

import edge_tts

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


def _play_audio():
    system = platform.system()

    if system == "Darwin":
        # macOS
        subprocess.run(
            ["afplay", _AUDIO_FILE],
            check=True
        )

    elif system == "Linux":
        # Linux
        subprocess.run(
            ["mpg123", "-q", _AUDIO_FILE],
            check=True
        )

    elif system == "Windows":
        # Windows
        subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                f'(New-Object Media.SoundPlayer "{_AUDIO_FILE}").PlaySync()'
            ],
            check=True
        )

    else:
        raise RuntimeError(
            f"Unsupported operating system: {system}"
        )


def speak(text: str):
    print(f"Vansh: {text}")

    try:
        asyncio.run(_generate_audio(text))
        _play_audio()

    except Exception as e:
        print(f"TTS error: {e}")