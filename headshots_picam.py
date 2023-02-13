import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import os

#path = '/Users/jsha/Projects/opencv_tutorial/carolinedunn_facial_recognition/'
path = os.getcwd() 
name = 'cometdongari' #replace with your name

if not os.path.exists(path + f'dataset/{name}'):
    os.makedirs(path + f'dataset/{name}')

save_image_dir = path + f'dataset/{name}'

cam = PiCamera()
cam.resolution = (512, 304)
cam.framerate = 10
rawCapture = PiRGBArray(cam, size=(512, 304))
    
img_counter = 0

while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Press Space to take a photo", image)
        rawCapture.truncate(0)
    
        k = cv2.waitKey(1)
        rawCapture.truncate(0)
        if k%256 == 27: # ESC pressed
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = save_image_dir + "/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            img_counter += 1
            
    if k%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()
