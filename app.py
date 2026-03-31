import cv2
from detector import detect_people

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame, count = detect_people(frame)

    # Crowd classification
    if count < 3:
        status = "LOW"
        color = (0, 255, 0)
    elif count < 7:
        status = "MEDIUM"
        color = (0, 255, 255)
    else:
        status = "HIGH ALERT!"
        color = (0, 0, 255)

    cv2.putText(frame, f"People: {count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.putText(frame, f"Density: {status}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Crowd Monitor", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()