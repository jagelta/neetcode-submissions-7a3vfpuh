class MinStack:
    def __init__(self):
        self.l = []
        self.min = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        

    def pop(self) -> None:
        val = self.l[-1]
        self.l = self.l[:len(self.l)-1]
        if val == self.min[-1]:
            self.min = self.min[:len(self.min)-1]
            

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.min[-1]
