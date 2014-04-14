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
    frameIndex = 0

    for frame in range(0, 10, 1):
      if self.isSpare(frameIndex):
        score += 10 + self.rolls[frameIndex+2]
        frameIndex += 2
      else:
        score += self.rolls[frameIndex] + self.rolls[frameIndex+1]
        frameIndex += 2
    return score

  def isSpare(self, frameIndex):
    return self.rolls[frameIndex] + self.rolls[frameIndex + 1] == 10

def main():
  pass

if __name__ == '__main__':
  main()