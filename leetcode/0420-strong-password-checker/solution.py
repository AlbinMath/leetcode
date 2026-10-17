class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing = 3
        if any(c.islower() for c in password): missing -= 1
        if any(c.isupper() for c in password): missing -= 1
        if any(c.isdigit() for c in password): missing -= 1

        repl = 0
        one = two = 0  # counts of runs with L%3 == 0 and L%3 == 1
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            L = j - i
            if L >= 3:
                repl += L // 3
                if L % 3 == 0:
                    one += 1
                elif L % 3 == 1:
                    two += 1
            i = j

        if n < 6:
            return max(6 - n, missing)
        if n <= 20:
            return max(missing, repl)

        over = n - 20
        left = over
        # 1 deletion per replacement saved on L%3==0 runs
        use = min(left, one)
        repl -= use
        left -= use
        # 2 deletions per replacement saved on L%3==1 runs
        use = min(left // 2, two)
        repl -= use
        left -= use * 2
        # 3 deletions per replacement saved otherwise
        repl -= left // 3
        repl = max(repl, 0)
        return over + max(missing, repl)
