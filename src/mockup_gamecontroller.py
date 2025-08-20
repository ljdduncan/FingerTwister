import time, random, sys
from buttons import blist, ButtonState
from utils import refresh_registers

if __name__ == "__main__":
    print(f"Good luck soldier!")

    refresh_registers()

    need_pressed = []
    buttonlist = blist
    max_buttonpresses = 6
    max_timeout = 10
    cur_buttonpresses = 0
    while True:
        # Begin main game loop
        # Select button to press
        # ind = random.randint(0, (len(buttonlist)-1))
        if len(buttonlist) == 0:
            print(f"You won!")
            sys.exit(1)
        ind = random.randint(0, 1)
        # add timeout here
        timeout = 0
        refresh_registers()
        print(f"Current state of new button is {buttonlist[ind].state()}")
        print(f"Current state of register list is {reglist}")
        print(f"Please press and hold {buttonlist[ind].name}")
        while (buttonlist[ind].state() == ButtonState.NOT_HELD):
            refresh_registers()
            # recalc timeout. If timeout exceeds end the game
            #timeout = timeout + 1
            #if timeout > 10:
            #    sys.exit(1)
            # Check that all other buttons are still pressed
            for b in need_pressed:
                if b.state() == ButtonState.NOT_HELD:
                    print(f"Exiting because a button was let go")
                    sys.exit(1)
        # Add button to list of all that must be kept held down
        need_pressed.append(buttonlist[ind])
        # Remove from pool of possible buttons to select
        buttonlist.pop(ind)
        # At this point our button is pressed, all other buttons have been held down until this point, and timeout was not reached. We go again
        cur_buttonpresses += 1
        # also end the game if we've reach some arbitrary limit
        #if cur_buttonpresses > max_buttonpresses:
        #    sys.exit(1)
        



        
            

