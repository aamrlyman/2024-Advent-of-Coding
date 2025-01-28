import requests
from day_1_puzzel_input import *


def errorHandler(list: list, index: int) -> bool:
    errorPrefix = f"The list:{list} at index: {index}"
    if len(list) == 0:
        raise ValueError(f"{errorPrefix} is empty")
    if not all(i.isnumeric() for i in list):
        raise ValueError(f"{errorPrefix} contains non-numeric values")
    if not all(int(i) < 10**6 for i in list):
        raise ValueError(f"{errorPrefix} contains values greater than 10^6")
    if len(list) > 2:
        raise ValueError(f"{errorPrefix} contains more than 2 items")
    return True


def parseInputStringToIntList(longString: str) -> dict[str, list[int]]:
    numsList: list[str] = longString.split("\n")
    list1: list[int] = []
    list2: list[int] = []
    for index, value in enumerate(numsList):
        if value == "":
            continue
        numTuple = value.split()
        errorHandler(numTuple, index)
        list1.append(int(numTuple[0]))
        list2.append(int(numTuple[1]))
    list1.sort()
    list2.sort()
    return {"listOne": list1, "listTwo": list2}


def getListDifference(listTuple: dict[str, list[int]]) -> int:
    list1, list2 = listTuple.values()
    difference = 0
    if len(list1) != len(list2):
        raise ValueError("The two lists are not of the same length")
    for i in range(len(list1)):
        difference += abs(list1[i] - list2[i])
    print("The difference between the two lists is: ", difference)
    return difference


getListDifference(parseInputStringToIntList(longString))


def createDictWithDuplicateCount(listTwo: list[int]) -> dict[int, int]:
    countedDuplicates = {}
    for i in listTwo:
        if i in countedDuplicates:
            countedDuplicates[i] += 1
        else:
            countedDuplicates[i] = 1
    return countedDuplicates


def getSimilarityScore(listOne: list[int], countedDuplicates: dict[int, int]) -> int:
    score = 0
    for i in listOne:
        if i in countedDuplicates:
            score += i * countedDuplicates[i]
    print("The similarity score is: ", score)
    return score


def getSimilarityScoreFromInputString(longString: str) -> int:
    parsedInput = parseInputStringToIntList(longString)
    listOne, listTwo = parsedInput.values()
    countedDuplicates = createDictWithDuplicateCount(listTwo)
    return getSimilarityScore(listOne, countedDuplicates)


getSimilarityScoreFromInputString(longString)
