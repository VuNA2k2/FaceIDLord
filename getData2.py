import cv2
import os

class GetData:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.XML')

    def getDataForStudentCode(self, studentCode):
        self.cap = cv2.VideoCapture(0)
        id = int(studentCode)
        sampleNum = 0
        while (True):
            ret, frame = self.cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                print(sampleNum)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 2)
                if not os.path.exists('dataSet'):
                    os.makedirs('dataSet')
                sampleNum += 1
                cv2.imwrite('dataSet/User.' + str(id) + '.' + str(sampleNum) + '.jpg', gray[y: y + h, x: x + w])
            cv2.imshow('frame', frame)
            cv2.waitKey(1)
            if sampleNum > 500:
                break
        self.cap.release()
        cv2.destroyAllWindows()
