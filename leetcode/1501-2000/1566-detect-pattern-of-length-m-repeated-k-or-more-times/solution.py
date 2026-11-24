class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        n = len(arr)

        for i in range(n - m * k + 1):
            count = 0

            for j in range(m * (k - 1)):
                if arr[i + j] == arr[i + j + m]:
                    count += 1
                else:
                    break

            if count == m * (k - 1):
                return True

        return False
