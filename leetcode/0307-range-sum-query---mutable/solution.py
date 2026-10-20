class NumArray:
    def __init__(self, nums: List[int]):
        self.a = nums[:]
        self.n = len(nums)
        self.bit = [0] * (self.n + 1)
        for i, x in enumerate(nums):
            self.add(i + 1, x)

    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & -i

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.a[index])
        self.a[index] = val

    def sumRange(self, left: int, right: int) -> int:
        def query(i):
            s = 0
            while i:
                s += self.bit[i]
                i -= i & -i
            return s
        return query(right + 1) - query(left)
