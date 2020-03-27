from PIL import Image
from django.shortcuts import render
from match.models import UserInfo
import cv2
import matplotlib.pyplot as plt
import numpy as np


def top(request):
    return render(request, 'myhp/main.html', {})


def index(request):
    images = UserInfo.objects.all()
    return render(request, 'myhp/index.html', {'images': images})

def show(request):
    aaa = 3
    images = UserInfo.objects.get(pk=aaa)
    return render(request, 'myhp/show.html', {'images': images})

# def mosaic(request):
    # src = cv2.imread('./media/photos/20/03/24/download.jpg')
    # small = cv2.resize(src, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
    # img = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    # cv2.imwrite('./media/photos/opencv_mosaic_01.jpg', img)
    # return render(request, 'myhp/create.html', {})

# def test(request):
# class MosaicForm():

def create(request):
    return render(request, 'myhp/create.html', {})

src = cv2.imread('./media/photos/20/03/24/images.jpg')
 
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

dst_01 = mosaic(src)
# cv2.imwrite('./media/photos/opencv_mosaic_01.jpg', dst_01)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

dst_area = mosaic_area(src, 100, 50, 100, 150)
# cv2.imwrite('./media/photos/opencv_mosaic_area.jpg', dst_area)

face_cascade_path = './haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

for x, y, w, h in faces:
    dst_face = mosaic_area(src, x, y, w, h)

cv2.imwrite('./media/photos/opencv_mosaic_face.jpg', dst_face)