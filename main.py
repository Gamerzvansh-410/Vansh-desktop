from jarvis.config import WAKE_WORD
from jarvis.stt import listen
from jarvis.tts import speak
from jarvis.skills import handle_command


def main():
    speak(f"Ashborn is online say '{WAKE_WORD}' to give me command.")

    while True:
        text = listen(timeout=None, phrase_time_limit=3)

        if WAKE_WORD in text:
            speak("how can i help you!")
            command_text = listen(timeout=5, phrase_time_limit=8)

            if not command_text:
                speak("Can't hear you, please try. again")
                continue

            response = handle_command(command_text)

            if response == "__EXIT__":
                speak("okay, see yaa!")
                break

            speak(response)


if __name__ == "__main__":
    main()