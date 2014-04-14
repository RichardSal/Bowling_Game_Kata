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
      if self.isStrike(frameIndex):
        score += 10 + self.strikeBonus(frameIndex)
        frameIndex += 1

      elif self.isSpare(frameIndex):
        score += 10 + self.spareBonus(frameIndex)
        frameIndex += 2

      else:
        score += self.sumOfBallsInFrame(frameIndex)
        frameIndex += 2
    return score

  def isStrike(self, frameIndex):
    return self.rolls[frameIndex] == 10

  def sumOfBallsInFrame(self, frameIndex):
    return self.rolls[frameIndex] + self.rolls[frameIndex+1]

  def spareBonus(self, frameIndex):
    return self.rolls[frameIndex+2]

  def strikeBonus(self, frameIndex):
    return self.rolls[frameIndex+1] + self.rolls[frameIndex+2]

  def isSpare(self, frameIndex):
    return self.rolls[frameIndex] + self.rolls[frameIndex + 1] == 10

def main():
  pass

if __name__ == '__main__':
  main()