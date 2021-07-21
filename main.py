import cv2
import numpy as np

if __name__ == "__main__":
    img = cv2.imread("images.jpg")
    height, width, dim = img.shape
    # print(img.shape)
    # transformation matrix for translation
    xtrasform = int(width*0.25)
    ytrasform = int(height*0.25)
    M = np.float32([[1, 0, xtrasform],
                    [0, 1, 0],
                    [0, 0, 1]])
    # # apply a perspective transformation to the image
    translated_img = cv2.warpPerspective(img, M, (width, height))
    cv2.imwrite("transform_x.jpg", translated_img)

    M = np.float32([[1, 0, 0],
                    [0, 1, ytrasform],
                    [0, 0, 1]])
    # # apply a perspective transformation to the image
    translated_img = cv2.warpPerspective(img, M, (width, height))
    cv2.imwrite("transform_y.jpg", translated_img)

    angle = np.radians(90)
    M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]])
    translated_img = cv2.warpPerspective(img, M, (width, height))
    cv2.imwrite("roate_z+90.jpg", translated_img)

    angle = np.radians(-90)
    M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]])
    translated_img = cv2.warpPerspective(img, M, (width, height))
    cv2.imwrite("roate_z-90.jpg", translated_img)

    cx = int(width/2)
    cy = int(height/2)
    img[cy, cx, ] = (img[cy, cx, ])*(1.5)
    for i in range(1, 50):
        img[cy - i:cy + i + 1, cx - i, ] = img[cy - i:cy + i + 1, cx - i, ] * ((150 - i) / 100)
        img[cy - i:cy + i + 1, cx + i, ] = img[cy - i:cy + i + 1, cx + i, ] * ((150 - i) / 100)
        img[cy - i, cx - i + 1:cx + i, ] = img[cy - i, cx - i + 1:cx + i, ] * ((150 - i) / 100)
        img[cy + i, cx - i + 1:cx + i, ] = img[cy + i, cx - i + 1:cx + i, ] * ((150 - i) / 100)

    cv2.imwrite("rgb_increase.jpg", img)