from keras.models import load_model
model = load_model('CNN_model.h5')

from PIL import Image
size =(28, 28)
for i in range(10):                             # 10張jpg放NxN資料夾
    with Image.open('NxN/m%d.jpg'%i) as im:     # with open as 的寫法比較好，結束就會close()
        im = im.convert('L')                    # 轉灰階
        im.thumbnail(size)                      # 做縮圖
        im.save('28x28/m%d.png'%i)              # 存成png放28x28資料夾

import matplotlib.image as mpimg

import numpy as np
for i in range(10):
    img = mpimg.imread('28x28/m%d.png'%i)
    img = img.reshape(1,28,28,1).astype('float32')
    img = np.ones(img.shape) - img              # MNIST的黑白是255～0，RGB的黑白是0～1
    prediction = model.predict_classes(img)
    print('Handwritten',i,'is predicted as',prediction[0])