from collections import deque

class Solution(object):
    def findLexSmallestString(self, s, a, b):
        visited = {s}
        queue = deque([s])
        smallest = s
        n = len(s)
        
        while queue:
            curr = queue.popleft()
            if curr < smallest:
                smallest = curr
            
            # Operation 1: Add 'a' to all odd indices
            chars = list(curr)
            for i in range(1, n, 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = "".join(chars)
            if added not in visited:
                visited.add(added)
                queue.append(added)
                
            # Operation 2: Rotate right by 'b' positions
            rotated = curr[-b:] + curr[:-b]
            if rotated not in visited:
                visited.add(rotated)
                queue.append(rotated)
                
        return smallest
