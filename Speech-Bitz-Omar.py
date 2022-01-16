from enum import Flag
from gtts import gTTS
import os

file = open("PVR1.txt", "r").read() #Aquí teneis que poner la ruta de vuestro file o el archivo./ Antes de esto teneis que crear un archivo .txt con lo que querais que diga el hablador(speecher)

speech = gTTS(text=file, lang='es', slow=True) #Podreis cambiar el lenguaje en mi caso pondre "es" que es mi lenguaje natal,tmbn podreis elegir la velocidad del speech(Hablador) en mi caso pondre True en slow porque se entiende mas.
speech.save("voice.mp3") #Aquí teneis que guardar el nombre del archivo que quereis que se guarde en la carpeta que tengais 
os.system("voice.mp3") #Aquí teneis que guardar el nombre del archivo que quereis que se guarde en la carpeta que tengais



