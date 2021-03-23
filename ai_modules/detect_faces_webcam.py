#!/usr/bin/env python
import face_recognition, cv2

'''
    Este módulo se encarga de leer todas las imágenes debajo de dataset
    para construir una lista de codificaciones para entrenar y detectar si la
    imagen introducida por el usuario es igual o parecida a alguna de las fotos 
    que tenemos

    DiracSpace
'''

img_heuristics = [
    '.jpg',
    '.jpeg',
    '.png',
]

def GetDataset():
    try:
        import os

        # initiating local variables
        path = os.path.abspath('dataset')
        name = []
        image_encoding = []

        # we iterate the images under dataset
        # folder to repeat the process of
        # reading N images and there names for keys
        for image_name in os.listdir(path):
            # saving the image name without extension
            name.append(image_name[:image_name.index(".")])

            # loading the image and saving the encoding
            image_filepath = face_recognition.load_image_file(path + '\\' + image_name)

            # since the images have one face, get the first value
            # in returning list of encodings
            image_encoding.append(
                face_recognition.face_encodings(image_filepath)[0]
            )

        # returning list with image names (includes extension)
        # and image encodings
        return name, image_encoding
    except Exception as err:
        print(f'¡Oh no! Error obteniendo encodings -> {err}')

def WebcamCapture():
    try:
        import numpy as np

        # getting the required data
        known_face_names, known_face_encodings = GetDataset()

        face_locations = []
        face_encodings = []
        face_names = []
        _frame = True

        cv2.namedWindow("Facial Finder")
        video_capture = cv2.VideoCapture(0)

        if video_capture.isOpened():
            rval, frame = video_capture.read()
        else:
            rval = False

        while rval:
            # show window with camera
            cv2.imshow("Facial Finder", frame)

            # start capturing frame input
            rval, frame = video_capture.read()

            # resize frame for performance
            small_frame = cv2.resize(
                frame,
                (0, 0),
                fx=0.25,
                fy=0.25
            )

            # BGR Color conversion to RGB color
            frame_color_conversion = small_frame[
                :,
                :,
                ::-1
            ]

            # Iterate processing frames for time
            if _frame:
                # get all faces and encode them in the current frame
                face_locations = face_recognition.face_locations(
                    frame_color_conversion
                )
                face_encodings = face_recognition.face_encodings(
                    frame_color_conversion,
                    face_locations
                )

                # iterating the encodings of each face
                # in the frame captured and comparing
                # with the current encoding of the known
                # encodings
                face_names = []
                try:
                    for face_encoding in face_encodings:
                        matches = face_recognition.compare_faces(
                            known_face_encodings,
                            face_encoding
                        )
                        name = "Unknown"

                        face_distances = face_recognition.face_distance(
                            known_face_encodings,
                            face_encoding
                        )
                        best_match_index = np.argmin(face_distances)

                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                        face_names.append(name)
                except IndexError as ie:
                    print (f'¡Oh no! Te saliste de la lista -> {ie}')
                    exit()
            _frame = not _frame

            # displaying the results
            try:
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    # return the scale of frame to original size
                    top *= 4
                    left *= 4
                    right *= 4
                    bottom *= 4

                    # draw box aroung the face
                    cv2.rectangle(
                        frame,
                        (left, top),
                        (right, bottom),
                        (0, 0, 255),
                        2
                    )

                    # draw a label for name
                    cv2.rectangle(
                        frame,
                        (left, bottom - 35),
                        (right, bottom),
                        (0, 0, 255),
                        cv2.FILLED
                    )
                    font = cv2.FONT_HERSHEY_DUPLEX

                    # insert the text into label
                    cv2.putText(
                        frame,
                        name,
                        (left + 6, bottom - 6),
                        font,
                        1.0,
                        (255, 255, 255),
                        1
                    )
            except Exception as err_display:
                print(f'¡Oh no! Error graficando -> {err_display}')
            # add the edited frame back into the 
            # display
            cv2.imshow("Facial Finder", frame)
            
            # waiting for key pressing
            key = cv2.waitKey(20)

            # detect ESC on keyboard to leave cycle
            if key == 27:
                break
        # release and destroy all
        # instances of video capturing 
        # or else it will be occupied in next run
        video_capture.release()
        cv2.destroyWindow("Facial Finder")
        print('')
    except Exception as err:
        print(f'¡Oh no! Error -> {err}')
