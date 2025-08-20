import gpiod as IO
import time

TEST = 16

chip = IO.Chip('gpiochip4')

button = chip.get_line(TEST)

button.request(consumer="Button", type=IO.LINE_REQ_DIR_IN)

while True:
    button_state = button.get_value()
    time.sleep(.5)
    if button_state == 1:
        print("press")
    else:
        print("not press")