import picamera
from lib import detect, highlight, control
with picamera.PiCamera() as camera:
    camera.resolution = (1920,1920)
    camera.hflip = True
    camera.vflip = True
    camera.contrast = 0
    camera.brightness = 50
    while input('ENTER to detect, else to quit...') == '':
        camera.capture('faces.jpg')
        faces = detect.faces('faces.jpg')
        print(len(faces), 'face(s) found!')
        highlight.highlight(faces, 'faces.jpg')
        print('faces_highlight.jpg created!')
        for _ in range(len(faces)):
            control.move('k',2)