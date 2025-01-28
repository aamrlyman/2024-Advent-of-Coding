from collections.abc import Callable


def get_input() -> list[list[int]]:
    with open(
        rf"C:\Users\RickLyman\Desktop\Coding Challenges\2024-CodingAdvent Challenges\Day 2\day_2_input.txt"
    ) as f:
        lines = f.readlines()
        two_deep_list = [line.split() for line in lines]
        return [[int(num) for num in sublist] for sublist in two_deep_list]


class IsIncreasing:
    def __init__(self, increasing: bool = False):
        self.increasing = increasing


class IsSafeTrend:
    def __init__(self, safeTrend: bool = False, problemIndex: int | None = None):
        self.safe = safeTrend
        self.problemIndex = problemIndex


def isChangingBy3orLess(sublist: list[int], isIncreasing: IsIncreasing) -> IsSafeTrend:
    for index in range(len(sublist)):
        if index + 1 == len(sublist):
            break
        diff = (
            sublist[index + 1] - sublist[index]
            if isIncreasing.increasing
            else sublist[index] - sublist[index + 1]
        )
        if diff > 3 or diff <= 0:
            problemIndex = index + 1
            return IsSafeTrend(False, problemIndex)
    return IsSafeTrend(True, None)


def isSafeTrend(sublist: list[int]):
    return (
        isChangingBy3orLess(sublist, IsIncreasing(True)).safe
        or isChangingBy3orLess(sublist, IsIncreasing(False)).safe
    )


def isSafeTrendWithItemRemoved(sublist: list[int]) -> bool:
    isIncreasingAttemptOne = isChangingBy3orLess(sublist, IsIncreasing(True))
    if isIncreasingAttemptOne.safe:
        return True
    if isIncreasingAttemptOne.problemIndex is not None:
        listWithItemRemoved = sublist.copy()
        del listWithItemRemoved[isIncreasingAttemptOne.problemIndex]
        if isChangingBy3orLess(listWithItemRemoved, IsIncreasing(True)).safe:
            return True
        listWithDiffRemoved = sublist.copy()
        del listWithItemRemoved[isIncreasingAttemptOne.problemIndex - 1]
        if isChangingBy3orLess(listWithDiffRemoved, IsIncreasing(True)).safe:
            return True

    isDecreasingAttemptOne = isChangingBy3orLess(sublist, IsIncreasing(False))
    if isDecreasingAttemptOne.safe:
        return True
    if isDecreasingAttemptOne.problemIndex is not None:
        listWithItemRemoved = sublist.copy()
        del listWithItemRemoved[isDecreasingAttemptOne.problemIndex]
        if isChangingBy3orLess(listWithItemRemoved, IsIncreasing(False)).safe:
            return True
        listWithDiffRemoved = sublist.copy()
        del listWithItemRemoved[isDecreasingAttemptOne.problemIndex - 1]
        if isChangingBy3orLess(listWithDiffRemoved, IsIncreasing(False)).safe:
            return True
    return False


def get_safe_count(two_deep_list: list[list[int]], isSafeFn: Callable) -> int:
    count = 0
    for sublist in two_deep_list:
        if isSafeFn(sublist):
            count += 1
    print("Total Safe Count: ", count)
    return count


def changingBy3orLess(
    sublist: list[int], isIncreasing: bool, retries: int, limit: int
) -> bool:
    for index in range(len(sublist) - 1):
        diff = (
            sublist[index + 1] - sublist[index]
            if isIncreasing
            else sublist[index] - sublist[index + 1]
        )
        if diff > 3 or diff <= 0:
            if retries >= limit:
                return False
            list1 = sublist[:index] + sublist[index + 1 :]
            list2 = sublist[: index + 1] + sublist[index + 2 :]
            retries += 1
            return changingBy3orLess(
                list1, isIncreasing, retries, limit
            ) or changingBy3orLess(list2, isIncreasing, retries, limit)
    return True


def is_stepping_by_3_with_recursion(sublist: list[int], limit: int = 1):
    retries = 0
    if changingBy3orLess(sublist, isIncreasing=True, retries=retries, limit=limit):
        return True
    if changingBy3orLess(sublist, isIncreasing=False, retries=retries, limit=limit):
        return True
    return False


get_safe_count(get_input(), is_stepping_by_3_with_recursion)
