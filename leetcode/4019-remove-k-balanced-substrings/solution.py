class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []  # list of [char, count]
        
        for c in s:
            if stk and stk[-1][0] == c:
                stk[-1][1] += 1
            else:
                stk.append([c, 1])
                
            if stk[-1][0] == ')' and stk[-1][1] == k:
                if len(stk) >= 2 and stk[-2][0] == '(' and stk[-2][1] >= k:
                    stk.pop()
                    stk[-1][1] -= k
                    if stk[-1][1] == 0:
                        stk.pop()
                        
        return "".join(ch * cnt for ch, cnt in stk)
