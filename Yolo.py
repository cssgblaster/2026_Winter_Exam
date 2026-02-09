import cv2
from ultralytics import YOLO

model = YOLO('yolo11n.pt')

results = model('/home/cssgblaster/Hotpot_Exam/小猫.jpg')

results[0].save('result.jpg')

result_cv2 = cv2.imread('result.jpg')
cv2.imshow('Detection Result', result_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()


