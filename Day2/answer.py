class ListIterator:
    def __init__(self, values):
        self.current = 0
        self.values = values.copy()
        self._length = len(values) 

    def __next__(self):
        self.current += 1
        if self.current < self._length:
            return self.values[self.current]
        raise StopIteration
    
    def __len__(self):
        return self._length
    
    def __getitem__(self, index):
        return self.values[index]
    
    def prev(self):
        self.current -= 1

    def has_next(self):
        if (self.current >= self._length):
            return False
        return True
    
    def remove(self, index):
        if index >= self._length or index < 0:
            raise IndexError
        self.values.pop(index)
        self._length -= 1

        

def check_safeness(levels):
    safe = 0
    for row in levels:
        r = ListIterator(row)
        warning = False
        diff = 0
        inc = True
        if row[1] - row[0] < 0:
            inc = False
        while r.has_next():
            diff = r[r.current+1] - r[r.current]
            if abs(diff) > 3 or diff == 0:
                if warning:
                    break
                warning = True
                r.remove(r.current+1)
                continue
            if inc and diff < 0:
                if warning:
                    break
                r.remove(r.current+1)
                warning = True
                continue
            elif not inc and diff > 0:
                if warning:
                    break
                r.remove(r.current+1)
                warning = True
                continue
            if r.current == len(r) - 2:
                safe += 1
                break
            next(r)
            
    return safe
                
def parse_input():
    l = []
    with open("./Day2/input.txt", 'r') as f:
        l = [list(map(int, row.split())) for row in f]
    return l

def main():
    levels = parse_input()
    print(len(levels))
    print(check_safeness(levels))


if __name__ == "__main__":
    main()