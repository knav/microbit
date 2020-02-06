from microbit import *
from random import randint
from sys import exit

#Start player off in the middle
player_x = 2

# Positive bias if accelerometer tends to left, negative bias if accelerometer tends to right
bias = 125
min_x = -500 + bias
max_x = 500 + bias
range_x = max_x - min_x

bullets = []
enemies = []
score = 0
speed = 2000
refresh = 100

while True:
    for enemy in enemies:
        # Check for end-game condition
        if enemy == [player_x,4]:
            display.show(Image.SAD)
            sleep(500)
            display.scroll("Game Over!")
            display.scroll("Score: " + str(score))
            exit(0)
        else:
            # Increase speed of enemies with every increment of 5 in score
            if speed > 500:
                speed = 2000 - ((divmod(score, 5)[0])*100)
            display.set_pixel(enemy[0], enemy[1], 0)

    x = accelerometer.get_x()
    x = min(max(min_x, x), max_x)
    x = ((x - min_x) / range_x) * 5
    x = min(max(0, x), 4)
    x = int(x + 0.5)
    display.set_pixel(player_x, 4, 0) # turn off old pixel
    for bullet in bullets:
        display.set_pixel(bullet[0], bullet[1], 0)
        bullet[1] -= 1
    bullets = [bullet for bullet in bullets if bullet[1] >= 0]
    for enemy in enemies:
        if enemy in bullets:
            enemies.remove(enemy)
            bullets.remove(enemy)
            score += 1
    if player_x < x:
        player_x += 1
    elif player_x > x:
        player_x -= 1
    display.set_pixel(player_x, 4, 9)

    if (running_time() % speed) < refresh:
        for enemy in enemies:
            if enemy[1] < 4:
                enemy[1] += 1
            else:
                enemies.remove(enemy)
                score += 1
        new_enemy = [randint(0,4), 0]
        if new_enemy not in enemies:
            enemies.append(new_enemy)

    for enemy in enemies:
        display.set_pixel(enemy[0], enemy[1], 6)

    for bullet in bullets:
        display.set_pixel(bullet[0], bullet[1], 3)

    start = running_time()
    while (running_time() - start) < refresh:
        if button_b.is_pressed() or button_a.is_pressed():
            if len(bullets) < 1:
                bullets.append([player_x, 4])
                sleep(refresh - (running_time() - start))