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
                    #print("Fail: Difference out of range")
                    break
                warning = True
                r.remove(r.current+1)
                #print("Warning: Difference out of range")
                continue
            if inc and diff < 0:
                if warning:
                    #print("Fail: Switched from inc to dec")
                    break
                r.remove(r.current+1)
                warning = True
                #print("Warning: Switched from inc to dec")
                continue
            elif not inc and diff > 0:
                if warning:
                    #print("Fail: Switched from dec to inc")
                    break
                r.remove(r.current+1)
                warning = True
                #print("Warning: Switched from dec to inc")
                continue
            if r.current == len(r) - 2:
                safe += 1
                #print("Pass")
                break
            next(r)
            
            
    return safe
                
def parse_input():
    l = []
    with open("./Day2/input.txt", 'r') as f:
        l = [list(map(int, row.split())) for row in f]
    return l

def main():
    #test = [[9,5,1,5],
    #         [1,2,3,4],
    #         [-3,-7,-6,-2],
    #         [1,3,6,12,9],
    #         [2,2,4,6,8,10,10]]
    levels = parse_input()
    print(check_safeness(levels))


if __name__ == "__main__":
    main()