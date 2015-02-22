from exercice11 import GridTopologie

def test_GridTopologie():
  gt = GridTopologie(3, 4)
  assert gt._are_adjacents(0, 1)
  assert gt._are_adjacents(0, 4)
  assert gt._are_adjacents(0, 5)

if __name__ == '__main__':
  test_GridTopologie()
