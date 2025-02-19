import re

testCase1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
testCase2 = (
    "xmul(2,4000100)%&mul[3,7000]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)


def getInput() -> str:
    with open(
        rf"C:\Users\RickLyman\Desktop\Coding Challenges\2024-CodingAdvent Challenges\Day 3\day_3_input.txt",
        "r",
    ) as file:
        return file.read()


input = getInput()


def getMultipliersSum(numericalString: str) -> int:
    mulList = getMulList(numericalString)
    validatedList = validateMulitpliers(mulList)
    return sum([pair[0] * pair[1] for pair in validatedList])


def validateMulitpliers(multipliers: list[list[int]]):
    return list(
        filter(
            lambda pair: pair[0] < 1000 and pair[1] < 1000,
            multipliers,
        )
    )


def getMulList(string: str) -> list[list[int]]:
    pattern = r"mul\(\d+,\d+\)"
    mulList = re.findall(pattern, string)
    multipliers = list(map(extractNums, mulList))
    return multipliers


def extractNums(string: str) -> list[int]:
    return list(map(int, re.findall(r"\d+", string)))


testCase3 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def filterStringByDoConditional(longString: str) -> list[str]:
    stringList = longString.split("do()")
    return [string.split("don't()")[0] for string in stringList]


def getConditionalTotal(filteredList: list[str]) -> int:
    return sum([getMultipliersSum(string) for string in filteredList])


def parseFilterStringGetTotal() -> int:
    longString = getInput()
    filteredString = filterStringByDoConditional(longString=longString)
    return getConditionalTotal(filteredString)


print(getMultipliersSum(testCase1))
print(getMultipliersSum(getInput()))  # Correct answer: 183380722
print(filterStringByDoConditional(testCase3))
print(parseFilterStringGetTotal())  # Correct answer: 82733683
