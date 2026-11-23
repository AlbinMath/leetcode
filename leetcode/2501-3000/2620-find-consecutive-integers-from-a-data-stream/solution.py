class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.run = 0      # length of the current streak of `value`

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.run += 1
        else:
            self.run = 0
        return self.run >= self.k
