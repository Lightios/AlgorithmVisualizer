import pygame as pg

import sorts

WIDTH = 800
HEIGHT = 600


class Main:
    def __init__( self ):
        pg.init()
        self.screen = pg.display.set_mode( (WIDTH, HEIGHT) )

        self.running = True

        self.FPS = 5
        self.clock = pg.time.Clock()
        self.clock.tick( self.FPS )

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

    def display( self ):
        self.screen.fill( (0, 0, 0) )

        for index in range( len( self.sorts.numbers ) ):
            self.draw_rectangle( index )

        pg.display.flip()
        self.clock.tick_busy_loop( self.FPS )


if __name__ == '__main__':
    Main()
