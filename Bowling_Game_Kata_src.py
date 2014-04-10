class game(object):
  """docstring for game"""
  def __init__(self):
    self.score = 0

  def roll(self, pins):
    self.score = self.score + pins

  def getScore(self):
    return self.score

def main():
  """
  g = game()

  for i in range(0, 20, 1):
    g.roll(1)

  print(str(g.getScore()))
  """

if __name__ == '__main__':
  main()