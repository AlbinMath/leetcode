class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        idx = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        stage = [0] * 4  # frogs currently waiting after c, r, o, a
        active = 0       # frogs currently mid-croak
        best = 0

        for ch in croakOfFrogs:
            i = idx[ch]
            if i == 0:
                stage[0] += 1
                active += 1
                best = max(best, active)
            else:
                if stage[i - 1] == 0:
                    return -1
                stage[i - 1] -= 1
                if i < 4:
                    stage[i] += 1
                else:
                    active -= 1

        return best if active == 0 else -1
