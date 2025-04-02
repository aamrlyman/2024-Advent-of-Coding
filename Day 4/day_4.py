testCase1 = """
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
"""
testCase2 = """"" 
XMAS
.M..
..A.
...S
"""


class WordSearch:
    def __init__(self, longString) -> None:
        self.wordSearch: list[str] = list(
            filter(lambda string: string != "", longString.split("\n"))
        )
        self.height: int = len(self.wordSearch)
        self.width: int = len(self.wordSearch[0])


def create_permutations():
    amplitudes = [-1, 0, 1]
    return [(i, j) for i in amplitudes for j in amplitudes if i != 0 or j != 0]


def getAllPoints(width, height):
    points = [(x, y) for x in range(width) for y in range(height)]
