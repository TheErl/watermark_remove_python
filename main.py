##
# import opencv library and numpy library for image processing 
import cv2,os
import numpy as np
from matplotlib import pyplot as plt
##
class Watermark():
    def __init__(self,path):
        self.folder = path
        pass

    def getPhotosFromFolder(self, path):
        # get all photos in the folder
        photos = []
        for photo in os.listdir(path):
            photos.append(photo)
        return photos

    def displayPhotos(self):
        photos = self.getPhotosFromFolder(self.folder)
        for photo in photos:
            photoPath = self.folder + '/' + photo
            cv2.imshow('photos', cv2.imread(photoPath))
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def displayPhotosWithEdge(self):
        photos = self.getPhotosFromFolder(self.folder)
        for photo in photos:
            photoPath = self.folder + '/' + photo
            img = cv2.imread(photoPath)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150, apertureSize=3)
            cv2.imshow('photos', edges)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
