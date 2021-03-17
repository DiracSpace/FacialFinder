#!/usr/bin/env python
from ai_modules import detect_landmarks
from ai_modules import detect_faces
from ai_modules import detect_faces_webcam

creator = 'DiracSpace'
logo = f'''
   ,d8888b                   d8,           d8b        ,d8888b  d8,                d8b                 
   88P'                     `8P            88P        88P'    `8P                 88P                 
d888888P                                  d88      d888888P                      d88                  
  ?88'     d888b8b   d8888b  88b d888b8b  888        ?88'      88b  88bd88b  d888888   d8888b  88bd88b
  88P     d8P' ?88  d8P' `P  88Pd8P' ?88  ?88        88P       88P  88P' ?8bd8P' ?88  d8b_,dP  88P'  `
 d88      88b  ,88b 88b     d88 88b  ,88b  88b      d88       d88  d88   88P88b  ,88b 88b     d88     
d88'      `?88P'`88b`?888P'd88' `?88P'`88b  88b    d88'      d88' d88'   88b`?88P'`88b`?888P'd88'           
                                                                        By {creator}
'''

# C:\Users\jsonr\Documents\Programming\jayson.jpg

options = [
    'Dibujar rasgos faciales en fotos',
    'Comparar tu foto con nuestro registro',
    'Detectar rostro con cámara'
]

def ShowOptions():
    for index, option in enumerate(options):
        print (f'{index} - {option}')

def Main():
    ShowOptions()
    print ('\n')
    selection = int(input("¿Qué desea hacer? -> "))
    
    if selection == 0:
        detect_landmarks.HighlightFacialFeatures()
    elif selection == 1:
        detect_faces.ImageComparison()
    elif selection == 2:
        detect_faces_webcam.WebcamCapture()


if __name__ == '__main__':
    print (logo)
    while True:
        try:
            Main()
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()