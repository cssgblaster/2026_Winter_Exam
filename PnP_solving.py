import cv2
import numpy as np

object_points = np.array([
    [-67.5, 28.0, 0],   
    [67.5, 28.0, 0],    
    [67.5, -28.0, 0],   
    [-67.5, -28.0, 0]   
], dtype=np.float32)

image_points = np.array([
    [100, 100],  
    [300, 80],    
    [320, 200],   
    [120, 220]    
], dtype=np.float32)

camera_matrix = np.array([
    [500, 0, 320],
    [0, 500, 240],
    [0, 0, 1]
], dtype=np.float32)

dist_coeffs = np.zeros((5, 1), dtype=np.float32)

success, rvec, tvec = cv2.solvePnP(object_points, image_points, camera_matrix, dist_coeffs)

print("平移向量:")
print(np.round(tvec.flatten(), 1))
print("旋转向量:")
print(np.round(rvec.flatten(), 1))


