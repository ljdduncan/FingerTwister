import pygame    
import settings

pygame.font.init()
#pass in text to display, font size, color of text, and top left position of text (or center)
#e.g. text.render_text("Finger Twister", 80, settings.TEXT_COLOR, (500,250))
#
#text should be called once in intitialization. calling every frame impacts performance.
def render_text(text, size, color, pos, center=False):
    if center:
        font = pygame.font.Font(settings.FONT, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = pos
        return  text_surface, text_rect
    else:    
        font = pygame.font.Font(settings.FONT, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = pos
        return  text_surface, text_rect 