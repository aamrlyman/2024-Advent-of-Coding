const fs = require("fs");

function getInput() {
  const input = fs.readFileSync(
    "C:/Users/RickLyman/Desktop/Coding Challenges/2024-CodingAdvent Challenges/Day 2/day_2_input.txt"
  );
  const list = input.toString().split("\r\n");
  const inputNumsList = list.map((s) => s.split(" ").map(Number));
  return inputNumsList;
}

function getSafeCount(longNumList) {
  let count = 0;
  longNumList.forEach((sublist) => {
    if (isSafe(sublist)) {
      count += 1;
    } else if (dampen(sublist).some((sl) => isSafe(sl))) {
      count += 1;
    }
  });
  console.log("Total Safe Count: ", count);
  return count;
}

function isSafe(sublist) {
  return (
    getDeltas(sublist).every((delta) => delta > 0 && Math.abs(delta) <= 3) ||
    getDeltas(sublist).every((delta) => delta < 0 && Math.abs(delta) <= 3)
  );
}

function dampen(sublist) {
  return sublist.map((_, index) => sublist.filter((_, i) => i !== index));
}

function getDeltas(sublist) {
  return sublist.slice(0, -1).map((num, i) => num - sublist[i + 1]);
}

getSafeCount(getInput());
