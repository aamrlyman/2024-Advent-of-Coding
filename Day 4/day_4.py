thistring = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

input_list = list(filter(lambda string: string != "", thistring.split("\n")))


def getRowCombinations(wordSearch: list[str]) -> list[str]:
    return [string[::-1] for string in wordSearch] + wordSearch


def getColumnCombinations(wordSearch: list[str], isDescending) -> list[str]:
    wordSearchLength = len(wordSearch)
    startingIndex = 0 if isDescending else wordSearchLength
    incrementer = 1 if isDescending else -1
    columns = []

    for i in range(len(wordSearch[0])):
        newString: str = ""
        for startingIndex in range(startingIndex, wordSearchLength, incrementer):
            currentString = wordSearch[startingIndex]
            newString += currentString[i]
        columns.append(newString)
    return columns


print(getColumnCombinations(input_list, isDescending=True))
# print(getRowCombinations(input_list))
