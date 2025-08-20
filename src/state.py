import datetime
import settings
import random

from scene import *
from leaderboard import Leaderboard as Leaderboard_JSON


class State():
    def __init__(self, window, leaderboard, daily_leaderboard):
        self.scene = Scene(window, leaderboard, daily_leaderboard)
        self.leaderboard = leaderboard
        self.daily_leaderboard = daily_leaderboard
        self.nav_methods = {"main_menu": self.nav_to_main, 
                            "more_games": self.nav_to_more_games,
                            "credits": self.nav_to_credits, 
                            "cats": self.nav_to_cats,
                            "game": self.nav_to_game,
                            "memory_game": self.nav_to_memory_game,
                            "loss": self.nav_to_loss,
                            "win": self.nav_to_win,
                            "leaderboard": self.nav_to_leaderboard,
                            "daily_leaderboard": self.nav_to_daily_leaderboard,
                            "regenerate_daily_leaderboard" : self.regenerateDailyLeaderboard}

        self.main_menu = MainMenu(self.scene, self.nav_methods)

        #Unused. Just for debugging by putting them in starting state.
        self.leaderboard_scene = Leaderboard(self.scene, self.nav_methods, self.leaderboard)
        self.credits = Credits(self.scene, self.nav_methods)
        self.cats = Cats(self.scene, self.nav_methods)
        self.game = Game(self.scene, self.nav_methods)
        
        #Starting state
        self.current_state = self.main_menu

        self.last_game_record = 0
        self.altered_button = None
        self.last_game_state = {}


    def display_scene(self):
        self.current_state.display_scene()

    def handle_up(self):
        self.current_state.handle_up()

    def handle_down(self):
        self.current_state.handle_down()

    def handle_back(self):
        self.current_state.handle_back()

    def handle_select(self):
        self.current_state.handle_select()
        
    def nav_to_main(self):
        self.current_state = MainMenu(self.scene, self.nav_methods)

    def nav_to_more_games(self):
        self.current_state = MoreGames(self.scene, self.nav_methods)

    def nav_to_credits(self):
        self.current_state = Credits(self.scene, self.nav_methods)
        
    def nav_to_cats(self):
        self.current_state = Cats(self.scene, self.nav_methods)

    def nav_to_game(self):
        self.current_state = Game(self.scene, self.nav_methods)

    def nav_to_memory_game(self):
        self.current_state = MemoryGame(self.scene, self.nav_methods)

    def nav_to_loss(self):
        self.current_state = Loss(self.scene, self.nav_methods, self.last_game_record, self.scene.game_mode)

    def nav_to_win(self):
        self.current_state = Win(self.scene, self.nav_methods, self.last_game_record, self.leaderboard)

    def nav_to_leaderboard(self):
        self.current_state = Leaderboard(self.scene, self.nav_methods, self.leaderboard)

    def nav_to_daily_leaderboard(self):
        self.current_state = DailyLeaderboard(self.scene, self.nav_methods, self.daily_leaderboard)

    def handle_loss(self, message):
        self.current_state.handle_loss(message)

    def handle_win(self, message):
        self.current_state.handle_win(message)

    def handle_goto_main(self):
        self.current_state.handle_goto_main()

    def regenerateDailyLeaderboard(self):
        self.daily_leaderboard = Leaderboard_JSON(self.leaderboard.get_daily_leaderboard())
        self.scene.daily_leaderboard = self.daily_leaderboard

    def detect_presses(self, altered_states, last_pressed):
        return self.current_state.detect_presses(altered_states, last_pressed)
    
    def getBlinkState(self):
        return self.current_state.blink_state

class DefaultState():
    def __init__(self):
        pass

    def display_scene(self):
        print("WARNING: scene not displayed in child class (this is bad)")
        
    def handle_up(self):
        print("up button not handled in child class")
        
    def handle_down(self):
        print("down button not handled in child class")
        
    def handle_select(self):
        print("select button not handled in child class")
        
    def handle_back(self):
        print("back button not handled in child class")

    def handle_loss(self):
        print("loss not handled in child class")

    def detect_presses(self):
        print("detect presses not handled in child class")

    def handle_goto_main(self):
        print("go to main not handled in child class")

class MainMenu(DefaultState):
    def __init__(self, scene, nav_methods):
        self.state_name = "Main"
        self.scene = scene
        self.nav_methods = nav_methods
        self.menu = ["Play", "Memory Game", "Leaderboard", "Credits"]
        self.selection = self.menu[0]
        self.slide = None
        self.render = None
        self.time = int(datetime.datetime.now().timestamp())
        self.fib = [1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.timer_buttons = [[1, "large_red", False], [2, "large_blue", False],[3, "large_green", False],[4, "large_yellow", False],[5, "large_red", False],[6, "large_blue", False],[7, "large_green", False],[8, "large_yellow", False],[9, "large_red", False]]

    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            try:
                check_time = int((int(datetime.datetime.now().timestamp()) - self.time)/60)
                if check_time in self.fib:
                    self.fib.remove(check_time)
                    choice = random.choice([i for i in self.timer_buttons if not i[2]])
                    self.timer_buttons[self.timer_buttons.index(choice)][2] = True
            except Exception as e:
                print(e)
            finally:
                self.render = self.scene.display_main_menu(self.selection, self.timer_buttons)
        
    def handle_up(self):
        next_selection = self.menu.index(self.selection) - 1
        self.selection = self.menu[next_selection % len(self.menu)]
        self.display_scene
        
    def handle_down(self):
        next_selection = self.menu.index(self.selection) + 1
        self.selection = self.menu[next_selection % len(self.menu)]
        self.display_scene
        
    def handle_select(self):
        match self.selection:
            case "Play":
                if self.render and not self.slide: 
                    self.slide = SlideTrasition(self.scene, self.nav_methods["game"], self.render, "Game")
            case "Memory Game":
                if self.render and not self.slide: 
                    self.slide = SlideTrasition(self.scene, self.nav_methods["memory_game"], self.render, "Memory Game")
            case "Leaderboard":
                if self.render and not self.slide: 
                    self.slide = SlideTrasition(self.scene, self.nav_methods["daily_leaderboard"], self.render, "Daily Leaderboard")
            # case "More Game Modes":
                # if self.render and not self.slide: 
                    # self.slide = SlideTrasition(self.scene, self.nav_methods["more_games"], self.render, "More Game Modes")
            case "Credits":
                if self.render and not self.slide: 
                    self.slide = SlideTrasition(self.scene, self.nav_methods["credits"], self.render, "Credits")
                
    def handle_back(self):
        return None
    
    def handle_goto_main(self):
        return None #main menu should never navigate to main menu

class MoreGames(DefaultState):
    def __init__(self, scene, nav_methods):
        self.state_name = "More Game Modes"
        self.scene = scene
        self.nav_methods = nav_methods
        self.more_games_menu = ["Memory Game", "asdf", "asdf2"]
        self.selection = self.more_games_menu[0]
        self.slide = None
        self.render = None

    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            self.render = self.scene.display_more_games(self.selection)
        
    def handle_up(self):
        next_selection = self.more_games_menu.index(self.selection) - 1
        self.selection = self.more_games_menu[next_selection % len(self.more_games_menu)]
        self.display_scene
        
    def handle_down(self):
        next_selection = self.more_games_menu.index(self.selection) + 1
        self.selection = self.more_games_menu[next_selection % len(self.more_games_menu)]
        self.display_scene
        
    def handle_select(self):
        match self.selection:
            case "Memory Game":
                if self.render and not self.slide: 
                    self.slide = SlideTrasition(self.scene, self.nav_methods["memory_game"], self.render, "Memory Game")
            case "asdf":
                if self.render and not self.slide: 
                    self.slide = SlideTrasition(self.scene, self.nav_methods["daily_leaderboard"], self.render, "Daily Leaderboard")
            case "asdf2":
                if self.render and not self.slide: 
                    self.slide = SlideTrasition(self.scene, self.nav_methods["more_games"], self.render, "More Game Modes")
                
    def handle_back(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")

class Credits(DefaultState):
    def __init__(self, scene, nav_methods):
        self.state_name = "Credits"
        self.scene = scene
        self.nav_methods = nav_methods
        self.slide = None
        self.render = None

    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            self.render = self.scene.display_credits()
        
    def handle_up(self):
        return None
        
    def handle_down(self):
        return None

    def handle_select(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["cats"], self.render, "Cats")

    def handle_back(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")


class Cats(DefaultState):
    def __init__(self, scene, nav_methods):
        self.state_name = "Cats"
        self.scene = scene
        self.nav_methods = nav_methods
        self.slide = None
        self.render = None

    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            self.render = self.scene.display_cats()
        
    def handle_up(self):
        return None
        
    def handle_down(self):
        return None
        
    def handle_select(self):
        return None

    def handle_back(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")

class Game(DefaultState):
    def __init__(self, scene, nav_methods):
        self.state_name = "Game"
        self.scene = scene
        self.nav_methods = nav_methods
        self.slide = None
        self.render = None

        # Determines how buttons are displayed. First value is if button is pressed. Second value is if LED is lit.
        self.display_buttons_state = [(0,0)]*36
        #self.possible_buttons = ["BUTTON_1", "BUTTON_2", "BUTTON_3", "BUTTON_4", "BUTTON_5", "BUTTON_6","BUTTON_7", "BUTTON_8", "BUTTON_9", "BUTTON_10"]
        self.possible_buttons = ["BUTTON_1", "BUTTON_2", "BUTTON_3", "BUTTON_4", "BUTTON_5", "BUTTON_6", 
                                 "BUTTON_7", "BUTTON_8", "BUTTON_9", "BUTTON_10", "BUTTON_11", "BUTTON_12", 
                                 "BUTTON_13", "BUTTON_14", "BUTTON_15", "BUTTON_16", "BUTTON_17", "BUTTON_18", 
                                 "BUTTON_19", "BUTTON_20", "BUTTON_21", "BUTTON_22", "BUTTON_23", "BUTTON_24", 
                                 "BUTTON_25", "BUTTON_26", "BUTTON_27", "BUTTON_28", "BUTTON_29", "BUTTON_30", 
                                 "BUTTON_31", "BUTTON_32", "BUTTON_33", "BUTTON_34", "BUTTON_35", "BUTTON_36"]
        self.target_button = random.choice(self.possible_buttons)
        self.target_button_num = int(self.target_button.split("_")[1])
        self.display_buttons_state[self.target_button_num-1] = (self.display_buttons_state[self.target_button_num-1][0], 1)
        self.possible_buttons.remove(self.target_button)
        # print("initial target")
        # print(self.target_button)
        self.scene.game_mode = "Game"


    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            self.render = self.scene.display_game(self.display_buttons_state)
        
    def handle_up(self):
        return None
        
    def handle_down(self):
        return None
        
    def handle_select(self):
        return None
        
    def handle_back(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")

    def handle_loss(self, message):
        if self.render and not self.slide:
            self.scene.last_game_record = int(message[0].split(":")[1])
            self.scene.last_game_state = {"buttons": self.display_buttons_state, "target": self.target_button, "altered": self.altered_button}
            self.slide = SlideTrasition(self.scene, self.nav_methods["loss"], self.render, "Loss")

    def handle_win(self, message):
        if self.render and not self.slide:
            self.scene.last_game_record = int(message[0].split(":")[1])
            self.scene.last_game_state = {"buttons": self.display_buttons_state, "target": self.target_button, "altered": self.altered_button}
            self.slide = SlideTrasition(self.scene, self.nav_methods["win"], self.render, "Win")
    
    # Returns tuple of the target button if it was pressed and boolean for if the game is over (true is over, false is continuing game)
    def detect_presses(self, altered_states, last_pressed):
        if len(altered_states) > 0 and altered_states[0] == self.target_button:
            if len(self.possible_buttons) == 0:
                last_button_num = int(self.target_button.split("_")[1])
                self.display_buttons_state[last_button_num-1] = (1, self.display_buttons_state[last_button_num-1][1])
                self.altered_button = -1
                self.target_button = -1
                return "win:36", True
            last_button_num = int(self.target_button.split("_")[1])
            self.display_buttons_state[last_button_num-1] = (1, self.display_buttons_state[last_button_num-1][1])

            self.target_button = random.choice(self.possible_buttons)
            target_button_num = int(self.target_button.split("_")[1])

            self.possible_buttons.remove(self.target_button)
            self.display_buttons_state[target_button_num-1] = (self.display_buttons_state[target_button_num-1][0], 1)

        elif (len(altered_states) > 0  and altered_states[0] != self.target_button) or (len(altered_states) > 1):
            # print("altered button")
            # print(altered_states[0])
            # print("target button")
            # print(self.target_button)
            try:
                self.altered_button = int(altered_states[0].split("_")[1])
                pressed = 35 - len(self.possible_buttons)
                self.target_button = "pressed:" + str(pressed)
                return self.target_button, True
            except:
                pass #lol
        return self.target_button, False

class MemoryGame(DefaultState):
    def __init__(self, scene, nav_methods):
        self.state_name = "Memory Game"
        self.scene = scene
        self.nav_methods = nav_methods
        self.slide = None
        self.render = None

        self.memory_list = []
        self.pressed_list = []

        self.blinking = False
        self.blink_timer = 0
        self.blink_length = 0

        self.blink_state = (0, 0)
        self.blink_position = 0
        self.lead_time = 30
        self.on_time = 25
        self.off_time = 10

        # Determines how buttons are displayed. First value is if button is pressed. Second value is if LED is lit.
        self.display_buttons_state = [(0,0)]*36
        #self.possible_buttons = ["BUTTON_1", "BUTTON_2", "BUTTON_3", "BUTTON_4", "BUTTON_5", "BUTTON_6","BUTTON_7", "BUTTON_8", "BUTTON_9", "BUTTON_10"]
        self.possible_buttons = ["BUTTON_1", "BUTTON_2", "BUTTON_3", "BUTTON_4", "BUTTON_5", "BUTTON_6", 
                                 "BUTTON_7", "BUTTON_8", "BUTTON_9", "BUTTON_10", "BUTTON_11", "BUTTON_12", 
                                 "BUTTON_13", "BUTTON_14", "BUTTON_15", "BUTTON_16", "BUTTON_17", "BUTTON_18", 
                                 "BUTTON_19", "BUTTON_20", "BUTTON_21", "BUTTON_22", "BUTTON_23", "BUTTON_24", 
                                 "BUTTON_25", "BUTTON_26", "BUTTON_27", "BUTTON_28", "BUTTON_29", "BUTTON_30", 
                                 "BUTTON_31", "BUTTON_32", "BUTTON_33", "BUTTON_34", "BUTTON_35", "BUTTON_36"]
        self.memory_list.append(random.choice(self.possible_buttons))
        self.target_button = self.memory_list[0]
        self.blink_state = (self.memory_list[self.blink_position] , 1)
        print(self.memory_list)
        self.target_button_num = int(self.target_button.split("_")[1])
        self.display_buttons_state[self.target_button_num-1] = (self.display_buttons_state[self.target_button_num-1][0], 1)

        self.scene.game_mode = "Memory Game"


    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            if self.blinking == True and self.blink_timer <= self.blink_length:
                self.blink_sequence()
            else:
                self.blinking = False
                self.blink_timer = 0
            self.render = self.scene.display_memory_game(len(self.memory_list) - 1, self.display_buttons_state)
        
    def handle_up(self):
        return None
        
    def handle_down(self):
        return None
        
    def handle_select(self):
        return None
        
    def handle_back(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")

    def handle_loss(self, message):
        if self.render and not self.slide:
            self.scene.last_game_record = int(message[0].split(":")[1])
            self.scene.last_game_state = {"buttons": self.display_buttons_state, "target": self.target_button, "altered": self.altered_button}
            self.slide = SlideTrasition(self.scene, self.nav_methods["loss"], self.render, "Loss")

    def handle_win(self):
        pass # you cannot win

    def blink_sequence(self):
        print("blink timer")
        print(self.blink_timer)
        print("blink length")
        print(self.blink_length)
        print("blink position")
        print(self.blink_position)
        #turn on light during on time
        if self.blink_timer == 0:
            self.blink_state = (self.memory_list[self.blink_position],0)
        elif self.blink_timer == self.lead_time + (self.blink_position * self.on_time) + (self.blink_position * self.off_time):
            # print("blink pos")
            # print(self.blink_position)
            # print("turning on light")
            # print("int(self.memory_list[self.blink_position].split('_')[1])-1")
            # print(int(self.memory_list[self.blink_position].split("_")[1])-1)
            # print((self.display_buttons_state[int(self.memory_list[self.blink_position].split("_")[1])-1][0], 1))
            # print("blink state")
            # print((self.memory_list[self.blink_position],1))
            self.blink_state = (self.memory_list[self.blink_position],1)
            self.display_buttons_state[int(self.memory_list[self.blink_position].split("_")[1])-1] = (self.display_buttons_state[int(self.memory_list[self.blink_position].split("_")[1])-1][0], 1)
        #turn off light during off time
        elif self.blink_timer == self.lead_time + (self.blink_position + 1) * self.on_time + self.blink_position * self.off_time:
            # print("turning off light")
            self.blink_state = (self.memory_list[self.blink_position],0)
            self.display_buttons_state = [(0,0)]*36
            if (self.blink_position < len(self.memory_list) - 1):
                self.blink_position = self.blink_position + 1
            # print("blink pos")
            # print(self.blink_position)
        #finish blinking
        if self.blink_timer == self.blink_length:
            # print("blinking finished")
            self.blinking = False
        self.blink_timer = self.blink_timer + 1

    def getCurrentBlink(self):
        pass

    # Returns tuple of the target button if it was pressed and boolean for if the game is over (true is over, false is continuing game)
    def detect_presses(self, altered_states, last_pressed):
        if not self.blinking:
            if last_pressed != None:
                # print("last_pressed")
                # print(last_pressed)
                # print("")
                # print("self.target_button")
                # print(self.target_button)
                # print("")
                self.pressed_list.append(last_pressed)
                if last_pressed == self.target_button:
                    # print("self.memory_list")
                    # print(self.memory_list)
                    # print("")
                    # print("self.pressed_list")
                    # print(self.pressed_list)
                    # print("")
                        
                    if len(self.memory_list) == len(self.pressed_list):
                        self.memory_list.append(random.choice(self.possible_buttons))
                        self.display_buttons_state = [(0,0)]*36
                        self.pressed_list = []
                        self.blink_timer = 0
                        self.blink_position = 0
                        self.blinking = True
                        self.target_button = self.memory_list[0]
                        self.blink_length = self.lead_time + (len(self.memory_list) * self.on_time) + ((len(self.memory_list) - 1) * self.off_time)
                        print("new blink length")
                        print(self.blink_length)
                    else:
                        self.target_button = self.memory_list[len(self.pressed_list)]


                elif last_pressed != self.target_button or (len(altered_states) > 1):
                    # print("altered button")
                    # print(altered_states[0])
                    # print("target button")
                    # print(self.target_button)
                    try:
                        print("triggering loss")
                        self.altered_button = int(last_pressed.split("_")[1])
                        pressed = len(self.memory_list) - 1
                        self.target_button = "pressed:" + str(pressed)
                        return self.target_button, True
                    except Exception as e:
                        print(f"write better exception handling {e}")
                        pass #lol
            return self.target_button, False
        else:
            return self.target_button, False

class Leaderboard(DefaultState):
    def __init__(self, scene, nav_methods, leaderboard):
        self.state_name = "Leaderboard"
        self.scene = scene
        self.nav_methods = nav_methods
        self.slide = None
        self.render = None
        self.leaderboard = leaderboard
        self.selection = 0

    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            self.render = self.scene.display_leaderboard(self.selection, self.leaderboard)
    
    def handle_up(self):
        next_selection = self.selection - 1
        if self.leaderboard.length != 0:
            self.selection = next_selection % (self.leaderboard.length if self.leaderboard.length < 10 else 9)
        self.display_scene
        
    def handle_down(self):
        next_selection = self.selection + 1
        if self.leaderboard.length != 0:
            self.selection = next_selection % (self.leaderboard.length if self.leaderboard.length < 10 else 9)
        self.display_scene
        
    def handle_select(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["daily_leaderboard"], self.render, "Daily Leaderboard")
        
    def handle_back(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
class DailyLeaderboard(DefaultState):
    def __init__(self, scene, nav_methods, leaderboard):
        self.state_name = "Daily Leaderboard"
        self.scene = scene
        self.nav_methods = nav_methods
        self.slide = None
        self.render = None
        self.leaderboard = leaderboard
        
        self.selection = 0

    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            self.render = self.scene.display_daily_leaderboard(self.selection, self.leaderboard)
    
    def handle_up(self):
        next_selection = self.selection - 1
        if self.leaderboard.length != 0:
            self.selection = next_selection % (self.leaderboard.length if self.leaderboard.length < 10 else 9)
        self.display_scene
        
    def handle_down(self):
        next_selection = self.selection + 1
        if self.leaderboard.length != 0:
            self.selection = next_selection % (self.leaderboard.length if self.leaderboard.length < 10 else 9)
        self.display_scene
    
    def handle_select(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["leaderboard"], self.render, "Leaderboard")
    
    def handle_back(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")

class Loss(DefaultState):
    def __init__(self, scene, nav_methods, last_game_record, game_mode):
        self.state_name = "Loss"
        self.scene = scene
        self.nav_methods = nav_methods
        self.slide = None
        self.render = None
        self.last_game_record = last_game_record
        self.game_mode = game_mode

    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            self.render = self.scene.display_loss(self.last_game_record, self.scene.last_game_state)
        
    def handle_up(self):
        return None
        
    def handle_down(self):
        return None
        
    def handle_select(self):
        if self.render and not self.slide:
            match self.game_mode:
                case "Game":
                    nav_type = "game"
                case "Memory Game":
                    nav_type = "memory_game"
            print("nav_type")
            print(nav_type)
            self.slide = SlideTrasition(self.scene, self.nav_methods[nav_type], self.render, self.game_mode)

    def handle_back(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")

class Win(DefaultState):
    def __init__(self, scene, nav_methods, last_game_record, leaderboard):
        self.state_name = "Win"
        self.scene = scene
        self.nav_methods = nav_methods
        self.slide = None
        self.render = None
        self.last_game_record = last_game_record
        self.name_entry = [65, 65, 65] #html number for unicode characters
        self.selection = 0
        self.leaderboard = leaderboard

        
    def handle_select(self):
        if self.render and not self.slide:
            if self.selection == 2:
                self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
                self.leaderboard.update_leaderboard(self.last_game_record,chr(self.name_entry[0])+chr(self.name_entry[1])+chr(self.name_entry[2]),self.scene.last_game_state)
                self.nav_methods["regenerate_daily_leaderboard"]()
            else:
                self.selection = self.selection + 1

    def handle_back(self):
        if self.render and not self.slide:
            if self.selection != 0:
                self.selection = self.selection - 1
        
    def handle_up(self):
        if self.render and not self.slide:
            if self.name_entry[self.selection] == 90:
                self.name_entry[self.selection] = 65
            # Adds numbers and spaces
            # if self.name_entry[self.selection] == 90:
            #     self.name_entry[self.selection] = 32
            # elif self.name_entry[self.selection] == 32:
            #     self.name_entry[self.selection] = 48
            # elif self.name_entry[self.selection] == 57:
            #     self.name_entry[self.selection] = 65
            else:
                self.name_entry[self.selection] = self.name_entry[self.selection] + 1
        
    def handle_down(self):
        if self.render and not self.slide:
            if self.name_entry[self.selection] == 65:
                self.name_entry[self.selection] = 90
            # Adds numbers and spaces
            # if self.name_entry[self.selection] == 32:
            #     self.name_entry[self.selection] = 90
            # elif self.name_entry[self.selection] == 65:
            #     self.name_entry[self.selection] = 57
            # elif self.name_entry[self.selection] == 48:
            #     self.name_entry[self.selection] = 32
            else:
                self.name_entry[self.selection] = self.name_entry[self.selection] - 1

    def display_scene(self):
        if self.slide:
            self.slide.play_slide()
        else:
            self.render = self.scene.display_win(self.last_game_record, self.selection, self.name_entry, self.scene.last_game_state)
    
    def handle_goto_main(self):
        if self.render and not self.slide:
            self.slide = SlideTrasition(self.scene, self.nav_methods["main_menu"], self.render, "Main Menu")
            self.leaderboard.update_leaderboard(self.last_game_record,chr(self.name_entry[0])+chr(self.name_entry[1])+chr(self.name_entry[2]), self.scene.last_game_state)
            self.nav_methods["regenerate_daily_leaderboard"]()

class SlideTrasition():
    def __init__(self, scene, next_nav, curr_scene, next_scene):
        self.state_name = "Transition"
        self.scene = scene
        self.next_nav = next_nav
        self.offset = 0
        self.slide = scene.slide_trasition(curr_scene, next_scene)

    def play_slide(self):
        if self.offset > -settings.DISPLAY_W:
            self.scene.display_slide(self.slide, (self.offset, 0))
            
            self.offset = self.offset - settings.SLIDE_SPEED
        else:
            self.offset = 0
            self.next_nav()
        
    def handle_up(self):
        return None
        
    def handle_down(self):
        return None
        
    def handle_select(self):
        return None
        
    def handle_back(self):
        return None
