import cv2

# Load pre-trained model (HOG + SVM)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect_people(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    boxes, _ = hog.detectMultiScale(frame, winStride=(8,8))

    count = len(boxes)

    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    return frame, count