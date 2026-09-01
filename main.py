from jarvis.config import WAKE_WORD
from jarvis.stt import listen
from jarvis.tts import speak
from jarvis.skills import handle_command


def main():
    speak(f"Ashborn online hai. '{WAKE_WORD}' bolke mujhe bulao.")

    while True:
        text = listen(timeout=None, phrase_time_limit=3)

        if WAKE_WORD in text:
            speak("Ji boliye")
            command_text = listen(timeout=5, phrase_time_limit=8)

            if not command_text:
                speak("Kuch sunayi nahi diya, dobara try karo")
                continue

            response = handle_command(command_text)

            if response == "__EXIT__":
                speak("Theek hai, milte hain!")
                break

            speak(response)


if __name__ == "__main__":
    main()