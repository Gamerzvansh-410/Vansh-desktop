import datetime
import webbrowser
import subprocess
import platform

def tell_time() -> str:
    now = datetime.datetime.now().strftime("%l:%M %p")
    return f"Current time is {now}"

def tell_date() -> str:
    today = datetime.datetime.now().strftime("%d %B, %Y")
    return f"today's date is {today}"


def open_website(site: str) -> str:
    urls={
        "youtube":"https://www.youtube.com",
        "google":"https://www.google.com",
        "gmail":"https://www.mail.google.com",
        "whatsapp":"https://web.whatsapp.com",
    }

    url = urls.get(site)
    if url:
        webbrowser.open(url)
        return f"I'm opening {site}"
    return f"I don't know {site}"

def open_app(app_name: str) -> str:
    system = platform.system()
    try:
        if system =="windows":
            subprocess.Popen(f"start {app_name}", shell =True)
        elif system == "Darwin":
            subprocess.Popen(["open","-a", app_name])
        else:
            subprocess.Popen([app_name])
        return f"{app_name} opening"
    except Exception:
        return f"{app_name} not opening, Is the name is correct?"


def handle_command(command: str) -> str:
    command = command.lower()

    if "time" in command:
        return tell_time()
    if "date" in command:
        return tell_date()
    if "open" in command:
        for site in ["youtube","google","gmail","whatsapp"]:
            if site in command:
                return open_website(site)
        app_name = command.replace("open","").strip()
        if app_name:
            return open_app(app_name)
    if "stop" in command or "bye" in command or "exit" in command:
        return "__EXIT__"

    return "Sorry, i didn't understand the command, try saying in different way"