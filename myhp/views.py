from PIL import Image
from django.shortcuts import render
from match.models import UserInfo
import cv2
# from django.views import View

def top(request):
    return render(request, 'myhp/main.html', {})

def index(request):
    images = UserInfo.objects.all()
    return render(request, 'myhp/index.html', {'images': images})

def show(request,id):
    images = UserInfo.objects.get(pk=id)
    return render(request, 'myhp/show.html', {'images': images})

def create(request):
    return render(request, 'myhp/create.html', {})

def message(request):
    return render(request, 'myhp/message.html', {})

# class MosaicProcess(View):
#     template_name = "myhp/create.html"
    
    src = cv2.imread('./media/photos/20/03/27/image9.jpg')
     
    def mosaic(src, ratio=0.1):
        small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    
    dst_01 = mosaic(src)
    
    def mosaic_area(src, x, y, width, height, ratio=0.1):
        dst = src.copy()
        dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
        return dst
    
    dst_area = mosaic_area(src, 100, 50, 100, 150)
    
    face_cascade_path = './haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(src_gray)
    
    for x, y, w, h in faces:
        dst_face = mosaic_area(src, x, y, w, h)
    
    cv2.imwrite('./media/photos/opencv_mosaic_face.jpg', dst_face)
    
    src = cv2.cvtColor(cv2.imread('./media/photos/20/03/27/image9.jpg'), cv2.COLOR_BGR2RGB)
    
    imgs = [Image.fromarray(mosaic(src, 1 / i)) for i in range(1, 25)]
    imgs += imgs[-2::-1] + [Image.fromarray(src)] * 5
    
    imgs[0].save('./media/photos/opencv_mosaic.gif',
                 save_all=True, append_images=imgs[1:], optimize=False, duration=50, loop=0)