def parse_input():
    l = []
    with open("./Day4/input.txt", 'r') as f:
        for row in f:
            l.append(row)
    return l

def word_search(ws):
    count = 0
    for j in range(0, len(ws)):
        for i in range(0, len(ws[j])):
            ch = ws[j][i]
            if ch == 'X':
                count += check_xmas(ws, i, j, -1, -1)
                count += check_xmas(ws, i, j, -1, 0)
                count += check_xmas(ws, i, j, -1, 1)
                count += check_xmas(ws, i, j, 0, -1)
                count += check_xmas(ws, i, j, 0, 1)
                count += check_xmas(ws, i, j, 1, -1)
                count += check_xmas(ws, i, j, 1, 0)
                count += check_xmas(ws, i, j, 1, 1)
    return count
                
def check_xmas(ws, i, j, x, y, word=''):
    if j < 0 or j >= len(ws):
        return 0
    if i < 0 or i >= len(ws[j]):
        return 0
    ch = ws[j][i]
    new_word = word + ch
    if ch == "X" or ch == "M" or ch == "A":
        return check_xmas(ws, i+x, j+y, x, y, new_word)
    elif ch == "S":
        if new_word == "XMAS":
            return 1
    return 0

def main():
    ws = parse_input()
    print(word_search(ws))

if __name__ == "__main__":
    main()