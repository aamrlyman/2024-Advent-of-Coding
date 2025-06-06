from day_5_input import *
import math
from dataclasses import dataclass

rules1 = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
"""


pageUpdates = """
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,4
"""


def getMiddleNumberCount(correctlyOrderedPageUpdates: list[list[int]]) -> int:
    total = 0
    # print(correctlyOrderedPageUpdates)
    for pageUpdate in correctlyOrderedPageUpdates:
        if len(pageUpdate) % 2 == 0 and len(pageUpdate) > 0:
            raise Exception(f"pageUpdateList {pageUpdate} has an even number of items")

        index = len(pageUpdate) // 2
        if index >= len(pageUpdate) or index < 0:
            raise Exception(f"{pageUpdate} list had an issue")
        total += pageUpdate[index]

    return total


def getPageUpdatesThatAreInCorrectOrder(rulesString: str, pagesString: str):
    rulesDict = parseRules(rulesString)
    pageUpdatesList = parsePageUpdates(pagesString)
    return [
        pageUpdate
        for pageUpdate in pageUpdatesList
        if isPageUpdateInCorrectOrder(
            rulesDict=rulesDict,
            pageUpdate=pageUpdate,
        )
    ]


@dataclass
class RuleNode:
    visited: bool
    afterKey: list[int]
    beforeKey: list[int]


def createDAG(longString: str) -> dict[int, RuleNode]:
    rulesList = [line for line in longString.splitlines() if line.strip()]
    rulesDict: dict[int, RuleNode] = {}
    for rule in rulesList:
        ruleTuple = [parseStringToInt(rule.strip()) for rule in rule.split("|")]
        if ruleTuple[0] not in rulesDict:
            rulesDict[ruleTuple[0]] = RuleNode(False, [ruleTuple[1]], [])
        else:
            rulesDict[ruleTuple[0]].afterKey.append(ruleTuple[1])

        if ruleTuple[1] not in rulesDict:
            rulesDict[ruleTuple[1]] = RuleNode(False, [], [ruleTuple[0]])
        else:
            rulesDict[ruleTuple[1]].beforeKey.append(ruleTuple[0])
    return rulesDict


def parseStringToInt(string: str) -> int:
    if string.isnumeric():
        return int(string)
    else:
        raise Exception(f"{string} is not a number")


def createTopSortList(DAG: dict[int, RuleNode]) -> list[int]:
    topSortList = []
    for key in DAG:
        if not DAG[key].visited:
            dfs(key, DAG, topSortList)
    return list(reversed(topSortList))  # Reverse to get the correct topological order


def dfs(key: int, DAG: dict[int, RuleNode], topSortList: list[int]):
    ruleNode = DAG[key]
    if ruleNode.visited:
        return
    ruleNode.visited = True
    for nextKey in ruleNode.afterKey:
        dfs(nextKey, DAG, topSortList)
    topSortList.append(key)  # Append after all descendants are visited


DAG = createDAG(rules1)

topSortList = createTopSortList(DAG)

distinctOrder = [97, 75, 47, 61, 53, 29, 13]


def test(output, expected):
    if output == expected:
        print("Success!!")
    else:
        print("failed")
    print("output:", output)
    print("expected:", expected)


test(topSortList, distinctOrder)


def parsePageUpdates(pageUpdates: str) -> list[list[int]]:
    intList = [
        [int(s.strip()) for s in line.split(",") if s.strip().isnumeric()]
        for line in pageUpdates.strip().splitlines()
        if line.strip() and any(s.strip().isnumeric() for s in line.split(","))
    ]
    return intList


def isPageUpdateInCorrectOrder(
    rulesDict: dict[int, list[int]], pageUpdate: list[int]
) -> bool:
    for i in range((len(pageUpdate) - 1), -1, -1):
        pageNumber = pageUpdate[i]
        if pageNumber in rulesDict:
            start = i - 1
            pagesThatComeAfter = rulesDict[pageNumber]
            for j in range(start, -1, -1):
                if pageUpdate[j] in pagesThatComeAfter:
                    return False

    return True


print(
    getMiddleNumberCount(
        getPageUpdatesThatAreInCorrectOrder(rulesString=rules1, pagesString=pageUpdates)
    )
)
print(
    "actual answer:",
    getMiddleNumberCount(
        getPageUpdatesThatAreInCorrectOrder(rulesString=rules, pagesString=pages)
    ),
)
# # 7074

distinct = {"47", "29", "53", "61", "13", "75", "97"}
distinctOrder = [97, 75, 47, 61, 53, 29, 13]

asdf = {
    47: RuleNode(visited=False, afterKey=[53, 13, 61, 29], beforeKey=[97, 75]),
    53: RuleNode(visited=False, afterKey=[29, 13], beforeKey=[47, 75, 61, 97]),
    97: RuleNode(visited=False, afterKey=[13, 61, 47, 29, 53, 75], beforeKey=[]),
    13: RuleNode(visited=False, afterKey=[], beforeKey=[97, 61, 29, 47, 75, 53]),
    61: RuleNode(visited=False, afterKey=[13, 53, 29], beforeKey=[97, 47, 75]),
    75: RuleNode(visited=False, afterKey=[29, 53, 47, 61, 13], beforeKey=[97]),
    29: RuleNode(visited=False, afterKey=[13], beforeKey=[75, 97, 53, 61, 47]),
}
