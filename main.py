from importlib import import_module
from timeit import timeit

if __name__ == '__main__':
    day = input('Run day ')
    aoc = import_module(f'scripts.AoC2022-{day.zfill(2)}')
    print(f'Part 1 answer: {aoc.part1()}, in {timeit(aoc.part1, number=1)}')
    print(f'Part 2 answer: {aoc.part2()}, in {timeit(aoc.part2, number=1)}')
