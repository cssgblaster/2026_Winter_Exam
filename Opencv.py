import cv2

img = cv2.imread('/home/cssgblaster/Hotpot_Exam/original.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite('gray.jpg', gray)
cv2.imwrite('binary.jpg', binary)

cv2.imshow('Original', img)
cv2.imshow('Gray', gray)
cv2.imshow('Binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

