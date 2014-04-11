class game(object):
  """docstring for game"""
  def __init__(self):
    self.rolls = [0]
    self.currentRoll = 0

  def roll(self, pins):
    # TODO: better way to check if first index [0], else append to end
    if self.currentRoll == 0:
      self.rolls[0] = pins
    else:
      self.rolls.append(pins)

    self.currentRoll += 1

  def getScore(self):
    score = 0
    i = 0

    for frame in range(0, 10, 1):
      score += self.rolls[i] + self.rolls[i+1]
      i += 2

    return score

def main():
  pass

if __name__ == '__main__':
  main()