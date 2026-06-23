import speech_recognition as sr
import pyttsx3
import time
import datetime
import os
import subprocess
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import threading
import musicLibrary

# ------------------ Text to Speech (pyttsx3) ------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # 0 = male, 1 = female

def speak(text):
    print("Jarvis:", text)
    log_message("Jarvis: " + text)
    engine.say(text)
    engine.runAndWait()

# ------------------ Memory Functions ------------------
MEMORY_FILE = "memory.txt"

def save_memory(text):
    now = datetime.datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")
    entry = f"{text} (saved on {now})"
    with open(MEMORY_FILE, "a", encoding="utf-8") as f:
        f.write(entry + "\n")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def clear_memory():
    open(MEMORY_FILE, "w", encoding="utf-8").close()

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Jarvis AI Assistant")
root.geometry("1000x650")
root.configure(bg="#0a0a0a")
root.resizable(False, False)

# Neon style for buttons
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                font=("Consolas", 14, "bold"),
                foreground="#00faff",
                background="#0a0a0a",
                borderwidth=0,
                padding=10)
style.map("TButton",
          background=[("active", "#111111")],
          foreground=[("active", "#ff9e00")])

# ------------------ Orb Animation ------------------
canvas = tk.Canvas(root, width=300, height=300, bg="#0a0a0a", highlightthickness=0)
canvas.place(relx=0.5, rely=0.4, anchor="center")
orb = canvas.create_oval(50, 50, 250, 250, outline="#00faff", width=4)

def animate_orb():
    colors = ["#00faff", "#9d4edd", "#ff9e00"]
    i = 0
    while True:
        canvas.itemconfig(orb, outline=colors[i % len(colors)])
        i += 1
        time.sleep(0.3)

threading.Thread(target=animate_orb, daemon=True).start()

# ------------------ Log Box ------------------
log_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=110, height=8,
                                    bg="#111111", fg="#00faff",
                                    font=("Consolas", 12),
                                    relief="flat", insertbackground="white")
log_box.pack(side="bottom", fill="x", padx=10, pady=10)

def log_message(msg):
    log_box.config(state="normal")
    log_box.insert(tk.END, msg + "\n")
    log_box.config(state="disabled")
    log_box.see(tk.END)

# ------------------ Command Processing ------------------
def processCommand(c):
    try:
        print("You said:", c)
        log_message("You: " + c)
        c = c.lower()

        if "google" in c:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif "youtube" in c:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif "chatgpt" in c:
            webbrowser.open("https://chat.openai.com")
            speak("Opening ChatGPT")

        elif c.startswith("play"):
            words = c.split(" ", 1)
            if len(words) > 1:
                song = words[1].strip()
                if song in musicLibrary.music:
                    link = musicLibrary.music[song]
                    speak(f"Playing {song}")
                    webbrowser.open(link)
                else:
                    speak(f"Sorry, I couldn't find the song named {song}.")
            else:
                speak("Please say the name of the song after play.")

        elif "time" in c:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")

        elif "date" in c:
            today = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {today}")

        elif "open notepad" in c:
            subprocess.Popen("notepad.exe")
            speak("Opening Notepad")

        elif "remember" in c:
            fact = c.replace("remember", "").strip()
            if fact:
                save_memory(fact)
                speak(f"Okay, I will remember: {fact}")
            else:
                speak("What do you want me to remember?")

        elif "what did i remember" in c or "recall" in c or "what do you remember" in c:
            memories = load_memory()
            if memories:
                speak("Here are the things you asked me to remember:")
                for m in memories:
                    speak(m)
            else:
                speak("You have not told me to remember anything yet.")

        elif "forget everything" in c:
            clear_memory()
            speak("Okay, I forgot everything you told me.")

        else:
            speak(f"Searching Google for {c}")
            webbrowser.open(f"https://www.google.com/search?q={c}")

    except Exception as e:
        log_message("Error: " + str(e))
        speak("Something went wrong while processing your command.")

# ------------------ Voice Input ------------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            log_message("Adjusting for noise...")
            r.adjust_for_ambient_noise(source, duration=1)
            log_message("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            command = r.recognize_google(audio)
            return command
        except sr.WaitTimeoutError:
            log_message("Listening timed out.")
        except sr.UnknownValueError:
            log_message("Could not understand the audio.")
            speak("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            log_message(f"Google API error: {e}")
            speak("Speech recognition service is down.")
        return None

# ------------------ Main Loop ------------------
def main_loop():
    speak("Initializing Jarvis")
    while True:
        command = listen()
        if command and "jarvis" in command.lower():
            speak("Yes?")
            command = listen()
            if command:
                processCommand(command)

# ------------------ Side Buttons ------------------
frame = tk.Frame(root, bg="#0a0a0a")
frame.place(relx=0.05, rely=0.5, anchor="w")

btn1 = ttk.Button(frame, text="Start Listening", command=lambda: threading.Thread(target=main_loop, daemon=True).start())
btn1.pack(pady=10, fill="x")

btn2 = ttk.Button(frame, text="Memory Recall", command=lambda: [speak(m) for m in load_memory()])
btn2.pack(pady=10, fill="x")

btn3 = ttk.Button(frame, text="Forget Memory", command=clear_memory)
btn3.pack(pady=10, fill="x")

btn4 = ttk.Button(frame, text="Quit", command=root.destroy)
btn4.pack(pady=10, fill="x")

# ------------------ Run ------------------
log_message("Jarvis System Initialized...")
root.mainloop()
