""" NONE_PIC means some part of piese have been placed here.
"""
NONE_PIC = '*'

class Tetrimino(object):

    """Describe each tetrimino."""
    title = NONE_PIC
    grids = [[]]
    arr = []
    length = 0

    def __init__(self):
        from operator import sub
        self.arr = []
        for i in range(len(self.grids)):
            arr = []
            for x in range(len(self.grids[i])):
                for y in range(len(self.grids[i][x])):
                    if self.grids[i][x][y] == '1':
                        arr.append((x,y))
            # convert first element as (0,0)
            (dx, dy) = arr[0]
            for i in range(len(arr)):
                arr[i] = tuple(map(sub, arr[i], (dx, dy)))
            self.arr.append(arr)

class TetriminoFactory(object):

    """Generate each tetrimino."""

    @staticmethod
    def make(type):
        """Generate all shape of type.

        :type: ILlNOPTVvWXZ
        :returns: One of Tetrimino

        """
        if (type == 'I'):
            return I()
        elif (type == 'L'):
            return L()
        elif (type == 'l'):
            return Sl()
        elif (type == 'N'):
            return N()
        elif (type == 'O'):
            return O()
        elif (type == 'P'):
            return P()
        elif (type == 'T'):
            return T()
        elif (type == 'V'):
            return V()
        elif (type == 'v'):
            return Sv()
        elif (type == 'W'):
            return W()
        elif (type == 'X'):
            return X()
        elif (type == 'Z'):
            return Z()
        else:
            return Tetrimino()

class I(Tetrimino):

    """Generate shape I"""

    def __init__(self):
        self.title = 'I'
        self.grids = [
            [
                "1111",
            ],
            [
                "1",
                "1",
                "1",
                "1",
            ],
        ]
        Tetrimino.__init__(self)

class L(Tetrimino):

    """Generate shape L"""

    def __init__(self):
        self.title = 'L'
        self.grids = [
            [
                "1",
                "1",
                "11",
            ],
            [
                "111",
                "1",
            ],
        ]
        Tetrimino.__init__(self)

class Sl(Tetrimino):

    """Generate shape small L"""

    def __init__(self):
        self.title = 'l'
        self.grids = [
            [
                "1",
                "11",
            ],
            [
                " 1",
                "11",
            ],
            [
                "11",
                "1",
            ],
            [
                "11",
                " 1",
            ],
        ]
        self.length = 3
        Tetrimino.__init__(self)

class N(Tetrimino):

    """Generate shape N"""

    def __init__(self):
        self.title = 'N'
        self.grids = [
            [
                "11",
                "11",
            ],
        ]
        Tetrimino.__init__(self)

class O(Tetrimino):

    """Generate shape O"""

    def __init__(self):
        self.title = 'O'
        self.grids = [
            [
                "11",
                "11",
            ],
        ]
        Tetrimino.__init__(self)

class P(Tetrimino):

    """Generate shape P"""

    def __init__(self):
        self.title = 'P'
        self.grids = [
            [
                "11",
                "11",
            ],
        ]
        Tetrimino.__init__(self)

class T(Tetrimino):

    """Generate shape T"""

    def __init__(self):
        self.title = 'T'
        self.grids = [
            [
                "111",
                " 1",
            ],
            [
                " 1",
                "11",
                " 1",
            ],
            [
                " 1",
                "111",
            ],
            [
                "1",
                "11",
                "1",
            ],
        ]
        Tetrimino.__init__(self)

class V(Tetrimino):

    """Generate shape V"""

    def __init__(self):
        self.title = 'V'
        self.grids = [
            [],
        ]
        Tetrimino.__init__(self)

class Sv(Tetrimino):

    """Generate shape small V"""

    def __init__(self):
        self.title = 'V'
        self.grids = [
            [],
        ]
        Tetrimino.__init__(self)

class W(Tetrimino):

    """Generate shape W"""

    def __init__(self):
        self.title = 'W'
        self.grids = [
            [],
        ]
        Tetrimino.__init__(self)

class X(Tetrimino):

    """Generate shape X"""

    def __init__(self):
        self.title = 'X'
        self.grids = [
            [],
        ]
        Tetrimino.__init__(self)

class Z(Tetrimino):

    """Generate shape Z"""

    def __init__(self):
        self.title = 'Z'
        self.grids = [
            [
                "11",
                " 11",
            ],
            [
                " 1",
                "11",
                "1 ",
            ],
        ]
        Tetrimino.__init__(self)

TYPE_SET = "ILlNOPTVvWXZ"


