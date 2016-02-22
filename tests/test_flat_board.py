import unittest
import program.flat_board

class TestTetriminos(unittest.TestCase):

    """Test Tetriminos."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_i(self):
        t = program.flat_board.TetriminoFactory.make('I')
        self.assertEqual(t.title, 'I')
        self.assertEquals(t.length, 4)
        arr = [
            [ (0,0), (0,1), (0,2), (0,3), ],
            [ (0,0), (1,0), (2,0), (3,0), ],
        ]
        self.assertEqual(t.arr, arr)

    def test_l(self):
        l = program.flat_board.TetriminoFactory.make('L')
        self.assertEqual(l.title, 'L')
        self.assertEquals(l.length, 5)
        arr = [
            [ (0,0), (1,0), (2,0), (3,0), (3,1), ],
            [ (0,0), (1,0), (2,0), (3,0), (3,-1), ],
            [ (0,0), (0,1), (0,2), (0,3), (1,0), ],
            [ (0,3), (0,2), (0,1), (0,0), (1,3), ],
            [ (0,0), (0,1), (1,1), (2,1), (3,1), ],
            [ (0,1), (0,0), (1,0), (2,0), (3,0), ],
            [ (0,0), (1,-3), (1,-2), (1,-1), (1,0), ],
            [ (0,0), (1,3), (1,2), (1,1), (1,0), ],
        ]
        self.assertEqual(l.arr, arr)

    def test_o(self):
        o = program.flat_board.TetriminoFactory.make('O')
        self.assertEqual(o.title, 'O')
        self.assertEquals(o.length, 4)
        arr = [
            [ (0,0), (0,1), (1,0), (1,1), ],
        ]
        self.assertEqual(o.arr, arr)

    def test_eq_arr(self):
        t_func = program.flat_board.Tetrimino.eq_arr
        arr = [1,2]
        rarr = [2,1]
        self.assertTrue(t_func(arr, rarr))
        arr = [1,2,2]
        rarr = [2,1,2]
        self.assertTrue(t_func(arr, rarr))
        arr = [1,2]
        rarr = [2]
        self.assertFalse(t_func(arr, rarr))
        arr = [1,2]
        rarr = [2]
        self.assertFalse(t_func(arr, rarr))
        arr = [2]
        rarr = [2,1]
        self.assertFalse(t_func(arr, rarr))

class TestBoard(unittest.TestCase):

    """Test board"""

    def setUp(self):
        self.b = program.flat_board.make_board(5)

    def tearDown(self):
        pass

    def test_try_place(self):
        # this will modify self.b
        b = self.b
        o = program.flat_board.TetriminoFactory.make('O')
        self.assertTrue(program.flat_board.try_place(b, 1, 0, o.arr[0], o.title))
        b0 = [
            [" "]*1,
            [c for c in "OO"],
            [c for c in "OO "],
            [" "]*4,
            [" "]*5,
        ]
        self.assertEqual(b0, b)

    def test_restore_place(self):
        b = self.b
        o = program.flat_board.TetriminoFactory.make('O')
        self.assertTrue(program.flat_board.try_place(b, 1, 0, o.arr[0], o.title))
        program.flat_board.restore_place(b, 1, 0, o.arr[0])
        ori_b = program.flat_board.make_board(5)
        self.assertEqual(ori_b, b)

if __name__ == "__main__":
    unittest.main()
