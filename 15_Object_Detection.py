# ****************************** For Image ******************************

from ultralytics import YOLOWorld
import cv2

# Read image
img = cv2.imread('detect.png')
img = cv2.resize(img, (700, 700))

# Load YOLO-World
model = YOLOWorld('yolov8s-world.pt')

# Tell the model what objects to look for
classes = [
    'person','car','bicycle',
    'bus','truck', 'sea','school',
    'university','building','shop','garden',
    'bridge','boat','motorcycle','sports ground']

# Set the objects we want to detect
model.set_classes(classes)

# Detect objects in the image
results = model(img)

# Go through all detections
for result in results:
    # Go through each detected object
    for box in result.boxes:
        # Get box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        confidence = float(box.conf[0])
        # Get class number
        class_id = int(box.cls[0])
        # Get class number
        name = classes[class_id]

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f'{name} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

cv2.imshow('Object Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()






# ****************************** For Live Streaming ******************************

# from ultralytics import YOLO
# import cv2
# import cvzone
#
# cap = cv2.VideoCapture(0)
# model = YOLO('yolo26s.pt')
#
# while True:
#     success, img = cap.read()
#     img = cv2.flip(img, 1)
#     result = model(img, stream=True)
#
#     for r in result:
#         for box in r.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             w, h = x2 - x1, y2 - y1
#
#             conf = int(box.conf[0] * 100)
#             cls = int(box.cls[0])
#             names = model.names[cls]
#
#             cvzone.cornerRect(img, (x1, y1, w, h))
#             cvzone.putTextRect(img, f'{names}, {conf}', (x1, y1 - 10), scale=1)
#
#     cv2.imshow('Object Detection', img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()