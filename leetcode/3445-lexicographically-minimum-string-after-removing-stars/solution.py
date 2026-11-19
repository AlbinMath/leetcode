class Solution:
    def clearStars(self, s: str) -> str:
        chars = list(s)
        pos = [[] for _ in range(26)]
        
        for i, ch in enumerate(chars):
            if ch == '*':
                for c in range(26):
                    if pos[c]:
                        chars[pos[c].pop()] = '*'
                        break
            else:
                pos[ord(ch) - ord('a')].append(i)
                
        return "".join(ch for ch in chars if ch != '*')
