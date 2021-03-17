# Facial Finder
Set of scripts written in Python 3 using the facial recognition API wrapper for Dlib C++ Deep Learning library

## Requirements

Since this script is using the [Face Recognition](https://github.com/ageitgey/face_recognition) API for the `Dlib` library used in Deep Learning, you're going to need `CMake` which is a family of tools for building, testing and packaging compiled software. 

* Download and install [CMake](https://cmake.org/download/) (probably already packaged in some Linux distributions)
* Download and install [Microsoft Media Feature Pack](https://www.microsoft.com/en-us/software-download/mediafeaturepack) for `Windows N` versions. This is required for `OpenCV`. *This requires a reboot!*

Finally, just a simple `pip install -r requirements.txt` should check if everything is ok.

# Features

* `Facial feature highlight` - Takes an image name and searches for it in the `dataset` folder. Then it draws the detection of eyebrows, mouth, lips and jaw.
* `Photo comparison` - Reads all the photos in `dataset` folder as it's known faces database, then takes an image filepath to check if any picture resembles the one introduced.
* `Face detection from webcam` - Reads all the photos in `dataset` folder as it's known faces database, then reviews webcam input to see if any face appearance matches the database.

<p align="center">
  <img src="screenshots/v0.0.1.png" />
</p>

## License
[MIT](https://choosealicense.com/licenses/mit/)