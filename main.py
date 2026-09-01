from Vansh.config import WAKE_WORDS
from Vansh.stt import listen
from Vansh.tts import speak
from Vansh.skills import handle_command

def main():
    speak(
        "Vansh is online. "
        "Say Vansh to give me a command."
    )


while True:
    text = listen(
        timeout=None,
        phrase_time_limit=5
    )

    print(f"DEBUG - Heard: {repr(text)}")

    if not text:
        continue

    if any(word in text for word in WAKE_WORDS):
        print("DEBUG - Wake word detected!")

        speak("How can I help you?")

        command_text = listen(
            timeout=5,
            phrase_time_limit=8
        )

        print(
            f"DEBUG - Command: "
            f"{repr(command_text)}"
        )

        if not command_text:
            speak(
                "I can't hear you. "
                "Please try again."
            )
            continue

        response = handle_command(command_text)

        print(
            f"DEBUG - Response: "
            f"{repr(response)}"
        )

        if response == "__EXIT__":
            speak("Okay, see you!")
            break

        speak(response)


if name == "main":
    main()
