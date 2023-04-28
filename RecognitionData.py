import cv2

class Recognition:

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.XML')
        self.recognizer = cv2.face_LBPHFaceRecognizer.create()
        self.recognizer.read('recognizer/trainningData.yml')
        self.fontFace = cv2.FONT_HERSHEY_SIMPLEX

    def recognition(self, uid, name, studentCode, className, age):
        self.cap = cv2.VideoCapture(0)
        while (True):
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.face_cascade.detectMultiScale(gray)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                id, confidence = self.recognizer.predict(roi_gray)
                print(id, confidence)
                if confidence < 65 and id == uid:
                    cv2.putText(frame, str(id), (x, y - 5), self.fontFace, 1, (0, 255, 0), 2)
                    cv2.putText(frame, str(name), (x, y - 30), self.fontFace, 1, (0, 255, 0), 2)
                    cv2.putText(frame, str(studentCode), (x, y - 55), self.fontFace, 1, (0, 255, 0), 2)
                    cv2.putText(frame, str(className), (x, y - 80), self.fontFace, 1, (0, 255, 0), 2)
                    cv2.putText(frame, str(age), (x, y - 105), self.fontFace, 1, (0, 255, 0), 2)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 2)

            cv2.imshow('image', frame)
            if (cv2.waitKey(1) == ord('q')):
                break
        self.cap.release()
        cv2.destroyAllWindows()



