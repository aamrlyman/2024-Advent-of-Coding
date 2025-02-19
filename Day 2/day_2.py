def get_input() -> list[list[int]]:
    with open(
        rf"C:\Users\RickLyman\Desktop\Coding Challenges\2024-CodingAdvent Challenges\Day 2\day_2_input.txt"
    ) as f:
        lines = f.readlines()
        two_deep_list = [line.split() for line in lines]
        return [[int(num) for num in sublist] for sublist in two_deep_list]


def get_safe_count(two_deep_list: list[list[int]], limit: int = 0) -> int:
    count = 0
    for sublist in two_deep_list:
        if is_stepping_by_3_with_recursion(sublist, limit):
            count += 1
    print("Total Safe Count: ", count)
    return count


def is_stepping_by_3_with_recursion(sublist: list[int], limit: int = 0):
    retries = 0
    return changingBy3orLess(
        sublist, isIncreasing=True, retries=retries, limit=limit
    ) or changingBy3orLess(sublist, isIncreasing=False, retries=retries, limit=limit)


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


get_safe_count(get_input(), limit=1)
