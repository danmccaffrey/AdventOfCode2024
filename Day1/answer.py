def main():
    lists = parse_input()
    lists[0].sort()
    lists[1].sort()
    print(list_sim(lists[0], lists[1]))


def list_diff(list1, list2):
    diff = 0
    for i in range(0, len(list1)):
        diff += abs(list1[i] - list2[i])
    return diff

def list_sim(list1, list2):
    sim = 0
    i = 0
    j = 0
    count = 0
    while True:
        if i == len(list1):
            break
        if list1[i] == list2[j]:
            count += 1
            j += 1
        else:
            if list1[i] > list2[j]:
                j += 1
            else:
                sim += list1[i] * count
                i += 1
            count = 0

    return sim


def parse_input():
    list1 = []
    list2 = []
    with open("./Day1/input.txt", 'r') as f:
        for row in f.readlines():
            items = row.split()
            list1.append(int(items[0]))
            list2.append(int(items[1]))
    return (list1, list2)


if __name__ == "__main__":
    main()