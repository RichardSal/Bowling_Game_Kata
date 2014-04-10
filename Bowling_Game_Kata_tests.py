import unittest
import Bowling_Game_Kata_src

class testCase1(unittest.TestCase):
  """ """

  def testA(self):
    """ Class exists """
    g = Bowling_Game_Kata_src.game()
    for i in range(20):
      g.roll(0)

if __name__ == "__main__":
  unittest.main() # run all tests