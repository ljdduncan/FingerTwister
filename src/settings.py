# Global definitions

# Shift reg to Pi 5 GPIO pin mappings
# https://www.ti.com/lit/ds/symlink/sn74hc165.pdf?ts=1723361350138 
CLOCK_SWITCH = 23 # GPIO address of shift reg sclk (2)
DATA_SWITCH = 24 # GPIO address of shift reg data line
LATCH_SWITCH = 25 # GPIO address of shift reg latch (1)

CLOCK_LED = 22
DATA_LED = 17
LATCH_LED = 27

OFFSET = 0 # Global offset added to all data values (9)
PULSE_WIDTH = 0.0001 # Pulse width for latch / clock

DISPLAY_W = 1920
DISPLAY_H = 1080

FONT = '/home/FingerTwister/assets/8bitoperator_jve.ttf'
ASSETS_FOLDER = '/home/FingerTwister/assets/'
TEXT_COLOR = (0, 0, 25)
BACKGROUND_COLOR = (255, 255, 230)
RED = (243, 0, 0)

SLIDE_SPEED = 128