from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.q = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.total += val

        while len(self.q) > self.window_size:
            self.total -= self.q[0]
            self.q.popleft()
            
        return self.total / len(self.q)
    

def main():
    mvg = MovingAverage(3)
    print(mvg.next(1))
    print(mvg.next(10))
    print(mvg.next(3))
    print(mvg.next(3))

if __name__ == "__main__":
    main()
    
