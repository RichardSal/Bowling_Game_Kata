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

  def testOneSpare(self):
    self.rollStrike()
    g.roll(3)
    g.roll(4)
    self.rollMany(16, 0)
    self.rollSpare()

    self.assertEqual(24, g.getScore())

  def testPerfectGame(self):
    self.rollMany(12, 10)
    self.assertEqual(300, g.getScore())

  def rollSpare(self):
    g.roll(5)
    g.roll(5)

  def rollStrike(self):
    g.roll(10)

if __name__ == "__main__":
  unittest.main() # run all tests