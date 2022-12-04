import re

def part1(line):
    return line[2] >= line[0] and line[3] <= line[1] or line[2] <= line[0] and line[3] >= line[1]

def part2(line):
    return line[0] <= line[2] <= line[1] or line[2] <= line[0] <= line[3]

def solve(lines, test):
    return sum([test(line) for line in lines])

def main():
    with open("input.txt", "r") as f:
        lines = [[int(x) for x in re.split(r'[-,]', line.strip())] for line in f.readlines()]
        print(solve(lines, part1))
        print(solve(lines, part2))

if __name__ == "__main__":
    main()