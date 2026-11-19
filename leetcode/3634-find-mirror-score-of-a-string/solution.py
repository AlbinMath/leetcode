class Solution:
    def calculateScore(self, s: str) -> int:
        score = 0
        unmarked = [[] for _ in range(26)]
        
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            mirror = 25 - c
            
            if unmarked[mirror]:
                j = unmarked[mirror].pop()
                score += i - j
            else:
                unmarked[c].append(i)
                
        return score
