import render

class Scene():
    def __init__(self, window, leaderboard, daily_leaderboard):
        self.window = window
        self.last_game_record = 0
        self.timer_buttons = [[1, "large_red", False], [2, "large_blue", False],[3, "large_green", False],[4, "large_yellow", False],[5, "large_red", False],[6, "large_blue", False],[7, "large_green", False],[8, "large_yellow", False],[9, "large_red", False]]
        self.leaderboard = leaderboard
        self.daily_leaderboard = daily_leaderboard
        self.last_game_state = {}
        self.game_mode = "Game"

    def display_main_menu(self, selection, timer_buttons):
        main_surface = render.render_main_menu(selection, timer_buttons)
        self.window.blit(main_surface, (0,0))
        return main_surface

    def display_more_games(self, selection):
        more_games_surface = render.render_more_games(selection, self.timer_buttons)
        self.window.blit(more_games_surface, (0,0))
        return more_games_surface

    def display_credits(self):
        credit_surface = render.render_credits()
        self.window.blit(credit_surface, (0, 0))
        return credit_surface

    def display_cats(self):
        cats_surface = render.render_cats()
        self.window.blit(cats_surface, (0, 0))
        return cats_surface
    
    def display_game(self, display_buttons_state):
        game_surface = render.render_game(display_buttons_state)
        self.window.blit(game_surface, (0,0))
        return game_surface

    def display_memory_game(self, current_score, display_buttons_state):
        memory_game_surface = render.render_memory_game(current_score, display_buttons_state)
        self.window.blit(memory_game_surface, (0,0))
        return memory_game_surface

    def display_loss(self, last_game_record, last_game_state):
        self.last_game_record = last_game_record
        self.last_game_state = last_game_state
        loss_surface = render.render_loss(last_game_record,last_game_state)
        self.window.blit(loss_surface, (0, 0))
        return loss_surface

    def display_win(self, last_game_record, selection, name_entry, last_game_state):
        self.last_game_record = last_game_record
        self.last_game_state = last_game_state
        win_surface = render.render_win(last_game_record, selection, name_entry, last_game_state)
        self.window.blit(win_surface, (0, 0))
        return win_surface
    
    def display_leaderboard(self,selection,leaderboard):
        self.leaderboard = leaderboard
        leaderboard_surface = render.render_leaderboard(selection, self.leaderboard)
        self.window.blit(leaderboard_surface, (0,0))
        return leaderboard_surface
    
    def display_daily_leaderboard(self,selection,leaderboard):
        self.daily_leaderboard = leaderboard
        leaderboard_surface = render.render_daily_leaderboard(selection, self.daily_leaderboard)
        self.window.blit(leaderboard_surface, (0,0))
        return leaderboard_surface

    def display_slide(self, slide, offset):
        self.window.blit(slide, offset)

    def slide_trasition(self, curr_render, next_state):
        next_render = self._get_render(next_state)
        return render.render_slide(curr_render, next_render)
    
    # makes a temp render for the slide_transition. discards the render after transition is done
    def _get_render(self, state):
        match state:
            case "Main Menu":
                return render.render_main_menu("Play", self.timer_buttons)
            case "Credits":
                return render.render_credits()
            case "Cats":
                return render.render_cats()
            case "Game":
                return render.render_game([(0,0)]*36)
            case "Leaderboard":
                return render.render_leaderboard(0, self.leaderboard)
            case "Daily Leaderboard":
                return render.render_daily_leaderboard(0, self.daily_leaderboard)
            case "Loss":
                return render.render_loss(self.last_game_record, self.last_game_state)
            case "Win":
                return render.render_win(self.last_game_record, 0, [65, 65, 65], self.last_game_state)
            case "Memory Game":
                return render.render_memory_game(0, [(0,0)]*36)
            case "More Game Modes":
                return render.render_more_games("Memory Game", self.timer_buttons)