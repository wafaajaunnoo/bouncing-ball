import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_ball():
    ball = "O"
    direction = 1
    position = 0

    while True:
        clear_console()
        print(" " * position + ball)
        time.sleep(0.1)

        position += direction
        if position == 0 or position == 40:
            direction *= -1

animate_ball()
