class game(object):
  """docstring for game"""
  def __init__(self):
    self.score = 0
    self.rolls = [21]
    self.currentRoll = 0

  def roll(self, pins):
    self.score += pins
    self.currentRoll += 1
    self.rolls.append(pins)

  def getScore(self):
    return self.score

def main():
  pass

if __name__ == '__main__':
  main()