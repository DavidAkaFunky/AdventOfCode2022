def solve(line, length):
    for i in range(len(line)-length+1):
        if len(set(line[i:i+length])) == length:
            return i+length

def main():
    with open("input.txt", "r") as f:
        line = f.readline().strip()
        print(solve(line, 4)) # Part 1: 1987
        print(solve(line, 14)) # Part 2: 3059

if __name__ == "__main__":
    main()