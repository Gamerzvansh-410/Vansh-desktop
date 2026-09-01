import speech_recognition as sr

_recognizer = sr.Recognizer()


def listen(timeout: int | None = 5, phrase_time_limit: int = 8) -> str:
    with sr.Microphone() as source:

        _recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        print("Listening...")

        try:
            audio = _recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

        except sr.WaitTimeoutError:
            return ""

        try:
            text = _recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            return text.lower().strip()

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return ""