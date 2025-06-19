import gpiod as IO
import time

CLOCK = 23
DATA = 24
LATCH = 25
PULSEWIDTH = .01

register = [0]*40

chip = IO.Chip('gpiochip4')

clock_line = chip.get_line(CLOCK)
data_line = chip.get_line(DATA)
latch_line = chip.get_line(LATCH)

clock_line.request(consumer="Clock", type=IO.LINE_REQ_DIR_OUT)
data_line.request(consumer="Data", type=IO.LINE_REQ_DIR_IN)
latch_line.request(consumer="Latch", type=IO.LINE_REQ_DIR_OUT)

latch_line.set_value(1)

while True:
    latch_line.set_value(0)
    #time.sleep(PULSEWIDTH)
    latch_line.set_value(1)
    for index, button in enumerate(register):
        data_state = data_line.get_value()
        register[index] = data_state
        clock_line.set_value(1)
        #do not add a pulse sleep. will create false positives
        clock_line.set_value(0)
        if data_state == 1:
            print(index)
    #time.sleep(.1)
    # print(register)
