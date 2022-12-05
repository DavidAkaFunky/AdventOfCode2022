def solve(lines, reverse):
    i = 0
    towers = [[] for _ in range(len(lines[0]) // 4)]
    while ord(lines[i][1]) not in range(ord("0"), ord("9") + 1):
        for j in range(1, len(lines[i]), 4):
            char = lines[i][j]
            if ord(char) in range(65, 91):
                towers[j//4].append(char)
        i += 1
    i += 2
    for k in range(i, len(lines)):
        line = lines[k].split()
        qty, origin, target = int(line[1]), int(line[3])-1, int(line[5])-1
        extracted = towers[origin][:qty]
        if reverse:
            extracted.reverse()
        towers[target] = extracted + towers[target]
        towers[origin] = towers[origin][qty:]
    return "".join(tower[0] for tower in towers)

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        print(solve(lines, True)) # Part 1: PSNRGBTFT
        print(solve(lines, False)) # Part 2: BNTZFPMMW

if __name__ == "__main__":
    main()
