from PIL import Image
import cv2
import time
import binascii
import base64
import numpy as np

def display_base64(img, interval=5):
    img = base64.b64decode(img)
    img = np.frombuffer(img,dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    cv2.imshow('image',img)
    cv2.waitKey(interval*1000)

def display_PIL(imgpath, interval=5):
    im = Image.open(imgpath)
    im.show()
    time.sleep(interval)
    
def display_cv2(imgpath, interval=5):
    im = cv2.imread(imgpath)
    cv2.imshow('image',im)
    cv2.waitKey(interval)
    # time.sleep(interval)
    # cv2.destroyAllWindows('image')
    # cv2.waitKey(1)


if __name__ == '__main__':
    display = display_base64
    start = time.time()
    path = 'data/images/lena.jpeg'
    data = cv2.imread(path)
    ret, data = cv2.imencode(".jpeg", data)
    # data = binascii.b2a_base64(data).decode('utf-8')
    # with open(path, 'rb') as f:
    #     data = f.read()
    data = base64.b64encode(data)
    # print(data)
    display(data, 3)
    print(time.time()-start)