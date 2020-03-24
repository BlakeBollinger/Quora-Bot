import pyautogui
import pyscreenshot as ImageGrab

while True:
    print(pyautogui.position())

    r, g, b = 0, 0, 0
    im = ImageGrab.grab(bbox=(1352, 607, 1353, 608))  # X1,Y1,X2,Y2

    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((0, 0))

    print(r, g, b)