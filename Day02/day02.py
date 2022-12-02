def part1(lines):
    results = {"A": {"X": 3, "Y": 6, "Z": 0}, "B": {"X": 0, "Y": 3, "Z": 6}, "C": {"Y": 0, "Z": 3, "X": 6}}
    points = {"X": 1, "Y": 2, "Z": 3}
    total = 0
    for line in lines:
        total += results[line[0]][line[1]] + points[line[1]]
    return total

def part2(lines):
    transformations = {"A": {"X": "Z", "Y": "X", "Z": "Y"}, "B": {"X": "X", "Y": "Y", "Z": "Z"}, "C": {"X": "Y", "Y": "Z", "Z": "X"}}
    for line in lines:
        line[1] = transformations[line[0]][line[1]]
    return part1(lines)

def main():
    with open("input.txt", "r") as f:
        lines = [line.strip().split() for line in f.readlines()]
        print(part1(lines)) # Part 1: 14297
        print(part2(lines)) # Part 2: 10498

if __name__ == "__main__":
    main()