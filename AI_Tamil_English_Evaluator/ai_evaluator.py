import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import socket

api_connected = False
api_provider = None
translator = None
mode = "Offline Mode (Dictionary)"

def internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        return False

try:
    from openai import OpenAI
    openai_available = True
except ImportError:
    openai_available = False

try:
    import google.generativeai as genai
    gemini_available = True
except ImportError:
    gemini_available = False

try:
    from googletrans import Translator as GoogleTranslator
    googletrans_available = True
except ImportError:
    googletrans_available = False

local_dict_en_ta = {
    "hello": "வணக்கம்",
    "how are you": "நீங்கள் எப்படி இருக்கிறீர்கள்",
    "computer": "கணினி",
    "love": "அன்பு",
    "lust": "காமம்",
    "artificial intelligence": "செயற்கை நுண்ணறிவு",
    "thank you": "நன்றி"
}
local_dict_ta_en = {v: k for k, v in local_dict_en_ta.items()}

def connect_api():
    global api_connected, api_provider, translator, mode
    if openai_available or gemini_available:
        choice = simpledialog.askstring("API Selection", "Enter 1 for OpenAI, 2 for Gemini, or 3 for Google Translate")
        if choice == "1" and openai_available:
            key = simpledialog.askstring("OpenAI Key", "Enter your OpenAI API key")
            translator = OpenAI(api_key=key)
            api_provider = "OpenAI"
            api_connected = True
            mode = "Connected to OpenAI"
        elif choice == "2" and gemini_available:
            key = simpledialog.askstring("Gemini Key", "Enter your Gemini API key")
            genai.configure(api_key=key)
            translator = genai.GenerativeModel("gemini-1.5-flash")
            api_provider = "Gemini"
            api_connected = True
            mode = "Connected to Gemini"
        elif choice == "3" and googletrans_available and internet_available():
            translator = GoogleTranslator()
            api_provider = "Google Translate"
            api_connected = True
            mode = "Connected to Google Translate"
        else:
            mode = "Offline Mode (Dictionary)"
    elif googletrans_available and internet_available():
        translator = GoogleTranslator()
        api_provider = "Google Translate"
        api_connected = True
        mode = "Connected to Google Translate"
    else:
        mode = "Offline Mode (Dictionary)"
    api_status.config(text=mode)

def translate_text():
    text = input_box.get("1.0", tk.END).strip()
    direction = lang_choice.get()
    if not text:
        messagebox.showwarning("Empty", "Please enter text to translate.")
        return

    if api_connected:
        try:
            if api_provider == "OpenAI":
                res = translator.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"Translate this {direction}: {text}"}]
                )
                translated = res.choices[0].message.content.strip()
            elif api_provider == "Gemini":
                res = translator.generate_content(f"Translate this {direction}: {text}")
                translated = res.text.strip()
            elif api_provider == "Google Translate":
                if direction == "English → Tamil":
                    translated = translator.translate(text, src='en', dest='ta').text
                else:
                    translated = translator.translate(text, src='ta', dest='en').text
            else:
                translated = local_translate(text, direction)
        except Exception:
            translated = local_translate(text, direction)
    else:
        translated = local_translate(text, direction)

    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, translated)
    output_box.config(state=tk.DISABLED)

def local_translate(text, direction):
    text_lower = text.lower()
    if direction == "English → Tamil":
        return local_dict_en_ta.get(text_lower, "No offline translation found.")
    else:
        return local_dict_ta_en.get(text, "No offline translation found.")

root = tk.Tk()
root.title("AI Tamil ↔ English Translator")
root.geometry("500x420")
root.resizable(False, False)

ttk.Label(root, text="Select Translation Direction:").pack(pady=5)
lang_choice = ttk.Combobox(root, values=["English → Tamil", "Tamil → English"], state="readonly")
lang_choice.current(0)
lang_choice.pack(pady=5)

ttk.Label(root, text="Enter Text:").pack(pady=5)
input_box = tk.Text(root, height=5, width=50)
input_box.pack(pady=5)

ttk.Button(root, text="Translate", command=translate_text).pack(pady=10)

ttk.Label(root, text="Translation:").pack(pady=5)
output_box = tk.Text(root, height=5, width=50, state=tk.DISABLED)
output_box.pack(pady=5)

api_status = ttk.Label(root, text="Detecting mode...")
api_status.pack(pady=5)

connect_api()

root.mainloop()