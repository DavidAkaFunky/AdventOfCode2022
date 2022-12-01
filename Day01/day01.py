def solve(lines):
    totals = []
    total = 0
    for line in lines:
        line = line.strip()
        if line == "":
            totals.append(total)
            total = 0
        else:
            total += int(line)
    return sorted(totals)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        totals = solve(lines)
        print(totals[-1]) # Part 1: 71471
        print(totals[-1] + totals[-2] + totals[-3]) # Part 2: 211189

if __name__ == "__main__":
    main()