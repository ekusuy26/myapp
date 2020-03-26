from PIL import Image
from django.shortcuts import render
from match.models import UserInfo
import cv2
import matplotlib.pyplot as plt


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
#     img = cv2.imread('./media/photos/20/03/24/images.jpg')
#     orgsize = img.shape[:2][::-1]
     
#     img = cv2.resize(img, (int(orgsize[0]/20), int(orgsize[1]/20))) #画像を1/20に縮小
#     img = cv2.resize(img, orgsize) #画像を元のサイズに拡大
     
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) #matplotlibで表示する場合はRGBからBGRに変換
#     plt.imshow(img)
#     # aaa = cv2.imread('./media/photos/20/03/24/images.jpg')
#     # return render(request, 'myhp/create.html', context)
#     params = { # <- 渡したい変数を辞書型オブジェクトに格納
#         'photo': plt.savefig('out.png'),
#     }
#     return render(request, 'myhp/create.html', params)

def mosaic(request):
    src = cv2.imread('./media/photos/20/03/24/download.jpg')
    small = cv2.resize(src, None, fx=0.1, fy=0.1, interpolation=cv2.INTER_NEAREST)
    img = cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    cv2.imwrite('./media/photos/opencv_mosaic_01.jpg', img)
    return render(request, 'myhp/create.html', {})