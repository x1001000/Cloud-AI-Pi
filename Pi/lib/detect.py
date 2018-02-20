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

if __name__ == '__main__':
    PATH = 'photo/1.jpg'                   # set relative PATH of photo file
    print(len(faces(PATH)), 'face(s) found!')