import picamera, sys
from time import sleep
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
        #print('faces-out.jpg created!')
        happy_faces = 0
        for face in faces:
            if detect.happy(face) == True:
                happy_faces += 1
        if happy_faces:
            print(f'There are {happy_faces} happy face(s)!')
            for _ in range(happy_faces):
                control.move(sys.argv[1],float(sys.argv[2]))
                sleep(0.5)
        else:
            print('No one is happy here...')
            for _ in range(3):
                    control.move('j',0.2)
                    control.move('k',0.2)
    control.GPIO.cleanup()
