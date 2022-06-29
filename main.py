import pygame as pg

import sorts
import buttons
from consts import *


class Main:
    def __init__( self ):
        pg.init()
        self.screen = pg.display.set_mode( (WIDTH, HEIGHT) )

        self.running = True

        self.FPS = 60
        self.clock = pg.time.Clock()
        self.clock.tick( self.FPS )
        self.delay_counter = 0

        self.font = pg.font.Font('Arial.otf', 32)
        self.text = self.font.render( 'Swaps: 0', False, WHITE, BLACK )

        self.buttons = {}
        self.buttons[ "bubble" ] = buttons.Button( self, "bubble", 20, HEIGHT - 40 )
        self.buttons[ "insertion" ] = buttons.Button( self, "insertion", 200, HEIGHT - 40 )
        self.buttons[ "selection" ] = buttons.Button( self, "selection", 400, HEIGHT - 40 )

        self.current_sorting = "bubble"

        self.sorts = sorts.Sorts()
        self.mainloop()

    def mainloop( self ):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                if event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    for button in self.buttons.values():
                        button.check_press( pos )

            self.update()
            self.display()

    def draw_rectangle( self, index: int ):
        height = 8 * self.sorts.numbers[ index ]

        pg.draw.rect( self.screen, CYAN, (20 + 50 * index, HEIGHT - 80 - height, 20, height) )

    def update( self ):
        self.delay_counter = (self.delay_counter + 1) % self.FPS

        if self.delay_counter == 0:
            if self.current_sorting == "bubble":
                self.sorts.bubble_sort()
            elif self.current_sorting == "insertion":
                self.sorts.insertion_sort()
            elif self.current_sorting == "selection":
                self.sorts.selection_sort()

        self.text = self.font.render( f'Swaps: {self.sorts.swaps_counter}', False, WHITE, BLACK )

    def display( self ):
        self.screen.fill( BLACK )

        for index in range( len( self.sorts.numbers ) ):
            self.draw_rectangle( index )

        self.screen.blit( self.text, self.text.get_rect() )

        for button in self.buttons.values():
            self.screen.blit( button.image, button.rect )

        pg.display.flip()
        self.clock.tick_busy_loop( self.FPS )


if __name__ == '__main__':
    Main()
