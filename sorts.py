import random


class Sorts:
    def __init__(self):
        self.numbers = [random.randint( 1, 40 ) for _ in range( 15 )]
        self.i = 0
        self.j = 0

        self.swaps_counter = 0

    def reset( self ):
        self.numbers = [random.randint( 1, 40 ) for _ in range( 15 )]
        self.i = 0
        self.j = 0

        self.swaps_counter = 0

    def swap(self, a: int, b: int):
        temp = self.numbers[ a ]
        self.numbers[ a ] = self.numbers[ b ]
        self.numbers[ b ] = temp

        self.swaps_counter += 1

    def bubble_sort( self ):
        if self.i < len( self.numbers ):
            if self.j < len( self.numbers ) - 1:
                if self.numbers[ self.j ] > self.numbers[ self.j + 1 ]:
                    self.swap( self.j, self.j + 1 )

                self.j += 1
            else:
                self.j = 0
                self.i += 1

    def insertion_sort( self ):
        if self.i < len( self.numbers ):
            key = self.numbers[ self.i ]

            j = self.i - 1
            while j >= 0 and key < self.numbers[ j ]:
                self.numbers[ j + 1 ] = self.numbers[ j ]
                j -= 1

            self.numbers[ j + 1 ] = key
            self.i += 1

    def selection_sort(self):
        if self.i < len( self.numbers ):

            min_index = self.i
            for j in range( self.i + 1, len( self.numbers ) ):
                if self.numbers[ min_index ] > self.numbers[ j ]:
                    min_index = j

            self.swap( self.i, min_index )

            self.i += 1
