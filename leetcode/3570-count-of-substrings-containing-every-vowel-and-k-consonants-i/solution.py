class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = "aeiou"
        ans = 0
        for i in range(n):
            seen = set()
            cons = 0
            for j in range(i, n):
                ch = word[j]
                if ch in vowels:
                    seen.add(ch)
                else:
                    cons += 1
                    if cons > k:
                        break
                if cons == k and len(seen) == 5:
                    ans += 1
        return ans
