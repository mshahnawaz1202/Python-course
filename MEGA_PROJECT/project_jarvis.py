# # import speech_recognition as sr
# # import pyttsx3
# # import time
# # import datetime
# # import os
# # import subprocess
# # import webbrowser
# # import tkinter as tk
# # from tkinter import ttk
# # from tkinter import scrolledtext
# # import threading
# # import queue
# # import musicLibrary

# # # ------------------ Text to Speech (Thread-Safe) ------------------
# # engine = pyttsx3.init()
# # engine.setProperty("rate", 170)
# # voices = engine.getProperty("voices")
# # engine.setProperty("voice", voices[1].id)  # female voice

# # speech_queue = queue.Queue()

# # def speak_worker():
# #     while True:
# #         text = speech_queue.get()
# #         if text is None:  # Stop signal
# #             break
# #         print("Jarvis:", text)
# #         log_message("Jarvis: " + text)
# #         engine.say(text)
# #         engine.runAndWait()
# #         speech_queue.task_done()

# # # Start speech thread
# # threading.Thread(target=speak_worker, daemon=True).start()

# # def speak(text):
# #     """Thread-safe speak function"""
# #     speech_queue.put(text)

# # # ------------------ Memory Functions ------------------
# # MEMORY_FILE = "memory.txt"

# # def save_memory(text):
# #     now = datetime.datetime.now().strftime("%A, %B %d, %Y at %I:%M %p")
# #     entry = f"{text} (saved on {now})"
# #     with open(MEMORY_FILE, "a", encoding="utf-8") as f:
# #         f.write(entry + "\n")

# # def load_memory():
# #     if not os.path.exists(MEMORY_FILE):
# #         return []
# #     with open(MEMORY_FILE, "r", encoding="utf-8") as f:
# #         return [line.strip() for line in f.readlines()]

# # def clear_memory():
# #     open(MEMORY_FILE, "w", encoding="utf-8").close()

# # # ------------------ GUI Setup ------------------
# # root = tk.Tk()
# # root.title("Jarvis AI Assistant")
# # root.geometry("1000x650")
# # root.configure(bg="#0a0a0a")
# # root.resizable(False, False)

# # # Neon style for buttons
# # style = ttk.Style()
# # style.theme_use("clam")
# # style.configure("TButton",
# #                 font=("Consolas", 14, "bold"),
# #                 foreground="#00faff",
# #                 background="#0a0a0a",
# #                 borderwidth=0,
# #                 padding=10)
# # style.map("TButton",
# #           background=[("active", "#111111")],
# #           foreground=[("active", "#ff9e00")])

# # # ------------------ Orb Animation ------------------
# # canvas = tk.Canvas(root, width=300, height=300, bg="#0a0a0a", highlightthickness=0)
# # canvas.place(relx=0.5, rely=0.4, anchor="center")
# # orb = canvas.create_oval(50, 50, 250, 250, outline="#00faff", width=4)

# # def animate_orb():
# #     colors = ["#00faff", "#9d4edd", "#ff9e00"]
# #     i = 0
# #     while True:
# #         canvas.itemconfig(orb, outline=colors[i % len(colors)])
# #         i += 1
# #         time.sleep(0.3)

# # threading.Thread(target=animate_orb, daemon=True).start()

# # # ------------------ Log Box ------------------
# # log_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=110, height=8,
# #                                     bg="#111111", fg="#00faff",
# #                                     font=("Consolas", 12),
# #                                     relief="flat", insertbackground="white")
# # log_box.pack(side="bottom", fill="x", padx=10, pady=10)

# # def log_message(msg):
# #     log_box.config(state="normal")
# #     log_box.insert(tk.END, msg + "\n")
# #     log_box.config(state="disabled")
# #     log_box.see(tk.END)

# # # ------------------ Command Processing ------------------
# # def processCommand(c):
# #     try:
# #         print("You said:", c)
# #         log_message("You: " + c)
# #         c = c.lower()

# #         if "google" in c:
# #             webbrowser.open("https://google.com")
# #             speak("Opening Google")

# #         elif "youtube" in c:
# #             webbrowser.open("https://youtube.com")
# #             speak("Opening YouTube")

# #         elif "chatgpt" in c:
# #             webbrowser.open("https://chat.openai.com")
# #             speak("Opening ChatGPT")

# #         elif c.startswith("play"):
# #             words = c.split(" ", 1)
# #             if len(words) > 1:
# #                 song = words[1].strip()
# #                 if song in musicLibrary.music:
# #                     link = musicLibrary.music[song]
# #                     speak(f"Playing {song}")
# #                     webbrowser.open(link)
# #                 else:
# #                     speak(f"Sorry, I couldn't find the song named {song}.")
# #             else:
# #                 speak("Please say the name of the song after play.")

# #         elif "time" in c:
# #             now = datetime.datetime.now().strftime("%I:%M %p")
# #             speak(f"The current time is {now}")

# #         elif "date" in c:
# #             today = datetime.datetime.now().strftime("%A, %B %d, %Y")
# #             speak(f"Today is {today}")

# #         elif "open notepad" in c:
# #             subprocess.Popen("notepad.exe")
# #             speak("Opening Notepad")

# #         elif "remember" in c:
# #             fact = c.replace("remember", "").strip()
# #             if fact:
# #                 save_memory(fact)
# #                 speak(f"Okay, I will remember: {fact}")
# #             else:
# #                 speak("What do you want me to remember?")

# #         elif "what did i remember" in c or "recall" in c or "what do you remember" in c:
# #             recall_memory()

# #         elif "forget everything" in c:
# #             clear_memory()
# #             speak("Okay, I forgot everything you told me.")

# #         else:
# #             speak(f"Searching Google for {c}")
# #             webbrowser.open(f"https://www.google.com/search?q={c}")

# #     except Exception as e:
# #         log_message("Error: " + str(e))
# #         speak("Something went wrong while processing your command.")

# # # ------------------ Voice Input ------------------
# # def listen():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         try:
# #             log_message("Adjusting for noise...")
# #             r.adjust_for_ambient_noise(source, duration=1)
# #             log_message("Listening...")
# #             audio = r.listen(source, timeout=5, phrase_time_limit=5)
# #             command = r.recognize_google(audio)
# #             return command
# #         except sr.WaitTimeoutError:
# #             log_message("Listening timed out.")
# #         except sr.UnknownValueError:
# #             log_message("Could not understand the audio.")
# #             speak("Sorry, I didn't catch that.")
# #         except sr.RequestError as e:
# #             log_message(f"Google API error: {e}")
# #             speak("Speech recognition service is down.")
# #         return None

# # # ------------------ Main Loop ------------------
# # def main_loop():
# #     speak("Initializing Jarvis")
# #     while True:
# #         command = listen()
# #         if command and "jarvis" in command.lower():
# #             speak("Yes?")
# #             command = listen()
# #             if command:
# #                 processCommand(command)

# # # ------------------ Memory Recall Function ------------------
# # def recall_memory():
# #     memories = load_memory()
# #     if memories:
# #         speak("Here are the things you asked me to remember:")
# #         for m in memories:
# #             speak(m)
# #     else:
# #         speak("You have not told me to remember anything yet.")

# # # ------------------ Side Buttons ------------------
# # frame = tk.Frame(root, bg="#0a0a0a")
# # frame.place(relx=0.05, rely=0.5, anchor="w")

# # btn1 = ttk.Button(frame, text="Start Listening", command=lambda: threading.Thread(target=main_loop, daemon=True).start())
# # btn1.pack(pady=10, fill="x")

# # btn2 = ttk.Button(frame, text="Memory Recall", command=recall_memory)
# # btn2.pack(pady=10, fill="x")

# # btn3 = ttk.Button(frame, text="Forget Memory", command=clear_memory)
# # btn3.pack(pady=10, fill="x")

# # btn4 = ttk.Button(frame, text="Quit", command=root.destroy)
# # btn4.pack(pady=10, fill="x")

# # # ------------------ Run ------------------
# # log_message("Jarvis System Initialized...")
# # root.mainloop()


# import tkinter as tk
# import time
# import threading
# import psutil
# import datetime

# root = tk.Tk()
# root.title("J.A.R.V.I.S. HUD")
# root.geometry("1200x700")
# root.configure(bg="black")
# root.resizable(False, False)

# # ---------------- Arc Reactor ----------------
# canvas = tk.Canvas(root, width=400, height=400, bg="black", highlightthickness=0)
# canvas.place(relx=0.5, rely=0.45, anchor="center")

# reactor = canvas.create_oval(50, 50, 350, 350, outline="#00faff", width=3)
# inner = canvas.create_oval(150, 150, 250, 250, outline="#9d4edd", width=2)

# def animate_reactor():
#     colors = ["#00faff", "#9d4edd", "#ff9e00", "#00ff88"]
#     i = 0
#     while True:
#         canvas.itemconfig(reactor, outline=colors[i % len(colors)])
#         canvas.itemconfig(inner, outline=colors[(i+2) % len(colors)])
#         i += 1
#         time.sleep(0.2)

# threading.Thread(target=animate_reactor, daemon=True).start()

# # ---------------- System Info Panels ----------------
# panel_left = tk.LabelFrame(root, text="SYSTEM STATUS", fg="#00faff", bg="black",
#                            font=("Consolas", 12, "bold"), width=250, height=300)
# panel_left.place(x=50, y=100)

# label_cpu = tk.Label(panel_left, text="CPU: --%", fg="#00faff", bg="black", font=("Consolas", 12))
# label_cpu.pack(pady=10)

# label_ram = tk.Label(panel_left, text="RAM: --%", fg="#00faff", bg="black", font=("Consolas", 12))
# label_ram.pack(pady=10)

# label_time = tk.Label(panel_left, text="Time: --:--", fg="#ff9e00", bg="black", font=("Consolas", 12))
# label_time.pack(pady=10)

# def update_system():
#     while True:
#         cpu = psutil.cpu_percent()
#         ram = psutil.virtual_memory().percent
#         now = datetime.datetime.now().strftime("%I:%M:%S %p")
#         label_cpu.config(text=f"CPU: {cpu}%")
#         label_ram.config(text=f"RAM: {ram}%")
#         label_time.config(text=f"Time: {now}")
#         time.sleep(1)

# threading.Thread(target=update_system, daemon=True).start()

# # ---------------- Status Log ----------------
# log_box = tk.Text(root, width=100, height=6, bg="black", fg="#00faff",
#                   font=("Consolas", 12), relief="flat", insertbackground="white")
# log_box.pack(side="bottom", fill="x", padx=10, pady=10)

# def log_message(msg):
#     log_box.insert(tk.END, msg + "\n")
#     log_box.see(tk.END)

# log_message("J.A.R.V.I.S. HUD Initialized...")

# root.mainloop()

#===========================================================================================
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
import queue
import psutil
import musicLibrary

# ------------------ Text to Speech (Thread-Safe) ------------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # female voice

speech_queue = queue.Queue()

def speak_worker():
    while True:
        text = speech_queue.get()
        if text is None:
            break
        print("Jarvis:", text)
        log_message("Jarvis: " + text)
        engine.say(text)
        engine.runAndWait()
        speech_queue.task_done()

threading.Thread(target=speak_worker, daemon=True).start()

def speak(text):
    speech_queue.put(text)

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

def recall_memory():
    memories = load_memory()
    if memories:
        speak("Here are the things you asked me to remember:")
        for m in memories:
            speak(m)
    else:
        speak("You have not told me to remember anything yet.")

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("J.A.R.V.I.S. HUD Assistant")
root.geometry("1200x700")
root.configure(bg="black")
root.resizable(False, False)

# ---------------- Arc Reactor ----------------
canvas = tk.Canvas(root, width=400, height=400, bg="black", highlightthickness=0)
canvas.place(relx=0.5, rely=0.45, anchor="center")

reactor = canvas.create_oval(50, 50, 350, 350, outline="#00faff", width=3)
inner = canvas.create_oval(150, 150, 250, 250, outline="#9d4edd", width=2)

def animate_reactor():
    colors = ["#00faff", "#9d4edd", "#ff9e00", "#00ff88"]
    i = 0
    while True:
        canvas.itemconfig(reactor, outline=colors[i % len(colors)])
        canvas.itemconfig(inner, outline=colors[(i+2) % len(colors)])
        i += 1
        time.sleep(0.2)

threading.Thread(target=animate_reactor, daemon=True).start()

# ---------------- System Info Panels ----------------
panel_left = tk.LabelFrame(root, text="SYSTEM STATUS", fg="#00faff", bg="black",
                           font=("Consolas", 12, "bold"), width=250, height=300)
panel_left.place(x=50, y=100)

label_cpu = tk.Label(panel_left, text="CPU: --%", fg="#00faff", bg="black", font=("Consolas", 12))
label_cpu.pack(pady=10)

label_ram = tk.Label(panel_left, text="RAM: --%", fg="#00faff", bg="black", font=("Consolas", 12))
label_ram.pack(pady=10)

label_time = tk.Label(panel_left, text="Time: --:--", fg="#ff9e00", bg="black", font=("Consolas", 12))
label_time.pack(pady=10)

def update_system():
    while True:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        now = datetime.datetime.now().strftime("%I:%M:%S %p")
        label_cpu.config(text=f"CPU: {cpu}%")
        label_ram.config(text=f"RAM: {ram}%")
        label_time.config(text=f"Time: {now}")
        time.sleep(1)

threading.Thread(target=update_system, daemon=True).start()

# ---------------- Status Log ----------------
log_box = tk.Text(root, width=100, height=6, bg="black", fg="#00faff",
                  font=("Consolas", 12), relief="flat", insertbackground="white")
log_box.pack(side="bottom", fill="x", padx=10, pady=10)

def log_message(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)

# ------------------ Command Processing ------------------
def processCommand(c):
    try:
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
            recall_memory()

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
frame = tk.Frame(root, bg="black")
frame.place(relx=0.05, rely=0.5, anchor="w")

btn1 = ttk.Button(frame, text="Start Listening", command=lambda: threading.Thread(target=main_loop, daemon=True).start())
btn1.pack(pady=10, fill="x")

btn2 = ttk.Button(frame, text="Memory Recall", command=recall_memory)
btn2.pack(pady=10, fill="x")

btn3 = ttk.Button(frame, text="Forget Memory", command=clear_memory)
btn3.pack(pady=10, fill="x")

btn4 = ttk.Button(frame, text="Quit", command=root.destroy)
btn4.pack(pady=10, fill="x")

# ------------------ Run ------------------
log_message("J.A.R.V.I.S. HUD + Assistant Initialized...")
speak("JARVIS online. All systems running normally.")
root.mainloop()
