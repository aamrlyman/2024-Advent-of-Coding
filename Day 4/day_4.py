# thistring = """
# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# """


def creategrid() -> list[list[str]]:
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    grid: list[list[str]] = []
    for index in range(10):
        grid.append([])
        for letter in letters:
            grid[index].append(f"{letter}{index+1}")
    return grid


# print(creategrid())


def wordSearch(longString) -> list[str]:
    return list(filter(lambda string: string != "", longString.split("\n")))


def getRowCombinations(wordSearch: list[str]) -> list[str]:
    # reversedStringsList = [string[::-1] for string in wordSearch]
    return wordSearch


def getColumnCombinations(wordSearch: list[str], isAscending: bool) -> list[str]:
    wordSearchLength = len(wordSearch)
    startingIndex = 0 if isAscending else wordSearchLength - 1
    stoppingIndex = wordSearchLength if isAscending else -1
    incrementer = 1 if isAscending else -1
    columns = []

    for i in range(len(wordSearch[0])):
        newString: str = ""
        for index in range(startingIndex, stoppingIndex, incrementer):
            currentString = wordSearch[index]
            newString += currentString[i]
        columns.append(newString)
    return columns


def getDiagonalLeftToRight(
    grid1: list[str],
    # , startingTopLeft: bool, startingBottomLeft: bool = False
) -> list[str]:
    diagonals: list[str] = []
    x = 0
    while x < len(grid1[0]):
        y = 0
        outputString = ""
        tempX = x
        while y < len(grid1) and tempX >= 0:
            outputString += grid1[y][tempX]
            tempX -= 1
            y += 1
        x += 1
        if len(outputString) > 3:
            diagonals.append(outputString)
    y = 1
    while y < len(grid1):
        x = len(grid1[0]) - 1
        outputString = ""
        tempY = y
        while tempY < len(grid1) and x >= 0:
            outputString += grid1[tempY][x]
            tempY += 1
            x -= 1
        y += 1
        if len(outputString) > 3:
            diagonals.append(outputString)
    return diagonals


def getDiagonalsRightToLeft(
    grid: list[str],
) -> list[str]:
    diagonals: list[str] = []
    y = len(grid) - 1
    while y >= 0:
        x = len(grid[0]) - 1
        outputString = ""
        tempY = y
        while tempY < len(grid) and x >= 0:
            outputString += grid[tempY][x]
            tempY += 1
            x -= 1
        y -= 1
        if len(outputString) > 3:
            diagonals.append(outputString)
    x = len(grid[0]) - 1
    while x >= 0:
        y = 0
        outputString = ""
        tempX = x
        while y <= len(grid) and tempX >= 0:
            outputString += grid[y][tempX]
            tempX -= 1
            y += 1
        x -= 1
        if len(outputString) > 3:
            diagonals.append(outputString)
    return diagonals


def getXmasCount():
    stringslist = (
        getRowCombinations(wordSearch=wordSearch)
        + getColumnCombinations(wordSearch=wordSearch, isAscending=True)
        + getDiagonalLeftToRight(grid1=wordSearch)
        + getDiagonalsRightToLeft(grid=wordSearch)
    )
    count = 0
    searchString = "XMAS"
    print(stringslist)
    for string in stringslist:
        count += string.count(searchString)
        count += string.count(searchString[::-1])
    return count


# print(getXmasCount())


# print(
#     "ascending columns: ",
#     getColumnCombinations(wordSearch=wordSearch, isAscending=True),
# )
# print(
#     "descending columns: ",
#     getColumnCombinations(wordSearch=wordSearch, isAscending=False),
# )
# print("rows: ", getRowCombinations(wordSearch=wordSearch))

test1 = """
X...
.M..
..A.
...S
"""
test2 = """
...X
..M.
.A..
S...
"""

print("diagonalsLeftToRight:", getDiagonalLeftToRight(wordSearch(test1)))
print("diagonalsRightToLeft:", getDiagonalsRightToLeft(wordSearch(test2)))
