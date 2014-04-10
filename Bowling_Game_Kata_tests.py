import unittest
import Bowling_Game_Kata_src

class BowlingGameTest(unittest.TestCase):
  """ """
  def setUp(self):
    global g
    g = Bowling_Game_Kata_src.game()

  def rollMany(self, n, pins):
    for i in range(0, n, 1):
      g.roll(pins)

  def testGutterGame(self):
    """ Class exists """
    self.rollMany(20, 0)
    self.assertEqual(0, g.getScore())

  def testAllOnes(self):
    self.rollMany(20, 1)
    self.assertEqual(20, g.getScore())



"""
  def testOneSpare(self):
    g.roll(5)
    g.roll(5)
    g.roll(3)
    self.rollMany(17, 0)

    self.assertEqual(16, g.getScore())
"""


if __name__ == "__main__":
  unittest.main() # run all tests