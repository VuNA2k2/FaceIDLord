import cv2
import numpy as np
import os
from PIL import Image

class TrainData:
    def __init__(self):
        self.recognizer = cv2.face_LBPHFaceRecognizer.create()
        self.path = 'dataSet'

    def train(self):
        faces, Ids = self._getImageWithId()

        self.recognizer.train(faces, np.array(Ids))

        if not os.path.exists('recognizer'):
            os.makedirs('recognizer')

        self.recognizer.save('recognizer/trainningData.yml')

        cv2.destroyAllWindows()

    def _getImageWithId(self):
        imagePaths = [os.path.join(self.path, f) for f in os.listdir(self.path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')

            faceNp = np.array(faceImg, 'uint8')
            print(faceNp)

            Id = int(imagePath.split('.')[1])

            faces.append(faceNp)
            IDs.append(Id)

            cv2.imshow('trainning', faceNp)
            cv2.waitKey(10)

        return faces, IDs

TrainData().train()