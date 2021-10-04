import keyboard
import mss
import cv2
import pyautogui
import numpy
from time import time, sleep
from playsound import playsound

pyautogui.PAUSE = 0

print("Press 's' to start playing.")
print("Once started press 'z' to quit.")
keyboard.wait('s')

sct = mss.mss()
dimensions_left = {
        'left': 560,
        'top': 50,
        'width': 800,
        'height': 30
    }

red_img = cv2.imread('ore4.png', cv2.IMREAD_UNCHANGED)

w = red_img.shape[1]
h = red_img.shape[0]


threshold = .80

while True:
    scr = numpy.array(sct.grab(dimensions_left))
    scr2 = numpy.array(sct.grab(dimensions_left))

    result = cv2.matchTemplate(scr, red_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    yloc, xloc = numpy.where(result >= threshold)
    for (x, y) in zip(xloc, yloc):
        playsound('beep.mp3')

	#un-comment the line below to see where its searching
    #cv2.imshow('Game', scr)
    cv2.waitKey(1)
    sleep(.10)
    if keyboard.is_pressed('z'):
        break