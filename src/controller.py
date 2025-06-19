import gpiod as IO
import settings
import time
import pygame

CLOCK_SWITCH = settings.CLOCK_SWITCH
DATA_SWITCH = settings.DATA_SWITCH
LATCH_SWITCH = settings.LATCH_SWITCH
CLOCK_LED = settings.CLOCK_LED
DATA_LED = settings.DATA_LED
LATCH_LED = settings.LATCH_LED

PULSEWIDTH = settings.PULSE_WIDTH

chip = IO.Chip('gpiochip4')

clock_line_switch = chip.get_line(CLOCK_SWITCH)
data_line_switch = chip.get_line(DATA_SWITCH)
latch_line_switch = chip.get_line(LATCH_SWITCH)
clock_line_led = chip.get_line(CLOCK_LED)
data_line_led = chip.get_line(DATA_LED)
latch_line_led = chip.get_line(LATCH_LED)

clock_line_switch.request(consumer="Clock", type=IO.LINE_REQ_DIR_OUT)
data_line_switch.request(consumer="Data", type=IO.LINE_REQ_DIR_IN)
latch_line_switch.request(consumer="Latch", type=IO.LINE_REQ_DIR_OUT)
clock_line_led.request(consumer="Clock", type=IO.LINE_REQ_DIR_OUT)
data_line_led.request(consumer="Data", type=IO.LINE_REQ_DIR_OUT)
latch_line_led.request(consumer="Latch", type=IO.LINE_REQ_DIR_OUT)

latch_line_switch.set_value(1)
latch_line_led.set_value(1)

def control_buttons(game_buttons, LED_mapping, switch_mapping):
    led_states = [0]*40
    switch_states = [0]*40
    altered_states = []

    # Sets up LED register to be pushed
    for button_key, button_value in game_buttons.items():
        led_states[button_value.LED_position] = button_value.LED_state

    # Loads switch states into local memory
    latch_line_switch.set_value(0)
    latch_line_switch.set_value(1)

    # Reads switch states into local memery
    for index, button_state in enumerate(switch_states):
        data_state = data_line_switch.get_value()
        switch_states[index] = data_state
        clock_line_switch.set_value(1)
        #do not add a pulse sleep. will create false positives
        clock_line_switch.set_value(0)

    # Puts LED states into register
    for led_state in led_states:
        data_line_led.set_value(led_state)

        # Shifts to next LED
        clock_line_led.set_value(1)
        time.sleep(PULSEWIDTH) #needed. idk how long yet though
        clock_line_led.set_value(0)

    # Loads LED values into register memory
    latch_line_led.set_value(0)
    time.sleep(PULSEWIDTH) #needed. idk how long yet though
    latch_line_led.set_value(1)

    # print("scanning switches")
    for index, new_switch_state in enumerate(switch_states):
        # print(new_switch_state)
        if new_switch_state != game_buttons[switch_mapping[index]].switch_state:
            game_buttons[switch_mapping[index]].switch_state = new_switch_state
            # print(game_buttons[switch_mapping[index]].name)
            if game_buttons[switch_mapping[index]].name == "Up" and new_switch_state == 1:
                # print("firing up event")
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP))
            elif game_buttons[switch_mapping[index]].name == "Down" and new_switch_state == 1:
                # print("firing down event")
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
            elif game_buttons[switch_mapping[index]].name == "Select" and new_switch_state == 1:
                # print("firing select event")
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
            elif game_buttons[switch_mapping[index]].name == "Back" and new_switch_state == 1:
                # print("firing back event")
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
            else:
                # print("switch changed:")
                # print(index)
                # print("switch mapped to:")
                # print(switch_mapping[index])
                altered_states.append(switch_mapping[index])
    
    return altered_states