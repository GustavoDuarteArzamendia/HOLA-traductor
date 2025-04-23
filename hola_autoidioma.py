
import speech_recognition as sr
from gtts import gTTS
from deep_translator import GoogleTranslator
from langdetect import detect
import pygame
import os
import time

pygame.init()
r = sr.Recognizer()

def detectar_y_traducir(destino="en"):
    with sr.Microphone() as source:
        print("Decí algo en cualquier idioma...")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio)
        print("Texto detectado:", texto)

        idioma_origen = detect(texto)
        print("Idioma detectado:", idioma_origen)

        traduccion = GoogleTranslator(source=idioma_origen, target=destino).translate(texto)
        print("Traducción:", traduccion)

        tts = gTTS(text=traduccion, lang=destino)
        archivo = "voz.mp3"
        tts.save(archivo)

        pygame.mixer.init()
        pygame.mixer.music.load(archivo)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        # Cerramos el mixer para liberar el archivo de audio
        pygame.mixer.quit()

        # Ahora sí se puede borrar
        os.remove(archivo)

    except sr.UnknownValueError:
        print("No se entendió lo que dijiste.")
    except sr.RequestError as e:
        print("Error con el servicio:", e)

detectar_y_traducir("en")