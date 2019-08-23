import picamera, sys#, io
from time import sleep
from lib import control
from tensorflow.keras.models import load_model
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
with picamera.PiCamera() as camera:
    camera.resolution = (1920,1920)
    camera.hflip = True
    camera.vflip = True
    camera.contrast = 100
    camera.brightness = 90
    #camera.start_preview()                     # no preview in RDP
    #stream = io.BytesIO()                      # Create an in-memory stream
    model = load_model('lib/CNN_model.h5')    # as Camera warm-up time 2s
    while input('ENTER to detect, else to quit...') == '':
        camera.capture('digit.jpg')            # 0.5s, png 5s
        #stream.seek(0)
        #camera.capture(stream, format='jpeg')  # 0.5s, png 5s
        #stream.seek(0)
        with Image.open('digit.jpg') as im:    # < 0.02s, no matter file or memory
            im = im.convert('L')
            im.thumbnail((28,28))
            im.save('28x28.png')
        img = mpimg.imread('28x28.png')
        img = img.reshape(1,28,28,1).astype('float32')
        img = np.ones(img.shape) - img
        prediction = model.predict_classes(img)
        print('Pi sees',prediction[0])
        for _ in range(prediction[0]):
            control.move(sys.argv[1],float(sys.argv[2]))
            sleep(0.5)
    control.GPIO.cleanup()
    #camera.stop_preview()
