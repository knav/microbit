from microbit import *
import radio

radio.on()
radio.config(channel=20)
up = Image("00900:09990:90909:00900:00900")
down = Image("00900:00900:90909:09990:00900")
right = Image("00900:00090:99999:00090:00900")
left = Image("00900:09000:99999:09000:00900")

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send("stop")
        display.show(Image.NO)
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
        tilt = round((0 - (accelerometer.get_y() / 1023)) * 100)
        if -15 < tilt < 15:
            radio.send("stop")
            display.show(Image("00000:09990:09090:09990:00000"))
            sleep(200)
        elif tilt >= 15:
            radio.send(str(tilt))
            display.show(up)
            sleep(200)
        elif tilt <= -15:
            radio.send(str(tilt))
            display.show(down)
            sleep(200)
