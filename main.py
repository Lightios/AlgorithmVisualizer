import pygame as pg

import sorts
from consts import *


class Main:
    def __init__( self ):
        pg.init()
        self.screen = pg.display.set_mode( (WIDTH, HEIGHT) )

        self.running = True

        self.FPS = 5
        self.clock = pg.time.Clock()
        self.clock.tick( self.FPS )

        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render( 'Swaps: 0', False, WHITE, BLACK )

        self.sorts = sorts.Sorts()
        self.mainloop()

    def mainloop( self ):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.update()
            self.display()

    def draw_rectangle( self, index: int ):
        height = 20 * self.sorts.numbers[ index ]

        pg.draw.rect( self.screen, (0, 0, 255), (20 + 50 * index, HEIGHT - 50 - height, 20, height) )

    def update( self ):
        # self.bubble_sort()
        # self.insertion_sort()
        self.sorts.selection_sort()

        self.text = self.font.render( f'Swaps: {self.sorts.swaps_counter}', False, WHITE, BLACK )

    def display( self ):
        self.screen.fill( (0, 0, 0) )

        for index in range( len( self.sorts.numbers ) ):
            self.draw_rectangle( index )

        self.screen.blit( self.text, self.text.get_rect() )

        pg.display.flip()
        self.clock.tick_busy_loop( self.FPS )


if __name__ == '__main__':
    Main()
