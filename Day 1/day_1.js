const fs = require("fs");

function getInput() {
  const inputList = fs
    .readFileSync(
      "C:/Users/RickLyman/Desktop/Coding Challenges/2024-CodingAdvent Challenges/Day 1/day_1_puzzel_input.txt",
      "utf-8"
    )
    .trim()
    .split("\r\n")
    .map((line) => line.split(/\s+/).map(Number));
  const list1 = inputList.map((pair) => pair[0]).sort((a, b) => a - b);
  const list2 = inputList.map((pair) => pair[1]).sort((a, b) => a - b);
  return [list1, list2];
}

function getDifferences(list1, list2) {
  if (list1.length !== list2.length)
    throw new Error("Lists are not the same length");
  return list1.reduce((total, num, i) => total + Math.abs(num - list2[i]), 0);
}

function getSimilarityScore(list1, list2) {
  const duplicateCounts = list2.reduce((acc, num) => {
    acc[num] = (acc[num] || 0) + 1;
    return acc;
  }, {});

  return list1.reduce(
    (score, num) => score + (duplicateCounts[num] || 0) * num,
    0
  );
}
const [list1, list2] = getInput();
console.log(getDifferences(list1, list2));
console.log(getSimilarityScore(list1, list2));
