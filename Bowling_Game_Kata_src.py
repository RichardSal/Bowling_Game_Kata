class game(object):
  """docstring for game"""
  def __init__(self):
    self.rolls = []
    self.currentRoll = 0

  def roll(self, pins):
    self.currentRoll += 1
    self.rolls.append(pins)

  def getScore(self):
    score = 0
    i = 0

    while i < len(self.rolls):
      score += self.rolls[i]
      i += 1

    return score

def main():
  pass

if __name__ == '__main__':
  main()