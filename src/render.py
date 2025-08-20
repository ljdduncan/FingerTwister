import text
import settings
import pygame
import settings
import graphics
import leaderboard

# Control items
controls_position = (0, 800)

select_control = pygame.Surface((300, 120), pygame.SRCALPHA)
select_control.blit(graphics.sprites["large_white"], (0, 0)) #right
select_text = text.render_text("Select", 50, settings.TEXT_COLOR, (120,30))
select_control.blit(select_text[0], select_text[1])

select_control_muted = pygame.Surface((300, 120), pygame.SRCALPHA)
select_control_muted.blit(graphics.sprites["large_white_muted"], (0, 0)) #right

select_control_cats = pygame.Surface((300, 120), pygame.SRCALPHA)
select_control_cats.blit(graphics.sprites["large_white"], (0, 0)) #right
select_text_cats = text.render_text("Cats", 50, settings.TEXT_COLOR, (120,30))
select_control_cats.blit(select_text_cats[0], select_text_cats[1])

select_control_play_again = pygame.Surface((350, 120), pygame.SRCALPHA)
select_control_play_again.blit(graphics.sprites["large_white"], (0, 0)) #right
select_text_play_again = text.render_text("Play Again", 50, settings.TEXT_COLOR, (120,30))
select_control_play_again.blit(select_text_play_again[0], select_text_play_again[1])

select_control_confirm = pygame.Surface((300, 120), pygame.SRCALPHA)
select_control_confirm.blit(graphics.sprites["large_white"], (0, 0)) #right
select_text_confirm = text.render_text("Confirm", 50, settings.TEXT_COLOR, (120,30))
select_control_confirm.blit(select_text_confirm[0], select_text_confirm[1])

select_control_daily = pygame.Surface((600, 120), pygame.SRCALPHA)
select_control_daily.blit(graphics.sprites["large_white"], (0, 0)) #right
select_text_daily = text.render_text("All-Time Leaderboard", 50, settings.TEXT_COLOR, (120,30))
select_control_daily.blit(select_text_daily[0], select_text_daily[1])

select_control_all_time = pygame.Surface((600, 120), pygame.SRCALPHA)
select_control_all_time.blit(graphics.sprites["large_white"], (0, 0)) #right
select_text_all_time = text.render_text("Daily Leaderboard", 50, settings.TEXT_COLOR, (120,30))
select_control_all_time.blit(select_text_all_time[0], select_text_all_time[1])

select_position = (330, 90)


back_control = pygame.Surface((400, 120), pygame.SRCALPHA)
back_control.blit(graphics.sprites["large_white"], (110, 0)) #left
back_text = text.render_text("Back", 50, settings.TEXT_COLOR, (0,30))
back_control.blit(back_text[0], back_text[1])

back_control_muted = pygame.Surface((400, 120), pygame.SRCALPHA)
back_control_muted.blit(graphics.sprites["large_white_muted"], (110, 0)) #left

back_position = (20, 90)


up_control = pygame.Surface((300, 220), pygame.SRCALPHA)
up_control.blit(graphics.sprites["large_white"], (0, 40)) #left
up_text = text.render_text("Up", 50, settings.TEXT_COLOR, (32,0))
up_control.blit(up_text[0], up_text[1])

up_control_muted = pygame.Surface((300, 220), pygame.SRCALPHA)
up_control_muted.blit(graphics.sprites["large_white_muted"], (0, 40)) #left

up_position = (230, 0)


down_control = pygame.Surface((300, 220), pygame.SRCALPHA)
down_control.blit(graphics.sprites["large_white"], (0, 0)) #left
down_text = text.render_text("Down", 50, settings.TEXT_COLOR, (10,90))
down_control.blit(down_text[0], down_text[1])

down_control_muted = pygame.Surface((300, 220), pygame.SRCALPHA)
down_control_muted.blit(graphics.sprites["large_white_muted"], (0, 0)) #left

down_position = (230, 140)

play_again_position = (225, 480)

# Main Menu items
mm_header = text.render_text("Finger Twister", 120, settings.TEXT_COLOR, (settings.DISPLAY_W/2,250), True)
mm_play_option = text.render_text("Play", 80, settings.TEXT_COLOR, (500,400))
mm_more_games_option = text.render_text("Memory Game", 80, settings.TEXT_COLOR, (500,500))
mm_leaderboard_option = text.render_text("Leaderboard", 80, settings.TEXT_COLOR, (500,600))
# mm_more_games_option = text.render_text("More Game Modes", 80, settings.TEXT_COLOR, (500,600))
mm_credits_option = text.render_text("Credits", 80, settings.TEXT_COLOR, (500,700))
mm_cursor = text.render_text("->", 80, settings.TEXT_COLOR, (400,400))

mm_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
mm_controls.blit(select_control, select_position)
mm_controls.blit(back_control_muted, back_position)
mm_controls.blit(up_control, up_position)
mm_controls.blit(down_control, down_position)

# More Game Modes items
more_games_header = text.render_text("More Game Modes", 120, settings.TEXT_COLOR, (settings.DISPLAY_W/2,250), True)
more_games_memory_option = text.render_text("Memory Game", 80, settings.TEXT_COLOR, (500,400))
more_games_asdf_option = text.render_text("asdf", 80, settings.TEXT_COLOR, (500,500))
more_games_asdf2_option = text.render_text("asdf2", 80, settings.TEXT_COLOR, (500,600))
more_games_cursor = text.render_text("->", 80, settings.TEXT_COLOR, (400,400))

more_games_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
more_games_controls.blit(select_control, select_position)
more_games_controls.blit(back_control, back_position)
more_games_controls.blit(up_control, up_position)
more_games_controls.blit(down_control, down_position)

# Credits items
c_header = text.render_text("Credits", 80, settings.TEXT_COLOR, (settings.DISPLAY_W/2, 190), True)
c_designer = text.render_text("Designed by: Lucas Duncan", 80, settings.TEXT_COLOR, (settings.DISPLAY_W/2,340), True)
c_builder = text.render_text("Built by: Bryan Higgins", 80, settings.TEXT_COLOR, (settings.DISPLAY_W/2,440), True)
c_more = text.render_text("Additional Help from: Michael Ackerman", 80, settings.TEXT_COLOR, (settings.DISPLAY_W/2,540), True)
c_more_2 = text.render_text("Nathan Borak, Gerard Puhalla", 80, settings.TEXT_COLOR, (settings.DISPLAY_W/2,640), True)
c_more_3 = text.render_text("Timothy Roy Sundberg, Casey Woodford", 80, settings.TEXT_COLOR, (settings.DISPLAY_W/2,740), True)

credits_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
credits_controls.blit(select_control_cats, select_position)
credits_controls.blit(back_control, back_position)
credits_controls.blit(up_control_muted, up_position)
credits_controls.blit(down_control_muted, down_position)

# Cats items
lane_text = text.render_text("Lane", 80, settings.TEXT_COLOR, (80, 465))
weeb_text = text.render_text("Weeb", 80, settings.TEXT_COLOR, (1630, 530))
kevin_text = text.render_text("Kevin", 80, settings.TEXT_COLOR, (350, 530))
om_text = text.render_text("Onyx & Maisie", 80, settings.TEXT_COLOR, (1360, 465))
egg_text = text.render_text("Egg", 80, settings.TEXT_COLOR, (1080, 950))
fia_text = text.render_text("Fia", 80, settings.TEXT_COLOR, (740, 235))

cats_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
cats_controls.blit(select_control_muted, select_position)
cats_controls.blit(back_control, back_position)
cats_controls.blit(up_control_muted, up_position)
cats_controls.blit(down_control_muted, down_position)

# Game items
game_instructions_text_header = text.render_text("How to play", 120, settings.TEXT_COLOR, (50, 50))
game_instructions_text_1 = text.render_text("When a button lights up, press it", 60, settings.TEXT_COLOR, (50, 200))
game_instructions_text_2 = text.render_text("If you press the wrong button, you lose", 60, settings.TEXT_COLOR, (50, 300))
game_instructions_text_3 = text.render_text("If you let go of a button, you lose", 60, settings.TEXT_COLOR, (50, 400))
game_instructions_text_4 = text.render_text("See how many you can press at once!", 60, settings.TEXT_COLOR, (50, 500))
game_instructions_text_5 = text.render_text("No feet!", 80, settings.TEXT_COLOR, (300, 620))


button_flash = pygame.Surface(graphics.button_flash_size, pygame.SRCALPHA)
button_flash.blit(graphics.button_flash, (0,0))
button_flash_fail = pygame.Surface(graphics.button_flash_size, pygame.SRCALPHA)
button_flash_fail.blit(graphics.button_flash_fail, (0,0))

game_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
game_controls.blit(select_control_muted, select_position)
game_controls.blit(back_control, back_position)
game_controls.blit(up_control_muted, up_position)
game_controls.blit(down_control_muted, down_position)

# Memory game items
memory_game_instructions_text_header = text.render_text("How to play", 120, settings.TEXT_COLOR, (50, 50))
memory_game_instructions_text_1 = text.render_text("Test your memory!", 60, settings.TEXT_COLOR, (50, 200))
memory_game_instructions_text_2 = text.render_text("Buttons light up in order", 60, settings.TEXT_COLOR, (50, 300))
memory_game_instructions_text_3 = text.render_text("Press the buttons in that same order", 60, settings.TEXT_COLOR, (50, 400))
memory_game_instructions_text_4 = text.render_text("No need to keep holding them down!", 60, settings.TEXT_COLOR, (50, 500))

#Leaderboard items
leaderboard_header = text.render_text("All-Time Leaderboard", 120, settings.TEXT_COLOR, (settings.DISPLAY_W/2,50), True)
daily_leaderboard_header = text.render_text("Daily Leaderboard", 120, settings.TEXT_COLOR, (settings.DISPLAY_W/2,50), True)
leaderboard_name_text = text.render_text("Name", 80, settings.TEXT_COLOR, (600,150))
leaderboard_score_text = text.render_text("Score", 80, settings.TEXT_COLOR, (800,150))
leaderboard_cursor = text.render_text("->", 80, settings.TEXT_COLOR, (450,240))
leaderboard_empty = text.render_text("Empty! :)", 80, settings.TEXT_COLOR, (settings.DISPLAY_W/2,250), True)

leaderboard_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
leaderboard_controls.blit(select_control_all_time, select_position)
leaderboard_controls.blit(back_control, back_position)
leaderboard_controls.blit(up_control, up_position)
leaderboard_controls.blit(down_control, down_position)

daily_leaderboard_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
daily_leaderboard_controls.blit(select_control_daily, select_position)
daily_leaderboard_controls.blit(back_control, back_position)
daily_leaderboard_controls.blit(up_control, up_position)
daily_leaderboard_controls.blit(down_control, down_position)

# Postgame items
loss_text = text.render_text("You lose!", 120, settings.TEXT_COLOR, (300, 190))
win_text = text.render_text("You win!", 120, settings.TEXT_COLOR, (300, 190))

loss_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
loss_controls.blit(select_control_play_again, select_position)
loss_controls.blit(back_control, back_position)
loss_controls.blit(up_control_muted, up_position)
loss_controls.blit(down_control_muted, down_position)

win_controls = pygame.Surface((1500, 1500), pygame.SRCALPHA)
win_controls.blit(select_control_confirm, select_position)
win_controls.blit(back_control, back_position)
win_controls.blit(up_control, up_position)
win_controls.blit(down_control, down_position)


initials_control = pygame.Surface((150, 120), pygame.SRCALPHA)
initials_control.blit(graphics.sprites["small_white"], (00, 20)) #left
initials_control.blit(graphics.sprites["small_white"], (40, 00)) #top
initials_control.blit(graphics.sprites["small_white"], (40, 40)) #bottom
initials_control.blit(graphics.sprites["small_white"], (80, 20)) #right
initials_text = text.render_text("Enter name", 30, settings.TEXT_COLOR, (0,80))
initials_control.blit(initials_text[0], initials_text[1])
initials_position = (160, 940)

initials_control_muted_right = pygame.Surface((150, 120), pygame.SRCALPHA)
initials_control_muted_right.blit(initials_control, (0,0))
initials_control_muted_right.blit(graphics.sprites["small_white_muted"], (80, 20)) #right

initials_up_cursor = text.render_text("^", 80, settings.TEXT_COLOR, (390,440))
initials_down_cursor = text.render_text("^", 80, settings.TEXT_COLOR, (390,566))
initials_down_cursor = (pygame.transform.flip(initials_down_cursor[0], False, True), initials_down_cursor[1])


def render_main_menu(selection, timer_buttons):
    main_menu_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    main_menu_surface.fill(settings.BACKGROUND_COLOR)
    main_menu_surface.blit(mm_header[0], mm_header[1])
    main_menu_surface.blit(mm_play_option[0], mm_play_option[1])
    main_menu_surface.blit(mm_leaderboard_option[0], mm_leaderboard_option[1])
    main_menu_surface.blit(mm_more_games_option[0], mm_more_games_option[1])
    main_menu_surface.blit(mm_credits_option[0], mm_credits_option[1])
    main_menu_surface.blit(mm_controls, controls_position)

    for deco_button in timer_buttons:
        if not deco_button[2]:
            main_menu_surface.blit(graphics.sprites[deco_button[1]], (200 * deco_button[0] - 100, 50))
        else:
            main_menu_surface.blit(graphics.sprites[deco_button[1] + "_pressed"], (200 * deco_button[0] - 100, 50))

    match selection:
        case "Play":
            main_menu_surface.blit(mm_cursor[0], mm_cursor[1])
        case "Memory Game":
            main_menu_surface.blit(mm_cursor[0], (mm_cursor[1][0], mm_cursor[1][1] + 100)) #disgusting calc. essentially just modifies the position tuple to offset it
        case "Leaderboard":
            main_menu_surface.blit(mm_cursor[0], (mm_cursor[1][0], mm_cursor[1][1] + 200))
        case "Credits":
            main_menu_surface.blit(mm_cursor[0], (mm_cursor[1][0], mm_cursor[1][1] + 300))
    return main_menu_surface

def render_more_games(selection, buttons):
    more_games_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    more_games_surface.fill(settings.BACKGROUND_COLOR)
    more_games_surface.blit(more_games_header[0], more_games_header[1])
    more_games_surface.blit(more_games_memory_option[0], more_games_memory_option[1])
    more_games_surface.blit(more_games_asdf_option[0], more_games_asdf_option[1])
    more_games_surface.blit(more_games_asdf2_option[0], more_games_asdf2_option[1])
    more_games_surface.blit(more_games_controls, controls_position)

    for deco_button in buttons:
        if not deco_button[2]:
            more_games_surface.blit(graphics.sprites[deco_button[1]], (200 * deco_button[0] - 100, 50))
        else:
            more_games_surface.blit(graphics.sprites[deco_button[1] + "_pressed"], (200 * deco_button[0] - 100, 50))

    match selection:
        case "Memory Game":
            more_games_surface.blit(more_games_cursor[0], more_games_cursor[1])
        case "asdf":
            more_games_surface.blit(more_games_cursor[0], (more_games_cursor[1][0], more_games_cursor[1][1] + 100)) #disgusting calc. essentially just modifies the position tuple to offset it
        case "asdf2":
            more_games_surface.blit(more_games_cursor[0], (more_games_cursor[1][0], more_games_cursor[1][1] + 200))
    return more_games_surface


def render_credits():
    credits_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    credits_surface.fill(settings.BACKGROUND_COLOR)
    credits_surface.blit(c_header[0], c_header[1])
    credits_surface.blit(c_designer[0], c_designer[1])
    credits_surface.blit(c_builder[0], c_builder[1])
    credits_surface.blit(c_more[0], c_more[1])
    credits_surface.blit(c_more_2[0], c_more_2[1])
    credits_surface.blit(c_more_3[0], c_more_3[1])
    credits_surface.blit(credits_controls, controls_position)
    return credits_surface

def render_cats():
    cats_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    cats_surface.fill(settings.BACKGROUND_COLOR)
    cats_surface.blit(cats_controls, (700, 10))

    cats_surface.blit(lane_text[0], lane_text[1])
    cats_surface.blit(graphics.cats["lane"], (0, 0))

    cats_surface.blit(weeb_text[0], weeb_text[1])
    cats_surface.blit(graphics.cats["weeb"], (1280, 600))

    cats_surface.blit(kevin_text[0], kevin_text[1])
    cats_surface.blit(graphics.cats["kevin"], (0, 600))

    cats_surface.blit(om_text[0], om_text[1])
    cats_surface.blit(graphics.cats["onyxmaisie"], (1280, 0))

    cats_surface.blit(egg_text[0], egg_text[1])
    cats_surface.blit(fia_text[0], fia_text[1])
    cats_surface.blit(graphics.cats["eggfia"], (640, 320))
    
    return cats_surface

def render_game(display_buttons_state):
    game_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    game_surface.fill(settings.BACKGROUND_COLOR)
    game_surface.blit(game_controls, controls_position)
    game_surface.blit(game_instructions_text_header[0], game_instructions_text_header[1])
    game_surface.blit(game_instructions_text_1[0], game_instructions_text_1[1])
    game_surface.blit(game_instructions_text_2[0], game_instructions_text_2[1])
    game_surface.blit(game_instructions_text_3[0], game_instructions_text_3[1])
    game_surface.blit(game_instructions_text_4[0], game_instructions_text_4[1])
    game_surface.blit(game_instructions_text_5[0], game_instructions_text_5[1])
    
    for index, button in enumerate(display_buttons_state):
        button_color = _get_button_color(index, button)
        button_position = _get_button_position(index)
        game_surface.blit(button_color, button_position)
        if button == (0,1):
            game_surface.blit(button_flash, (button_position[0]-30, button_position[1]))

    return game_surface

def render_memory_game(current_score, display_buttons_state):
    memory_game_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    memory_game_surface.fill(settings.BACKGROUND_COLOR)
    memory_game_surface.blit(game_controls, controls_position)
    memory_game_surface.blit(memory_game_instructions_text_header[0], memory_game_instructions_text_header[1])
    memory_game_surface.blit(memory_game_instructions_text_1[0], memory_game_instructions_text_1[1])
    memory_game_surface.blit(memory_game_instructions_text_2[0], memory_game_instructions_text_2[1])
    memory_game_surface.blit(memory_game_instructions_text_3[0], memory_game_instructions_text_3[1])
    memory_game_surface.blit(memory_game_instructions_text_4[0], memory_game_instructions_text_4[1])
    
    memory_game_score_text = text.render_text("Score: "+ str(current_score), 80, settings.TEXT_COLOR, (300, 620))
    memory_game_surface.blit(memory_game_score_text[0],memory_game_score_text[1])

    for index, button in enumerate(display_buttons_state):
        button_color = _get_button_color(index, button)
        button_position = _get_button_position(index)
        memory_game_surface.blit(button_color, button_position)
        if button == (0,1):
            memory_game_surface.blit(button_flash, (button_position[0]-30, button_position[1]))

    return memory_game_surface


def render_leaderboard(selection, leaderboard):
    leaderboard_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    leaderboard_surface.fill(settings.BACKGROUND_COLOR)
    leaderboard_surface.blit(leaderboard_header[0], leaderboard_header[1])
    leaderboard_surface.blit(leaderboard_controls, controls_position)
    if leaderboard.get_position(selection):
        for index in range(leaderboard.length):
            if index == 9:
                break
            leaderboard_entry = leaderboard.get_position(index)
            leaderboard_entry_pos = text.render_text(str(index + 1) + "." , 60, settings.TEXT_COLOR, (540, 250 + 70*index))
            leaderboard_entry_name = text.render_text(leaderboard_entry['name'] , 60, settings.TEXT_COLOR, (600, 250 + 70*index))
            leaderboard_entry_score = text.render_text(str(leaderboard_entry['score']) , 60, settings.TEXT_COLOR, (800, 250 + 70*index))
            leaderboard_surface.blit(leaderboard_entry_pos[0], leaderboard_entry_pos[1])
            leaderboard_surface.blit(leaderboard_entry_name[0], leaderboard_entry_name[1])
            leaderboard_surface.blit(leaderboard_entry_score[0], leaderboard_entry_score[1])
        
    
    
        leaderboard_surface.blit(leaderboard_name_text[0], leaderboard_name_text[1])
        leaderboard_surface.blit(leaderboard_score_text[0], leaderboard_score_text[1])

        leaderboard_surface.blit(leaderboard_cursor[0], (leaderboard_cursor[1][0], leaderboard_cursor[1][1] + (70 * selection)))
    
        for index, button in enumerate(leaderboard.get_position(selection)['state']["buttons"]):
            button_color = _get_button_color(index, button)
            button_position = _get_button_position(index)
            leaderboard_surface.blit(button_color, button_position)
            if button == (0,1):
                leaderboard_surface.blit(button_flash, (button_position[0]-30, button_position[1]))
            if index == leaderboard.get_position(selection)['state']["altered"] - 1:
                leaderboard_surface.blit(button_flash_fail, (button_position[0]-30, button_position[1]))
    else:
        leaderboard_surface.blit(leaderboard_empty[0],leaderboard_empty[1])
    
    return leaderboard_surface


def render_daily_leaderboard(selection, leaderboard):
    leaderboard_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    leaderboard_surface.fill(settings.BACKGROUND_COLOR)
    leaderboard_surface.blit(daily_leaderboard_header[0], daily_leaderboard_header[1])
    leaderboard_surface.blit(daily_leaderboard_controls, controls_position)
    if leaderboard.get_position(selection):
        for index in range(leaderboard.length):
            if index == 9:
                break
            leaderboard_entry = leaderboard.get_position(index)
            leaderboard_entry_pos = text.render_text(str(index + 1) + "." , 60, settings.TEXT_COLOR, (540, 250 + 70*index))
            leaderboard_entry_name = text.render_text(leaderboard_entry['name'] , 60, settings.TEXT_COLOR, (600, 250 + 70*index))
            leaderboard_entry_score = text.render_text(str(leaderboard_entry['score']) , 60, settings.TEXT_COLOR, (800, 250 + 70*index))
            leaderboard_surface.blit(leaderboard_entry_pos[0], leaderboard_entry_pos[1])
            leaderboard_surface.blit(leaderboard_entry_name[0], leaderboard_entry_name[1])
            leaderboard_surface.blit(leaderboard_entry_score[0], leaderboard_entry_score[1])
        
    
    
        leaderboard_surface.blit(leaderboard_name_text[0], leaderboard_name_text[1])
        leaderboard_surface.blit(leaderboard_score_text[0], leaderboard_score_text[1])

        leaderboard_surface.blit(leaderboard_cursor[0], (leaderboard_cursor[1][0], leaderboard_cursor[1][1] + (70 * selection)))
    
        for index, button in enumerate(leaderboard.get_position(selection)['state']["buttons"]):
            button_color = _get_button_color(index, button)
            button_position = _get_button_position(index)
            leaderboard_surface.blit(button_color, button_position)
            if button == (0,1):
                leaderboard_surface.blit(button_flash, (button_position[0]-30, button_position[1]))
            if index == leaderboard.get_position(selection)['state']["altered"] - 1:
                leaderboard_surface.blit(button_flash_fail, (button_position[0]-30, button_position[1]))
    else:
        leaderboard_surface.blit(leaderboard_empty[0],leaderboard_empty[1])
    
    return leaderboard_surface

def render_loss(last_game_record, last_game_state):
    last_game_record_text = text.render_text("Score: "+ str(last_game_record), 80, settings.TEXT_COLOR, (390, 320))
    loss_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    loss_surface.fill(settings.BACKGROUND_COLOR)
    loss_surface.blit(loss_controls, play_again_position)

    
    loss_surface.blit(loss_text[0], loss_text[1])
    loss_surface.blit(last_game_record_text[0], last_game_record_text[1])
    
    for index, button in enumerate(last_game_state["buttons"]):
        button_color = _get_button_color(index, button)
        button_position = _get_button_position(index)
        loss_surface.blit(button_color, button_position)
        if button == (0,1):
            loss_surface.blit(button_flash, (button_position[0]-30, button_position[1]))
        if index == last_game_state["altered"] - 1:
            loss_surface.blit(button_flash_fail, (button_position[0]-30, button_position[1]))


    return loss_surface


def render_win(last_game_record, selection, name_entry, last_game_state):
    last_game_record_text = text.render_text("Score: "+ str(last_game_record), 80, settings.TEXT_COLOR, (370, 320))
    initials_0 = text.render_text(str(chr(name_entry[0])), 80, settings.TEXT_COLOR, (390, 500))
    initials_1 = text.render_text(str(chr(name_entry[1])), 80, settings.TEXT_COLOR, (470, 500))
    initials_2 = text.render_text(str(chr(name_entry[2])), 80, settings.TEXT_COLOR, (550, 500))
    win_surface = pygame.Surface((settings.DISPLAY_W, settings.DISPLAY_H))
    win_surface.fill(settings.BACKGROUND_COLOR)
    
    win_surface.blit(win_controls,controls_position)

    win_surface.blit(win_text[0], win_text[1])
    win_surface.blit(last_game_record_text[0], last_game_record_text[1])
    win_surface.blit(initials_0[0], initials_0[1])
    win_surface.blit(initials_1[0], initials_1[1])
    win_surface.blit(initials_2[0], initials_2[1])

    win_surface.blit(initials_up_cursor[0], (initials_up_cursor[1][0] + (80 * selection), initials_up_cursor[1][1]))
    win_surface.blit(initials_down_cursor[0], (initials_down_cursor[1][0] + (80 * selection), initials_down_cursor[1][1]))
    
    for index, button in enumerate(last_game_state["buttons"]):
        button_color = _get_button_color(index, button)
        button_position = _get_button_position(index)
        win_surface.blit(button_color, button_position)
        if button == (0,1):
            win_surface.blit(button_flash, (button_position[0]-30, button_position[1]))
        if index == last_game_state["altered"] - 1:
            win_surface.blit(button_flash_fail, (button_position[0]-30, button_position[1]))



    return win_surface

def _get_button_position(index):
    return ((index%6)*150 + 1000, int(index/6)*150 + 100)

def _get_button_color(index, button):
    button_string = ""
    if index in [0, 4, 9, 14, 19, 23, 24, 28, 33]:
        button_string = button_string + "large_blue"
    elif index in [1, 5, 6, 10, 15, 20, 25, 29, 30, 34]:
        button_string = button_string + "large_red"
    elif index in [2, 7, 11, 12, 16, 21, 26, 31, 35]:
        button_string = button_string + "large_yellow"
    else:
        button_string = button_string + "large_green"

    if button[0] == 1:
        button_string = button_string + "_pressed"

    if button[1] == 0:
        button_string = button_string + "_muted"
        

    return graphics.sprites[button_string]
    

def render_slide(curr_scene, next_scene):
    slide = pygame.Surface((settings.DISPLAY_W * 2, settings.DISPLAY_H))
    slide.blit(curr_scene, (0, 0))
    slide.blit(next_scene, (1920, 0)) #next to the current page
    return slide

