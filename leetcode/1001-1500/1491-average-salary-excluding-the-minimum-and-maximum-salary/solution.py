class Solution:
    def average(self, salary: list[int]) -> float:
        total = sum(salary)
        minimum = min(salary)
        maximum = max(salary)

        return (total - minimum - maximum) / (len(salary) - 2)
