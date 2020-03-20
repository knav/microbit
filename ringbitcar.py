from microbit import *
import neopixel
import radio

"""
Good reference: https://www.firialabs.com/blogs/lab-notes/continuous-rotation-servos-with-python-and-the-micro-bit
"""

hz = 50         # Set the wanted hertz (e.g. 50Hz means that the signal is sent 50 times in one second)
scale = 100     # Scale of the speed of movement (e.g. scale of 100 means you can input values from 0 to 100)

t = int(1000 / hz)          # Duration of one pulse cycle
pin1.set_analog_period(t)   # Set the pulse cycle periods for servos
pin2.set_analog_period(t)
headlights = neopixel.NeoPixel(pin0, 2)
radio.on()
radio.config(channel=20)

up = Image("00900:09990:90909:00900:00900")
right = Image("00900:00090:99999:00090:00900")
left = Image("00900:09000:99999:09000:00900")

# Get speed of rotation in respective directions, using scale of 1 to 100
def rot(speed):
    high_percent = (1.5 - ((speed / scale) * 0.5)) / t    # positive - clockwise; negative - counterclockwise
    return high_percent


# Direction, speed and duration of linear movement; Positive = Forward, Negative = Backward, 0 = stop
def move(speed=100, duration=200):
    pin1.write_analog(1023 * rot(-speed))
    pin2.write_analog(1023 * rot(speed))
    sleep(duration)


# Direction, speed and duration of turning on the spot; Positive = Left, Negative = Right
def turn(speed=100, duration=200):
    pin1.write_analog(1023 * rot(speed))
    pin2.write_analog(1023 * rot(speed))
    sleep(duration)


def show_lights(lights, red, green, blue):
    for pixel_id in range(0, len(lights)):
        lights[pixel_id] = (red, green, blue)
    lights.show()


while True:
    incoming = radio.receive()
    if incoming is None:
        display.show(Image.ANGRY)
        sleep(200)
    # else:
    #     display.scroll(incoming)
    #     sleep(500)
    elif incoming == "left":
        display.show(left)
        show_lights(headlights, 255, 0, 0)
        turn(100)
    elif incoming == "right":
        display.show(right)
        show_lights(headlights, 0, 0, 255)
        turn(-100)
    elif incoming == "stop":
        display.show(Image.NO)
        show_lights(headlights, 0, 0, 255)
        move(0)
    else:
        display.show(Image.YES)
        v = int(incoming)
        display.show(up)
        show_lights(headlights, 255, 255, 255)
        move(v)


"""
def move_forward(speed = 100, duration = 2000):
    pin1.write_analog(1023 * (1.5 + ((speed / 100) * 0.5)) / t)
    pin2.write_analog(1023 * (1.5 - ((speed / 100) * 0.5)) / t)
    sleep(duration)

def move_backward(speed = 100, duration = 2000):
    pin1.write_analog(1023 * (1.5 - ((speed / 100) * 0.5)) / t)
    pin2.write_analog(1023 * (1.5 + ((speed / 100) * 0.5)) / t)
    sleep(duration)

def turn_left(speed = 100, duration = 2000):
    pin1.write_analog(1023 * (1.5 + ((speed / 100) * 0.5)) / t)
    pin2.write_analog(1023 * (1.5 + ((speed / 100) * 0.5)) / t)
    sleep(duration)

def turn_right(speed = 100, duration = 2000):
    pin1.write_analog(1023 * (1.5 - ((speed / 100) * 0.5)) / t)
    pin2.write_analog(1023 * (1.5 - ((speed / 100) * 0.5)) / t)
    sleep(duration)

def dont_move(duration = 2000):
    pin1.write_analog(1023 * stop)
    pin2.write_analog(1023 * stop)
    sleep(duration)
"""