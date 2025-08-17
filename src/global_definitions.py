# Global definitions

# Shift reg to Pi 5 GPIO pin mappings
# https://www.ti.com/lit/ds/symlink/sn74hc165.pdf?ts=1723361350138 

LATCH = 25 # GPIO address of shift reg latch (1)
CLOCK = 23 # GPIO address of shift reg sclk (2)
OFFSET = 0 # Global offset added to all data values (9)
PULSE_WIDTH = 0.05 # Pulse width for latch / clock
DATA = 24 # GPIO address of shift reg data line
