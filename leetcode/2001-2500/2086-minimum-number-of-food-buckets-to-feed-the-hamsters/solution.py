class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        s = list(hamsters)
        n = len(s)
        count = 0
        i = 0
        while i < n:
            if s[i] == 'H':
                if i + 1 < n and s[i + 1] == '.':
                    count += 1
                    i += 3  # bucket at i+1 feeds i and i+2; next unfed candidate is i+3
                    continue
                elif i - 1 >= 0 and s[i - 1] == '.':
                    count += 1
                else:
                    return -1
            i += 1
        return count
