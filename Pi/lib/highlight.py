import detect                           # detect.py module
import sys                              # get system arguments
from PIL import Image, ImageDraw        # Python Imaging Library - Pillow

def highlight(faces, path):
    with Image.open(path) as im:
        draw = ImageDraw.Draw(im)       # draw squares
        for face in faces:              # around detected faces
            box = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
            draw.line(box + [box[0]], width=5, fill='#00ff00')
        im.save(path[:-4]+'-out'+path[-4:])

if __name__ == '__main__':
    PATH = sys.argv[1]
    faces = detect.faces(PATH)
    print(len(faces), 'face(s) found!')
    highlight(faces, PATH)
    print(PATH[:-4]+'-out'+PATH[-4:], 'created!')