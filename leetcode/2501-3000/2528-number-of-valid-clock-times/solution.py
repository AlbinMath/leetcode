class Solution(object):
    def countTime(self, time):
        h1, h2, _, m1, m2 = time

        if h1 == '?' and h2 == '?':
            hours = 24
        elif h1 == '?':
            hours = 3 if h2 <= '3' else 2
        elif h2 == '?':
            hours = 4 if h1 == '2' else 10
        else:
            hours = 1

        minutes = (6 if m1 == '?' else 1) * (10 if m2 == '?' else 1)
        return hours * minutes
