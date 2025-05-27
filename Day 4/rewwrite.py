from typing import Iterator, List, Tuple
from itertools import zip_longest, islice
from collections import defaultdict


class WordSearch:
    def __init__(self, raw_input: str) -> None:
        self.grid: List[str] = [line for line in raw_input.splitlines() if line.strip()]
        self.height: int = len(self.grid)
        self.width: int = len(self.grid[0])

        # Generate all grid positions lazily
        self.positions: Iterator[Tuple[int, int]] = (
            (x, y) for x in range(self.width) for y in range(self.height)
        )

        # Direction vectors: 8 directions (N, S, E, W, NE, NW, SE, SW)
        direction_offsets = [-1, 0, 1]
        self.all_directions = [
            (dx, dy)
            for dx in direction_offsets
            for dy in direction_offsets
            if dx != 0 or dy != 0
        ]

        # Only diagonal directions
        self.diagonal_directions = [
            (dx, dy)
            for dx in direction_offsets
            for dy in direction_offsets
            if dx != 0 and dy != 0
        ]

    def get_word_count(self, target_word: str) -> int:
        print(f"\nSearching for word: '{target_word}'")
        matches = 0
        for word_stream in self.generate_word_streams():
            grid_chars = islice((char for char, _, _ in word_stream), len(target_word))
            word_match = zip_longest(grid_chars, target_word)

            if all(grid_char == target_char for grid_char, target_char in word_match):
                matches += 1
                print(f"Match found for '{target_word}'")
        return matches

    def get_matching_triplets(
        self, target_word: str
    ) -> List[List[Tuple[str, int, int]]]:
        print(f"\nFinding triplets that match: '{target_word}'")
        matching_triplets = []

        for word_stream in self.generate_word_streams(use_all_directions=False):
            triplet: List[Tuple[str, int, int]] = []

            for char_info in word_stream:
                triplet.append(char_info)
                if len(triplet) == len(target_word):
                    break

            if len(triplet) != len(target_word):
                continue

            chars_in_triplet = [char for char, _, _ in triplet]
            if chars_in_triplet == list(target_word):
                print(f"Found matching triplet: {triplet}")
                matching_triplets.append(triplet)

        return matching_triplets

    def count_xmas_patterns(self) -> int:
        print("\nCounting 'XMAS' patterns with overlapping middle 'A' letters...")
        mas_triplets = self.get_matching_triplets("MAS")
        middle_map = defaultdict(list)

        for triplet in mas_triplets:
            if len(triplet) != 3:
                continue
            middle_char, x, y = triplet[1]
            middle_map[(x, y)].append(triplet)

        count = sum(1 for match_list in middle_map.values() if len(match_list) >= 2)
        print(f"Number of overlapping 'MAS' with the same middle 'A': {count}")
        return count

    def generate_word_streams(
        self, use_all_directions: bool = True
    ) -> Iterator[Iterator[Tuple[str, int, int]]]:
        directions = (
            self.all_directions if use_all_directions else self.diagonal_directions
        )
        return (
            self.traverse_from_position(start, direction)
            for start in self.positions
            for direction in directions
        )

    def traverse_from_position(
        self, start: Tuple[int, int], direction: Tuple[int, int]
    ) -> Iterator[Tuple[str, int, int]]:
        x, y = start
        dx, dy = direction

        while self.is_within_bounds(x, y):
            char = self.grid[y][x]
            yield (char, x, y)
            x += dx
            y += dy

    def is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height
