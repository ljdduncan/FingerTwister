import gpiod as IO
import time

CLOCK = 22
DATA = 17
LATCH = 27
PULSEWIDTH = .0001

register = [0]*40
LED = 0

chip = IO.Chip('gpiochip4')

clock_line = chip.get_line(CLOCK)
data_line = chip.get_line(DATA)
latch_line = chip.get_line(LATCH)

clock_line.request(consumer="Clock", type=IO.LINE_REQ_DIR_OUT)
data_line.request(consumer="Data", type=IO.LINE_REQ_DIR_OUT)
latch_line.request(consumer="Latch", type=IO.LINE_REQ_DIR_OUT)


# latch_line.set_value(0)
# for index, button in enumerate(register):
#     data_line.set_value(0)
#     clock_line.set_value(1)
#     clock_line.set_value(0)
latch_line.set_value(1)

mode = input("Choose mode: ")

while True:

    if mode == "1":
        print(register)
        for index, button in enumerate(register):
            # if index == LED:
            #     data_line.set_value(1)
            #     print("setting data line: ")
            #     print(index)
            # else:
            #     data_line.set_value(0)
            data_line.set_value(register[index])
            if register[index] == 0:
                register[index] = 1
            else:
                register[index] = 0

            # Shifts to next LED
            clock_line.set_value(1)
            time.sleep(PULSEWIDTH) #needed. idk how long yet though
            clock_line.set_value(0)

        # Loads LED values into register memory
        latch_line.set_value(0)
        time.sleep(PULSEWIDTH) #needed. idk how long yet though
        latch_line.set_value(1)
        time.sleep(1)



    if mode == "2":
        for index, button in enumerate(register):
            if index == LED:
                data_line.set_value(1)
                print("setting data line: ")
                print(index)
            else:
                data_line.set_value(0)
            

            # Shifts to next LED
            clock_line.set_value(1)
            clock_line.set_value(0)

        if LED == 39:
            LED = LED - 39
        else:
            LED = LED + 1

        # Loads LED values into register memory
        latch_line.set_value(0)
        time.sleep(PULSEWIDTH) #needed. idk how long yet though
        latch_line.set_value(1)
        time.sleep(.1)

        
    if mode == "3":
        TEST_LED = input ("Input LED to test: ")
        
        for index, button in enumerate(register):
            if index == int(TEST_LED):
                data_line.set_value(1)
                print("setting data line: ")
                print(index)
            else:
                data_line.set_value(0)
            

            # Shifts to next LED
            clock_line.set_value(1)
            clock_line.set_value(0)



        # Loads LED values into register memory
        latch_line.set_value(0)
        time.sleep(PULSEWIDTH) #needed. idk how long yet though
        latch_line.set_value(1)
        time.sleep(.1)