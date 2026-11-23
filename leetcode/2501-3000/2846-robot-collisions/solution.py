from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        order = sorted(range(len(positions)), key=lambda i: positions[i])
        stk = []
        
        for idx in order:
            if directions[idx] == 'R':
                stk.append(idx)
            else:
                while stk and healths[idx] > 0:
                    top = stk[-1]
                    if healths[top] < healths[idx]:
                        healths[top] = 0
                        stk.pop()
                        healths[idx] -= 1
                    elif healths[top] > healths[idx]:
                        healths[idx] = 0
                        healths[top] -= 1
                    else:
                        healths[top] = 0
                        healths[idx] = 0
                        stk.pop()
                        
        return [h for h in healths if h > 0]
