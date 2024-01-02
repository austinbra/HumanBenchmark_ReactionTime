from PIL import ImageGrab
import time
import pyautogui

def checkColor(x, y):
    pixel_color = pyautogui.pixel(x, y)
    return pixel_color


while True:
    if checkColor(842,614) == (75,219,106):
        pyautogui.click(x=842, y=614)

