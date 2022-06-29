import pygame as pg
from consts import *


class Button:
    def __init__( self, main, sort_type: str, x: int, y: int ):
        self.main = main
        self.type = sort_type
        self.image = self.main.font.render( sort_type, False, WHITE, BLACK )
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def check_press( self, mouse_pos: tuple ):
        if self.rect.x < mouse_pos[ 0 ] < self.rect.x + self.rect.width and self.rect.y < mouse_pos[ 1 ] < self.rect.y + self.rect.height:
            self.main.current_sorting = self.type
            self.main.sorts.reset()
