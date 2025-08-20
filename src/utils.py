import gpiod, time

CLOCK = 23
DATA = 24
LATCH = 25
PULSE_WIDTH = .01


# Gathers a new data frame
def _pulse_latch(latch_line):
    latch_line.set_value(0)
    time.sleep(PULSE_WIDTH)
    latch_line.set_value(1)


# Each clocl pulse pushes data down one register on the shift
def _pulse_clock(clock_line):
    clock_line.set_value(0)
    clock_line.set_value(1)
                         
def refresh_registers(reglist, data_line, clock_line, latch_line):
    _pulse_latch(latch_line)
    for index, button in enumerate(reglist):
        data_state = data_line.get_value()
        reglist[index] = data_state
        _pulse_clock(clock_line)
