import cv2
import os

#path = '/Users/jsha/Projects/opencv_tutorial/carolinedunn_facial_recognition/'
path = '/home/pi/carolinedunn_facial_recognition/'
name = 'cometdongari' #replace with your name

if not os.path.exists(path + f'dataset/{name}'):
    os.makedirs(path + f'dataset/{name}')

save_image_dir = path + f'dataset/{name}'

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = save_image_dir + "/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
