def main():
    levels = parse_input()
    print(len(levels))
    print(check_safeness(levels))

def check_safeness(levels):
    inc = True
    safe = 0
    for row in levels:
        diff = 0
        if row[1] - row[0] < 0:
            inc = False
        elif row[1] - row[0] > 0:
            inc = True
        for i in range(0, len(row)-1):
            diff = row[i+1] - row[i]
            if abs(diff) > 3 or diff == 0:
                break
            if inc and diff < 0:
                break
            elif not inc and diff > 0:
                break
            if i == len(row) - 2:
                safe += 1
    return safe
                



def parse_input():
    l = []
    with open("./Day2/input.txt", 'r') as f:
        l = [list(map(int, row.split())) for row in f]
    return l


if __name__ == "__main__":
    main()