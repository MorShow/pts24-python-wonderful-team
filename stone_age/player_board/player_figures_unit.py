import unittest
from player_figures import PlayerFigures


class PlayerFiguresUnit(unittest.TestCase):
    def test_count_figures(self):
        p1 = PlayerFigures()
        self.assertFalse(p1.take_figures(5))
        self.assertFalse(p1.has_figures(2))
        for i in range(3):
            p1.add_new_figure()
        self.assertTrue(p1.has_figures(2))
        for i in range(6):
            p1.add_new_figure()
        self.assertEqual(p1.get_total_figures, 31)
        self.assertTrue(p1.add_new_figure())
        self.assertFalse(p1.add_new_figure())
        self.assertEqual(p1.get_total_figures, 30)

        p2 = PlayerFigures()
        for i in range(7):
            p2.add_new_figure()
        self.assertEqual(p2.get_total_figures, 23)
        self.assertFalse(p1.add_new_figure())
        self.assertEqual(p2.get_total_figures, 23)

    def run_out_of_figures(self):
        p1 = PlayerFigures()
        p2 = PlayerFigures()
        p3 = PlayerFigures()
        p4 = PlayerFigures()
        for i in range(10):
            p1.add_new_figure()
            p2.add_new_figure()
            p3.add_new_figure()
            p4.add_new_figure()
        self.assertEqual(p1.get_total_figures, 0)
        p1.add_new_figure()
        self.assertGreaterEqual(p1.get_total_figures, 0)

    def take_figures(self):
        p1 = PlayerFigures()
        for i in range(9):
            p1.add_new_figure()
        self.assertTrue(p1.take_figures(5))
        self.assertEqual(p1.get_total_figures, 31)
        self.assertFalse(p1.take_figures(5))
        self.assertFalse(p1.has_figures(1))
        self.assertTrue(p1.has_figures(0))


if __name__ == '__main__':
    unittest.main()
