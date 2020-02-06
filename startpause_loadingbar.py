# Add your Python code here. E.g.
from microbit import *


while True:
    for y in range(5):
        for x in range (5):
            pixel_state = display.get_pixel(x,y)
            if pixel_state == 9:
                display.set_pixel(x,y,0)
            else:
                display.set_pixel(x,y,9)
            
            start = running_time()
            
            while (running_time() - start) < 200:
                if button_a.is_pressed():
                    while True:
                        if button_b.is_pressed():
                            break