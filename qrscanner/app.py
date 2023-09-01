import cv2
from pyzbar.pyzbar import decode
import time




cap = cv2.VideoCapture(0)  # 0 indicates the default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break

    decoded_objects = decode(frame)
    for obj in decoded_objects:
        barcode_data = obj.data.decode('utf-8')
        print("QR Code Data:", barcode_data)
        points = obj.polygon

        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            cv2.polylines(frame, [hull], True, (0, 255, 0), 2)

    cv2.imshow("QR Code Scanner", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



# cap = cv2.VideoCapture(0)  # 0 indicates the default camera
# cap.set(5, 640)
# cap.set(6, 480)

# camera = True
# while camera == True:
#     success, frame = cap.read()
#     for item in decode(frame):
#         print(item.type)
#         print(item.data.decode('utf-8'))
#         time.sleep(6)

#         cv2.imshow("Our QR Code Scanner", frame)
#         cv2.waitkey(3)

