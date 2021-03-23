#!/usr/bin/env python

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
        from ai_modules import detect_landmarks

        detect_landmarks.HighlightFacialFeatures()
    elif selection == 1:
        from ai_modules import detect_faces

        detect_faces.ImageComparison()
    elif selection == 2:
        from ai_modules import detect_faces_webcam
        
        detect_faces_webcam.WebcamCapture()


if __name__ == '__main__':
    print (logo)
    while True:
        try:
            Main()
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()