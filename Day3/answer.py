import re

def l_to_str(lst):
    result = ""
    for item in lst:
        result += f"{item}\n"
    return result

def parse_input():
    l = ""
    with open("./Day3/input.txt", 'r') as f:
        for line in f:
            l += line
    return l

def multiply(input):
    input_str = re.findall("mul\(\d+,\d+\)", input)
    total = 0
    for s in input_str:
        ops = re.findall("\d+", s)
        total += int(ops[0]) * int(ops[1])
    return total

def main():
    print(multiply(parse_input()))

if __name__ == "__main__":
    main()        