from microbit import *
import radio

radio.on()
radio.config(channel=20)
up = Image("00900:09990:90909:00900:00900")
right = Image("00900:00090:99999:00090:00900")
left = Image("00900:09000:99999:09000:00900")

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send("move")
        display.show(up)
        sleep(200)
    elif button_a.is_pressed():
        radio.send("left")
        display.show(left)
        sleep(200)
    elif button_b.is_pressed():
        radio.send("right")
        display.show(right)
        sleep(200)
    else:
        radio.send("stop")
        display.show(Image.NO)
        sleep(200)