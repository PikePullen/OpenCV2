import cv2

img = cv2.imread("../DATA/00-puppy.jpg")
# cv2.imshow('Puppy', img)
# cv2.waitKey()

"""
Alleviates kernel errors
"""
while True:
    cv2.imshow('Puppy', img)

    # IF we've waited for 1ms AND we've pressed the ESC key (27 = ESC Key)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()