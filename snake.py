from microbit import *
from random import randint

snake = [[2,2]]
food = [randint(1,4), randint(1,4)]
directions = [[1,0],[0,1],[-1,0],[0,-1]]
direction = 0

while True:
    if len(snake) > 6:
        display.scroll("You win!")

    start = running_time()

    while (running_time() - start) < 500:
        if button_a.is_pressed():
            if direction == 0:
                direction = 3
            else:
                direction -= 1
            sleep(500-(running_time() - start))

        if button_b.is_pressed():
            if direction == 3:
                direction = 0
            else:
                direction += 1
            sleep(500-(running_time() - start))

    next_block = [(snake[0][0] + directions[direction][0]) % 5, (snake[0][1] + directions[direction][1]) % 5]

    if next_block in snake:
        display.scroll("Game Over!")
        break

    snake = [next_block] + snake

    if food in snake:
        while food in snake:
            food = [randint(1,4), randint(1,4)]
    else:
        snake.pop()

    display.clear()
    display.set_pixel(food[0], food[1], 9)
    for block in snake:
        display.set_pixel(block[0], block[1], 5)