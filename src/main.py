import pygame
import settings
import buttons
import controller

from leaderboard import Leaderboard as Leaderboard_JSON
from state import *
from scene import *

settings.DISPLAY_W = 1920
settings.DISPLAY_H = 1080

buttons = buttons.Buttons()

def main_loop():
    leaderboard = Leaderboard_JSON()
    daily_leaderboard = Leaderboard_JSON(leaderboard.get_daily_leaderboard())
    state = State(window, leaderboard, daily_leaderboard)
    time = int(datetime.datetime.now().timestamp()) #It's 9pm on a fucking friday. Wake the fuck up, we're going to Hï.
    last_input = 9999999999999999999999999
    date = datetime.datetime.now().date()
    minute = datetime.datetime.now().minute
    while True:
        altered_states = controller.control_buttons(buttons.game_buttons, buttons.led_mapping, buttons.switch_mapping)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit
                    case pygame.K_UP:
                        last_input = int(datetime.datetime.now().timestamp())
                        state.handle_up()
                    case pygame.K_DOWN:
                        last_input = int(datetime.datetime.now().timestamp())
                        state.handle_down()
                    case pygame.K_RIGHT:
                        last_input = int(datetime.datetime.now().timestamp())
                        if state.current_state.state_name == "Main":
                            buttons.set_non_game_state()
                        state.handle_select()
                    case pygame.K_LEFT:
                        last_input = int(datetime.datetime.now().timestamp())
                        state.handle_back()

        if state.current_state.state_name == "Game":
            last_input = int(datetime.datetime.now().timestamp())
            return_message = state.detect_presses(altered_states)

            #false if next button is not pressed. message will contain the next button in return_message[0] and light it up
            if return_message[1] == False:
                try:
                    buttons.game_buttons[return_message[0]].LED_state = 1
                except:
                    pass
            #true if game was ended
            else:
                buttons.set_non_game_state()
                state.last_game_record = int(return_message[0].split(":")[1])
                if state.last_game_record >= 10:
                    state.handle_win(return_message)
                else:
                    state.handle_loss(return_message)

        if state.current_state.state_name == "Main" and state.current_state.slide == None:
            if datetime.datetime.now().date() != date:
                date = datetime.datetime.now().date()
                daily_leaderboard = Leaderboard_JSON(leaderboard.get_daily_leaderboard())
                state.regenerateDailyLeaderboard()
                print("Daily leaderboard reset")
           
            
            if time != int(datetime.datetime.now().timestamp()):
                time = int(datetime.datetime.now().timestamp())
                buttons.pulse_wave()

        if state.current_state.state_name != "Main" and state.current_state.state_name != "Game":
            buttons.set_non_game_state()
            if state.current_state.state_name == "Win" and (int(datetime.datetime.now().timestamp()) - last_input) >= 180:
                state.handle_goto_main()
            if state.current_state.state_name != "Win" and (int(datetime.datetime.now().timestamp()) - last_input) >= 60:
                state.handle_goto_main()
                

            
        state.display_scene()
        
        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)
        #updates the screen, called last
        #TODO might need to do delta_time calc at some point
        pygame.display.update()



if __name__ == "__main__":
    #Set up
    window = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN, vsync=1)
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    buttons.set_non_game_state()
    controller.control_buttons(buttons.game_buttons, buttons.led_mapping, buttons.switch_mapping)

    #run the game
    main_loop()