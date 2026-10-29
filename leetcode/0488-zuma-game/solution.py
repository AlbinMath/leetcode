from collections import deque
import re

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s: str) -> str:
            """Repeatedly eliminate 3 or more consecutive identical balls."""
            pattern = re.compile(r'(.)\1{2,}')
            while True:
                new_s = pattern.sub('', s)
                if len(new_s) == len(s):
                    break
                s = new_s
            return s

        init_hand = "".join(sorted(hand))
        queue = deque([(board, init_hand, 0)])
        visited = {(board, init_hand)}

        while queue:
            b, h, steps = queue.popleft()
            distinct_balls = set(h)

            for i in range(len(b) + 1):
                for ball in distinct_balls:
                    # Valid Insertion Criteria:
                    # 1. Place adjacent to a ball of the same color
                    same_color = (i > 0 and b[i - 1] == ball) or (i < len(b) and b[i] == ball)
                    
                    # 2. Split two identical balls with a different color: ...X | X... with ball Y != X
                    split_pair = (0 < i < len(b) and b[i - 1] == b[i] and b[i] != ball)

                    if not (same_color or split_pair):
                        continue

                    # Simulate move
                    new_b = clean(b[:i] + ball + b[i:])

                    if not new_b:
                        return steps + 1

                    # Remove ball from hand
                    idx = h.find(ball)
                    new_h = h[:idx] + h[idx + 1:]

                    state = (new_b, new_h)
                    if state not in visited:
                        visited.add(state)
                        queue.append((new_b, new_h, steps + 1))

        return -1
