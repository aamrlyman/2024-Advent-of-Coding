const fs = require("fs");
const testCase =
  "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";

const testCase2 =
  "xmul(2,4000100)%&mul[3,7000]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";

function getInput() {
  const input = fs.readFileSync(
    "C:/Users/RickLyman/Desktop/Coding Challenges/2024-CodingAdvent Challenges/Day 3/day_3_input.txt",
    "utf-8"
  );
  return input;
}

function getTotalMultipliers({ longString, applyConditionals, regex }) {
  let mulsArray = parseMULs(longString, regex);
  if (applyConditionals) {
    mulsArray = filterArray(mulsArray);
  }
  const numberSearch = /\d+/g;
  const numsOnlyArray = mulsArray.map((pair) =>
    pair.match(numberSearch).map(Number)
  );
  return numsOnlyArray.reduce((sum, [a, b]) => sum + a * b, 0);
}

function parseMULs(longString, regex) {
  const pattern = regex;
  return longString.match(pattern);
}

function filterArray(arrayWithDoDontAndMulPairs) {
  let add = true;
  const filteredArray = [];
  for (let i = 0; i < arrayWithDoDontAndMulPairs.length; i++) {
    const item = arrayWithDoDontAndMulPairs[i];
    if (item === "don't()") {
      add = false;
    }
    if (item === "do()") {
      add = true;
    }
    if (add && item.match(/\d+/g)) {
      filteredArray.push(item);
    }
  }
  return filteredArray;
}

const longString = getInput();
const star1 = getTotalMultipliers({
  longString: longString,
  applyConditionals: false,
  regex: /mul\(\d+,\d+\)/g,
});
console.log("star 1: ", star1);
const star2 = getTotalMultipliers({
  longString: longString,
  applyConditionals: true,
  regex: /do\(\)|don't\(\)|mul\(\d+,\d+\)/g,
});
console.log("star 2: ", star2);
