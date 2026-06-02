import speech_recognition as sr
import os

def procesar_comando(texto):
    texto = texto.lower()
    
    if "reproductor" in texto and "video" in texto:
        os.system("start ms-windows-video")
    elif "word" in texto:
        os.system("start winword")
    elif "calculadora" in texto:
        os.system("start calc")
    elif "apagar" in texto:
        os.system("shutdown /s /t 5")

# Seleccionar archivo
from tkinter import Tk, filedialog
root = Tk()
root.withdraw()
ruta = filedialog.askopenfilename(title="Selecciona audio", filetypes=[("Audio", "*.wav *.mp3")])

if ruta:
    recognizer = sr.Recognizer()
    with sr.AudioFile(ruta) as source:
        audio = recognizer.record(source)
        texto = recognizer.recognize_google(audio, language="es-ES")
        print(f"Dijiste: {texto}")
        procesar_comando(texto)