#!/usr/bin/env python
from PIL import Image, ImageDraw
import face_recognition
import os

'''
    Este módulo se encarga de buscar entre los archivos dentro de la carpeta /dataset.
    Usa extensiones comunes para identificar imágenes cuyo nombre sea el que introdució
    el usuario, para después sacar la codificación y poder dibujar los valores obtenidos.

    DiracSpace
'''

img_heuristics = [
    'jpg',
    'jpeg',
    'png',
]

def CheckExistence(filepath: str) -> bool:
    return True if os.path.isfile(filepath) else False

def DrawingLandmarks(filename: str):
    try:
        # loading image to traing ai
        img = face_recognition.load_image_file(filename)
        
        # detecting facial features
        face_landmarks = face_recognition.face_landmarks(img)
        
        # creating pillow imagedraw object to display results
        pillow_image = Image.fromarray(img)
        pencil = ImageDraw.Draw(pillow_image)

        # print (face_landmarks)
        for landmark in face_landmarks:
            for feature in landmark.keys():
                pencil.line(landmark[feature], width=5)
        
        # display final result
        print (f"¡Tenemos su dibujo!")
        pillow_image.show()
    except Exception as err:
        print (f'¡Oh no! Error -> {err}')

def HighlightFacialFeatures():
    try:
        dirname = os.path.dirname('programming')
        img_name = input("¿Qué nombre tiene? -> ")
        for ext in img_heuristics:
            filename = os.path.join(dirname, f'dataset\{img_name}.{ext}')
            if CheckExistence(filename):
                print (f'¡Encontré! {filename}')
                DrawingLandmarks(filename)
    except Exception as err:
        print (f'¡Oh no! Error -> {err}')