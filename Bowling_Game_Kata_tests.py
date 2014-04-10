import unittest
import Bowling_Game_Kata_src

class BowlingGameTest(unittest.TestCase):
  """ """
  def setUp(self):
    global g
    g = Bowling_Game_Kata_src.game()

  def testGutterGame(self):
    """ Class exists """
    
    for i in range(0, 20, 1):
      g.roll(0)
    self.assertEqual(0, g.getScore())

  def testAllOnes(self):
    for i in range(0, 20, 1):
      g.roll(1)
    self.assertEqual(20, g.getScore())


if __name__ == "__main__":
  unittest.main() # run all tests