from PIL import Image
import matplotlib.pyplot as plt
import cv2
import time


if __name__ == "__main__":
    path = 'data/images/lena.jpeg'
    image = cv2.imread(path)
    cv2.imshow('i', image)
    time.sleep(4)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # plt.imshow()
    # plt.show()
    # 
    # plt.imshow(image)
    