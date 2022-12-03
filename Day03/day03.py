def priority(char):
    value = ord(char)
    return value - 38 if value in range(65, 91) else value - 96

def part1(lines):
    total = 0
    for line in lines:
        left = line[:len(line)//2]
        right = line[len(line)//2:]
        for char in list(set(left) & set(right)):
            total += priority(char)
    return total

def part2(lines):
    total = 0
    for i in range(0, len(lines), 3):
        for char in list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2])):
            total += priority(char)
    return total

def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        print(part1(lines)) # Part 1: 7997
        print(part2(lines)) # Part 2: 2545

if __name__ == "__main__":
    main()