import speech_recognition as sr

_recognizer = sr.Recognizer()


def listen(timeout: int = 5, phrase_time_limit: int = 8) -> str:
    with sr.Microphone() as source:
        _recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("I'm listening...")
        try:
            audio = _recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            return ""

    try:
        text = _recognizer.recognize_google(audio, language="en-IN")
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownvalueError:
        return ""
    except sr.RequestError:
        print("Check your internet connection -- Can't reach speeech recognition.")
        return ""