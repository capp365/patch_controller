import subprocess
import time
import cv2
import pyautogui as pyag

from PIL import ImageGrab
from datetime import datetime
import numpy as np
from sklearn.metrics import mean_squared_error as mse
from matplotlib import pyplot as plt

def start():
    subprocess.Popen('E:\PatchCon\PatchCon.exe',shell=True)
    time.sleep(1)

def get_screenshot(filename=None,dir='./capture/test'):
    img = ImageGrab.grab()
    if filename is None:
        filename=str(datetime.now()).replace(':',"-").split('.')[0]
    img.save(dir+"/"+filename+".png")
    return filename


def find_location(img_location=None,debug=False):
    if img_location is None:
        img_location='./capture/test/'+ get_screenshot() +'.png'
    else:
        screen=cv2.imread(img_location)
    template = cv2.imread('./resource/icon_titles.png')
    #img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    #template = cv2.imread('mario_coin.png',0)
    w, h = template.shape[:2]

    res = cv2.matchTemplate(screen,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)
    if len(loc[0])!=1:
        print('Warning: Plural or no icons detected!')

    for pt in zip(*loc[::-1]):
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.rectangle(screen, (pt[0] -3, pt[1] -4), (pt[0] + 1024-3, pt[1] + 792-4), (255,0,0), 2)
        if debug:
            cv2.imwrite('./capture/find_location/'+str(datetime.now()).replace(':',"-").split('.')[0]+'.png',screen)

    return (pt[0]-3, pt[1]-4, pt[0]+1024-3, pt[1]+792-4)

def click(x,y):
    print('moveto:',x,y)
    pyag.moveTo(x,y)
    time.sleep(0.3)
    pyag.click()

def screen_capture(dir,position):
    x1,y1,x2,y2=position
    img = ImageGrab.grab(bbox=position)
    img.save(dir+"/"+str(datetime.now()).replace(':',"-").split('.')[0]+".png")

def main():
    start()
    filename=get_screenshot()
    position=find_location('./capture/test/'+filename+'.png',True)
    screen_capture('screencaptest',position)

if __name__ == '__main__':
    main()