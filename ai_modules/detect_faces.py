#!/usr/bin/env python
import face_recognition

'''
    Este módulo se encarga de leer todas las imágenes debajo de dataset
    para construir una lista de codificaciones para entrenar y detectar si la
    imagen introducida por el usuario es igual o parecida a alguna de las fotos 
    que tenemos

    DiracSpace
'''

def GetDataset() -> dict:
    try:
        import os

        path = os.path.abspath('dataset')
        name = []
        image_encoding = []
        for image in os.listdir(path):
            name.append(image)
            image = face_recognition.load_image_file(path + '\\' + image)
            image_encoding.append(
                face_recognition.face_encodings(image)[0]
            )
        return dict(
            zip(name, image_encoding)
        )
    except Exception as err:
        print (f'¡Oh no! Error -> {err}')

def GetComparisonEncoding(path: str) -> list:
    try:
        import face_recognition

        return face_recognition.face_encodings(
            face_recognition.load_image_file(path)
        )
    except Exception as err:
        print (f'¡Oh no! Error -> {err}')

def ImageComparison():
    try:
        from glob import glob

        # get the name and encoding for every image in dataset
        resultset = GetDataset()

        # now read the image to compare with dataset
        print ("Ingresa una imagen tuya para comparar con nuestro dataset")
        img = input('Dame la ruta de tu imagen -> ')

        # encoding the image in separate list
        # because we need to iterate and individually 
        # compare the encodings of all images in dataset
        comparison_encoding = GetComparisonEncoding(img)

        # iterate the dictionary to get name and encoding values
        # then compare the ones in dataset with unknown image
        for index, key in enumerate(resultset):
            try:
                print (f'{index} - Comparando a {key}')

                # getting array of boolean values because the ai
                # compares the individual encodings and returns true
                # or false for each one
                results = face_recognition.compare_faces(
                    resultset[key], 
                    comparison_encoding, 
                    tolerance=0.6
                )

                # for some reason an IndexOutOfBounds Exception
                # pops up, so it detects when a positive match
                # shows and gracefully exits without breaking. Hopefully
                if results[index]:
                    # displays the only result important to us
                    # which is the positive case
                    print (results[index])
                    print ('')
                    break
            except IndexError:
                print (f'¡Oh no! Te saliste de la lista')
                exit()
    except Exception as err:
        print (f'¡Oh no! Error -> {err}')