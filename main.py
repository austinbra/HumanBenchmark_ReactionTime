from PIL import ImageGrab
import time
import pyautogui
import keyboard
import sys


def checkColor(x, y):
    #finds the rgb values at the coordinate
    pixel_color = pyautogui.pixel(x, y)
    return pixel_color

def get_xy():
    # Get the screen width and height
    screen_width, screen_height = pyautogui.size()
    # Calculate the coordinates of the point halfway down the screen a little to the left
    center_x = screen_width // 3
    center_y = screen_height // 2
    return center_x, center_y

print("Press the Ctrl key to run script")
while True:
    if keyboard.is_pressed('ctrl'):
        print("Running Code")
        while True:
            x,y = get_xy()
            if checkColor(x,y) == (75,219,106):
                pyautogui.click(x, y)    
#script only runs after the ctrl key is pressed
#to stop script click on terminal and press 'Ctrl + c'
