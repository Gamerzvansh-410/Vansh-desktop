# Vansh

A Python voice assistant (Jarvis-style) for **Windows, macOS, and Linux**.

## Features

- Wake word activation ("Vansh")
- Voice commands — time, date, open websites/apps
- Remote control via REST API (control from any device on your network)
- Natural-sounding voice replies (Edge TTS)

## Requirements

- Python 3.9+
- Microphone
- Internet connection (required for TTS and speech recognition)

## Installation

```bash
git clone https://github.com/Gamerzvansh-410/Vansh-desktop.git
cd Vansh-desktop
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Windows** — if `pyaudio` fails to install:
```bash
pip install pipwin
pipwin install pyaudio
```

**macOS** — install portaudio first:
```bash
brew install portaudio
pip install pyaudio
```

**Linux** — install portaudio first:
```bash
sudo apt install portaudio19-dev python3-pyaudio
```

## Usage

```bash
python3 main.py
```

Say **"Vansh"** to activate, then speak your command (e.g. "tell time", "open youtube").

## Remote Control

Run the server on your PC to control Vansh from another device on the same network:

```bash
python3 server.py
```

Find your PC's local IP (`ipconfig` on Windows, `ifconfig` on macOS/Linux). From another device:

```
http://<PC-IP>:8000/command?text=your+command
```

### iPhone (Siri Shortcuts)

1. Create a new Shortcut
2. Add action **"Get Contents of URL"** pointing to the server URL above
3. Extract the `reply` field from the response
4. Add a **"Speak Text"** action with that field
5. Add the Shortcut to Siri with a custom phrase

## Changing the Voice

Edit `EDGE_VOICE` in `jarvis/config.py`. List all available voices:
```bash
edge-tts --list-voices
```

**Windows** — if `playsound` errors with "No module named 'win32com'":
```bash
pip install pywin32
```

## Adding a New Skill

Add a function in `jarvis/skills.py`, then map it inside `handle_command()`.

## Notes

- Uses basic keyword matching, not full natural language understanding
- Speech recognition uses Google's free API (requires internet); for fully offline STT, consider the Vosk library
