class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]          # any window crossing this zero has product 0
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):      # window includes a zero
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]
