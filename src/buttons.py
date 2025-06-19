from enum import Enum
from settings import *

class ButtonState(Enum):
    HELD =       1
    NOT_HELD =   2

class ButtonError(Enum):
    EARLY_LET_GO = 1
    NEVER_PRESSED = 2

class ButtonColor(Enum):
    GREEN =     1
    BLUE =      2
    YELLOW =    3
    RED =       4
    WHITE =     5

class Buttons():
    def __init__(self):
        self.game_buttons = {}
        self.led_mapping = {}
        self.switch_mapping = {}
        self.wave_color = ButtonColor.BLUE

        self.game_buttons["BUTTON_UP"] = Button("Up", ButtonColor.WHITE, 1, 36, 0, 1)
        self.led_mapping[36] = "BUTTON_UP"
        self.switch_mapping[1] = "BUTTON_UP"
        self.game_buttons["BUTTON_DOWN"] = Button("Down", ButtonColor.WHITE, 3, 37, 0, 1)
        self.led_mapping[37] = "BUTTON_DOWN"
        self.switch_mapping[3] = "BUTTON_DOWN"
        self.game_buttons["BUTTON_BACK"] = Button("Back", ButtonColor.WHITE, 0, 38, 0, 1)
        self.led_mapping[38] = "BUTTON_BACK"
        self.switch_mapping[0] = "BUTTON_BACK"
        self.game_buttons["BUTTON_SELECT"] = Button("Select", ButtonColor.WHITE, 2, 39, 0, 1)
        self.led_mapping[39] = "BUTTON_SELECT"
        self.switch_mapping[2] = "BUTTON_SELECT"

        self.game_buttons["BUTTON_1"] = Button("1", ButtonColor.BLUE, 7, 23, 0, 0)
        self.led_mapping[26] = "BUTTON_1"
        self.switch_mapping[7] = "BUTTON_1"
        self.game_buttons["BUTTON_2"] = Button("2", ButtonColor.RED, 6, 16, 0, 0)
        self.led_mapping[16] = "BUTTON_2"
        self.switch_mapping[6] = "BUTTON_2"
        self.game_buttons["BUTTON_3"] = Button("3", ButtonColor.YELLOW, 5, 8, 0, 0)
        self.led_mapping[8] = "BUTTON_3"
        self.switch_mapping[5] = "BUTTON_3"
        self.game_buttons["BUTTON_4"] = Button("4", ButtonColor.GREEN, 4, 7, 0, 0)
        self.led_mapping[7] = "BUTTON_4"
        self.switch_mapping[4] = "BUTTON_4"
        self.game_buttons["BUTTON_5"] = Button("5", ButtonColor.BLUE, 15, 4, 0, 0)
        self.led_mapping[4] = "BUTTON_5"
        self.switch_mapping[15] = "BUTTON_5"
        self.game_buttons["BUTTON_6"] = Button("6", ButtonColor.RED, 14, 5, 0, 0)
        self.led_mapping[5] = "BUTTON_6"
        self.switch_mapping[14] = "BUTTON_6"
        self.game_buttons["BUTTON_7"] = Button("7", ButtonColor.RED, 8, 27, 0, 0)
        self.led_mapping[27] = "BUTTON_7"
        self.switch_mapping[8] = "BUTTON_7"
        self.game_buttons["BUTTON_8"] = Button("8", ButtonColor.YELLOW, 13, 17, 0, 0)
        self.led_mapping[17] = "BUTTON_8"
        self.switch_mapping[13] = "BUTTON_8"
        self.game_buttons["BUTTON_9"] = Button("9", ButtonColor.GREEN, 12, 9, 0, 0)
        self.led_mapping[9] = "BUTTON_9"
        self.switch_mapping[12] = "BUTTON_9"
        self.game_buttons["BUTTON_10"] = Button("10", ButtonColor.BLUE, 20, 1, 0, 0)
        self.led_mapping[1] = "BUTTON_10"
        self.switch_mapping[20] = "BUTTON_10"
        self.game_buttons["BUTTON_11"] = Button("11", ButtonColor.RED, 23, 12, 0, 0)
        self.led_mapping[12] = "BUTTON_11"
        self.switch_mapping[23] = "BUTTON_11"
        self.game_buttons["BUTTON_12"] = Button("12", ButtonColor.YELLOW, 22, 14, 0, 0)
        self.led_mapping[14] = "BUTTON_12"
        self.switch_mapping[22] = "BUTTON_12"
        self.game_buttons["BUTTON_13"] = Button("13", ButtonColor.YELLOW, 16, 31, 0, 0)
        self.led_mapping[31] = "BUTTON_13"
        self.switch_mapping[16] = "BUTTON_13"
        self.game_buttons["BUTTON_14"] = Button("14", ButtonColor.GREEN, 34, 2, 0, 0)
        self.led_mapping[2] = "BUTTON_14"
        self.switch_mapping[34] = "BUTTON_14"
        self.game_buttons["BUTTON_15"] = Button("15", ButtonColor.BLUE, 21, 15, 0, 0)
        self.led_mapping[15] = "BUTTON_15"
        self.switch_mapping[21] = "BUTTON_15"
        self.game_buttons["BUTTON_16"] = Button("16", ButtonColor.RED, 9, 0, 0, 0)
        self.led_mapping[0] = "BUTTON_16"
        self.switch_mapping[9] = "BUTTON_16"
        self.game_buttons["BUTTON_17"] = Button("17", ButtonColor.YELLOW, 10, 13, 0, 0)
        self.led_mapping[13] = "BUTTON_17"
        self.switch_mapping[10] = "BUTTON_17"
        self.game_buttons["BUTTON_18"] = Button("18", ButtonColor.GREEN, 11, 3, 0, 0)
        self.led_mapping[3] = "BUTTON_18"
        self.switch_mapping[11] = "BUTTON_18"
        self.game_buttons["BUTTON_19"] = Button("19", ButtonColor.GREEN, 17, 34, 0, 0)
        self.led_mapping[34] = "BUTTON_19"
        self.switch_mapping[17] = "BUTTON_19"
        self.game_buttons["BUTTON_20"] = Button("20", ButtonColor.BLUE, 18, 26, 0, 0)
        self.led_mapping[23] = "BUTTON_20"
        self.switch_mapping[18] = "BUTTON_20"
        self.game_buttons["BUTTON_21"] = Button("21", ButtonColor.RED, 19, 28, 0, 0)
        self.led_mapping[28] = "BUTTON_21"
        self.switch_mapping[19] = "BUTTON_21"
        self.game_buttons["BUTTON_22"] = Button("22", ButtonColor.YELLOW, 30, 24, 0, 0)
        self.led_mapping[24] = "BUTTON_22"
        self.switch_mapping[30] = "BUTTON_22"
        self.game_buttons["BUTTON_23"] = Button("23", ButtonColor.GREEN, 31, 22, 0, 0)
        self.led_mapping[22] = "BUTTON_23"
        self.switch_mapping[31] = "BUTTON_23"
        self.game_buttons["BUTTON_24"] = Button("24", ButtonColor.BLUE, 29, 6, 0, 0)
        self.led_mapping[6] = "BUTTON_24"
        self.switch_mapping[29] = "BUTTON_24"
        self.game_buttons["BUTTON_25"] = Button("25", ButtonColor.BLUE, 24, 35, 0, 0)
        self.led_mapping[35] = "BUTTON_25"
        self.switch_mapping[24] = "BUTTON_25"
        self.game_buttons["BUTTON_26"] = Button("26", ButtonColor.RED, 25, 32, 0, 0)
        self.led_mapping[32] = "BUTTON_26"
        self.switch_mapping[25] = "BUTTON_26"
        self.game_buttons["BUTTON_27"] = Button("27", ButtonColor.YELLOW, 26, 29, 0, 0)
        self.led_mapping[29] = "BUTTON_27"
        self.switch_mapping[26] = "BUTTON_27"
        self.game_buttons["BUTTON_28"] = Button("28", ButtonColor.GREEN, 27, 10, 0, 0)
        self.led_mapping[10] = "BUTTON_28"
        self.switch_mapping[27] = "BUTTON_28"
        self.game_buttons["BUTTON_29"] = Button("29", ButtonColor.BLUE, 28, 18, 0, 0)
        self.led_mapping[18] = "BUTTON_29"
        self.switch_mapping[28] = "BUTTON_29"
        self.game_buttons["BUTTON_30"] = Button("30", ButtonColor.RED, 32, 11, 0, 0)
        self.led_mapping[11] = "BUTTON_30"
        self.switch_mapping[32] = "BUTTON_30"
        self.game_buttons["BUTTON_31"] = Button("31", ButtonColor.RED, 33, 33, 0, 0)
        self.led_mapping[33] = "BUTTON_31"
        self.switch_mapping[33] = "BUTTON_31"
        self.game_buttons["BUTTON_32"] = Button("32", ButtonColor.YELLOW, 35, 25, 0, 0)
        self.led_mapping[25] = "BUTTON_32"
        self.switch_mapping[35] = "BUTTON_32"
        self.game_buttons["BUTTON_33"] = Button("33", ButtonColor.GREEN, 39, 21, 0, 0)
        self.led_mapping[21] = "BUTTON_33"
        self.switch_mapping[39] = "BUTTON_33"
        self.game_buttons["BUTTON_34"] = Button("34", ButtonColor.BLUE, 38, 20, 0, 0)
        self.led_mapping[20] = "BUTTON_34"
        self.switch_mapping[38] = "BUTTON_34"
        self.game_buttons["BUTTON_35"] = Button("35", ButtonColor.RED, 37, 30, 0, 0)
        self.led_mapping[30] = "BUTTON_35"
        self.switch_mapping[37] = "BUTTON_35"
        self.game_buttons["BUTTON_36"] = Button("36", ButtonColor.YELLOW, 36, 19, 0, 0)
        self.led_mapping[19] = "BUTTON_36"
        self.switch_mapping[36] = "BUTTON_36"

    def set_non_game_state(self):
        for button_key, button_value in self.game_buttons.items():
            if button_value.color == ButtonColor.WHITE:
                button_value.LED_state = 1
            else:
                button_value.LED_state = 0

    def pulse_wave(self):
        match self.wave_color:
            case ButtonColor.BLUE:
                self.wave_color = ButtonColor.RED
            case ButtonColor.RED:
                self.wave_color = ButtonColor.YELLOW
            case ButtonColor.YELLOW:
                self.wave_color = ButtonColor.GREEN
            case ButtonColor.GREEN:
                self.wave_color = ButtonColor.BLUE

        for button_key, button_value in self.game_buttons.items():
            if button_value.color == ButtonColor.WHITE or button_value.color == self.wave_color:
                button_value.LED_state = 1
            else:
                button_value.LED_state = 0

class Button():
    def __init__(self, name, color, switch_position, LED_position, switch_state, LED_state):
        self.name =     name
        self.color =    color
        self.switch_position = switch_position
        self.LED_position = LED_position
        self.switch_state = switch_state
        self.LED_state = LED_state
    