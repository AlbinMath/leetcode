class Solution:
    def findEvenNumbers(self, digits):
        s = set(digits)
        ans = set()
        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):
                    num = [a, b, c]
                    d = digits.copy()
                    if all(num.count(x) <= d.count(x) for x in set(num)):
                        ans.add(a * 100 + b * 10 + c)
        return sorted(ans)
