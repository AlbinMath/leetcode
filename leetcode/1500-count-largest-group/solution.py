from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = Counter()

        for num in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(num))
            groups[digit_sum] += 1

        largest = max(groups.values())

        return sum(1 for size in groups.values() if size == largest)
