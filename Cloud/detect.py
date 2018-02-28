import sys                                  # get system arguments
from google.cloud import vision             # Google Cloud Vision API client library
from google.cloud.vision import types

def faces(path):
    client = vision.ImageAnnotatorClient()  # instantiate a client for Vison API service
    with open(path, 'rb') as f:             # open/close a file
        content = f.read()                  # read file into memory
    image = types.Image(content=content)
    response = client.face_detection(image=image)   # POST request JSON
    faces = response.face_annotations           # convert response JSON into Python object
    return faces

def happy(face):
    return True if face.joy_likelihood >= 3 else False  # 5 very likely, 3 possible

if __name__ == '__main__':
    PATH = sys.argv[1]
    Faces = faces(PATH)
    print(len(Faces), 'face(s) found!')
    count = 0
    for face in Faces:
        if not happy(face):
            count += 1
    print(count, 'seem(s) NOT happy...')