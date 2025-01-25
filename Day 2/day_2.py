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


def changingByThreeOrLess(sublist: list[int], isIncreasing: IsIncreasing) -> bool:
    for index in range(len(sublist)):
        if index + 1 == len(sublist):
            break
        diff = (
            sublist[index + 1] - sublist[index]
            if isIncreasing.increasing
            else sublist[index] - sublist[index + 1]
        )
        if diff > 3 or diff <= 0:
            return False
    return True


def isSafeTrend(sublist: list[int]):
    return changingByThreeOrLess(sublist, IsIncreasing(True)) or changingByThreeOrLess(
        sublist, IsIncreasing(False)
    )


def get_safe_count(two_deep_list: list[list[int]]) -> int:
    count = 0
    for sublist in two_deep_list:
        if isSafeTrend(sublist):
            count += 1
    print(count)
    return count


testlist = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

get_safe_count(get_input())
get_safe_count(testlist)
