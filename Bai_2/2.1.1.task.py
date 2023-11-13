import cv2
import numpy as np

# Đọc hình ảnh từ tệp "dog.jpg"
img = cv2.imread("dog.jpg")

# Biến toàn cục để lưu tọa độ của các hình tròn được vẽ
circles = []

def draw_circle(event, x, y, flags, param):
    global circles

    # Sự kiện chuột phải
    if event == cv2.EVENT_RBUTTONDOWN:
        circles.append((x, y))

    # Vẽ tất cả các hình tròn đã được lưu
    for center in circles:
        cv2.circle(img, center, 20, (0, 0, 255), -1)

    cv2.imshow('Image', img)

cv2.imshow('Image', img)
cv2.setMouseCallback('Image', draw_circle)

while True:
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # Bấm phím Escape (ESC) để thoát
        break

cv2.destroyAllWindows()
