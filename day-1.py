import requests
from day_1_puzzel_input import *


def parseInputStringToIntList(longString: str) -> dict[str, list[int]]:
    numsList: list[str] = longString.split("\n")
    list1: list[int] = []
    list2: list[int] = []
    for i in numsList:
        if i == "":
            continue
        numTuple = i.split()
        if len(numTuple) != 2:
            raise ValueError("The input string is not in the correct format")
        if not numTuple[0].isdigit() or not numTuple[1].isdigit():
            raise ValueError("The input string is not in the correct format")
        list1.append(int(numTuple[0]))
        list2.append(int(numTuple[1]))
    list1.sort()
    list2.sort()
    return {"listOne": list1, "listTwo": list2}


parseInputStringToIntList(longString)


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


def createDuplicateCountDict(listTwo: list[int]) -> dict[int, int]:
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
    countedDuplicates = createDuplicateCountDict(listTwo)
    return getSimilarityScore(listOne, countedDuplicates)


getSimilarityScoreFromInputString(longString)
