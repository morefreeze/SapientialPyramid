""" NONE_PIC means some part of piese have been placed here.
"""
NONE_PIC = '*'
EMPTY_PIC = ' '

class Tetrimino(object):

    """Describe each tetrimino."""
    title = NONE_PIC
    """ Each grids first line must contains at least '1'.
    The last space of each line can be omitted.
    """
    grids = [[]]
    """ arr must contains (0,0), but order is no need.
    """
    arr = []
    length = 0

    def __init__(self):
        from operator import sub
        self.arr = []
        for i in range(len(self.grids)):
            arr = []
            # max_width record max width for horizontal flip
            max_width = 0
            # first_max_y record first line max y, which is as (0,0)
            first_max_y = 0
            for x in range(len(self.grids[i])):
                for y in range(len(self.grids[i][x])):
                    if self.grids[i][x][y] == '1':
                        if x == 0:
                            first_max_y = y
                        arr.append((x,y))
                max_width = max(max_width, len(self.grids[i][x]))
            # construct horizontal flip arr
            rarr = []
            drx, dry = 0, max_width-first_max_y-1
            for j in range(len(arr)):
                rarr.append((arr[j][0], max_width-arr[j][1]-1))
            # convert first element as (0,0) including arr and rarr
            (dx, dy) = arr[0]
            for j in range(len(arr)):
                arr[j] = tuple(map(sub, arr[j], (dx, dy)))
                rarr[j] = tuple(map(sub, rarr[j], (drx, dry)))
            self.arr.append(arr)
            if not self.__class__.eq_arr(arr, rarr):
                self.arr.append(rarr)

    @classmethod
    def eq_arr(cls, lhs, rhs):
        """TODO: Docstring for eq_arr.
        :lhs: left hand side array
        :rhs: right hand side array
        :returns: boolean

        """
        d = {}
        for i in range(len(lhs)):
            if lhs[i] not in d:
                d[lhs[i]] = 0
            d[lhs[i]] += 1
        for i in range(len(rhs)):
            if rhs[i] not in d:
                return False
            d[rhs[i]] -= 1
            if d[rhs[i]] == 0:
                del(d[rhs[i]])
        return len(d) == 0

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
        self.length = 4
        Tetrimino.__init__(self)

class L(Tetrimino):

    """Generate shape L"""

    def __init__(self):
        self.title = 'L'
        self.grids = [
            [
                "1",
                "1",
                "1",
                "11",
            ],
            [
                "1111",
                "1",
            ],
            [
                "11",
                " 1",
                " 1",
                " 1",
            ],
            [
                "   1",
                "1111",
            ],
        ]
        self.length = 5
        Tetrimino.__init__(self)

class Sl(Tetrimino):

    """Generate shape small L"""

    def __init__(self):
        self.title = 'l'
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
            [
                "11",
                " 1",
                " 1",
            ],
            [
                "  1",
                "111",
            ],
        ]
        self.length = 4
        Tetrimino.__init__(self)

class N(Tetrimino):

    """Generate shape N"""

    def __init__(self):
        self.title = 'N'
        self.grids = [
            [
                "111",
                "1 1",
            ],
            [
                "11",
                " 1",
                "11",
            ],
            [
                "1 1",
                "111",
            ],
            [
                "11",
                "1",
                "11",
            ],
        ]
        self.length = 5
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
        self.length = 4
        Tetrimino.__init__(self)

class P(Tetrimino):

    """Generate shape P"""

    def __init__(self):
        self.title = 'P'
        self.grids = [
            [
                "11",
                "11",
                "1",
            ],
            [
                "111",
                " 11",
            ],
            [
                " 1",
                "11",
                "11",
            ],
            [
                "11",
                "111",
            ],
        ]
        self.length = 5
        Tetrimino.__init__(self)

class T(Tetrimino):

    """Generate shape T"""

    def __init__(self):
        self.title = 'T'
        self.grids = [
            [
                "1111",
                " 1",
            ],
            [
                " 1",
                "11",
                " 1",
                " 1",
            ],
            [
                "  1",
                "1111",
            ],
            [
                "1",
                "1",
                "11",
                "1",
            ],
        ]
        self.length = 5
        Tetrimino.__init__(self)

class V(Tetrimino):

    """Generate shape V"""

    def __init__(self):
        self.title = 'V'
        self.grids = [
            [
                "1",
                "1",
                "111",
            ],
            [
                "111",
                "1",
                "1",
            ],
            # Others can be flipped.
        ]
        self.length = 5
        Tetrimino.__init__(self)

class Sv(Tetrimino):

    """Generate shape small V"""

    def __init__(self):
        self.title = 'V'
        self.grids = [
            [
                "1",
                "11",
            ],
            [
                "11",
                "1",
            ],
            # Others can be flipped.
        ]
        self.length = 3
        Tetrimino.__init__(self)

class W(Tetrimino):

    """Generate shape W"""

    def __init__(self):
        self.title = 'W'
        self.grids = [
            [
                "11",
                " 11",
                "  1",
            ],
            [
                "  1",
                " 11",
                "11",
            ],
            # Others can be flipped.
        ]
        self.length = 5
        Tetrimino.__init__(self)

class X(Tetrimino):

    """Generate shape X"""

    def __init__(self):
        self.title = 'X'
        self.grids = [
            [
                " 1",
                "111",
                " 1",
            ],
        ]
        self.length = 5
        Tetrimino.__init__(self)

class Z(Tetrimino):

    """Generate shape Z"""

    def __init__(self):
        self.title = 'Z'
        self.grids = [
            [
                "11",
                " 111",
            ],
            [
                " 1",
                "11",
                "1 ",
                "1 ",
            ],
            [
                "111",
                "  11",
            ],
            [
                " 1",
                " 1",
                "11",
                "1 ",
            ],
        ]
        self.length = 5
        Tetrimino.__init__(self)

TYPE_SET = "ILlNOPTVvWXZ"


