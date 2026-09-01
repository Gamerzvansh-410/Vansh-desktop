from Vansh.config import WAKE_WORDS
from Vansh.stt import listen
from Vansh.tts import speak
from Vansh.skills import handle_command


def contains_wake_word(text: str) -> bool:
    text = text.lower().strip()

    return any(
        word in text
        for word in WAKE_WORDS
    )
    
def main():
    speak(
        "Vansh is online. "
        "Say Vansh to give me a command."
    )

    active = False

    while True:

        if not active:
            text = listen(
                timeout=None,
                phrase_time_limit=5
            )

            if not text:
                continue

            if contains_wake_word(text):
                active = True
                speak("How can I help you?")
            continue

        # ACTIVE CONVERSATION MODE
        command_text = listen(
            timeout=5,
            phrase_time_limit=8
        )

        if not command_text:
            continue

        # Sleep commands
        if any(word in command_text for word in [
            "go to sleep",
            "sleep",
            "bye",
            "goodbye",
            "stop listening"
        ]):
            speak("Okay, going to sleep.")
            active = False
            continue

        response = handle_command(command_text)

        if response == "__EXIT__":
            speak("Okay, see you!")
            break

        speak(response)


if __name__ == "__main__":
    main()