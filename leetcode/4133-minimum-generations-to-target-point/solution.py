class Solution:
    def minGenerations(self, points: list[list[int]], target: list[int]) -> int:
        t = tuple(target)
        have = set(map(tuple, points))
        if t in have:
            return 0

        k = 0
        while True:
            k += 1
            pts = list(have)
            new = set()
            for i in range(len(pts)):
                a = pts[i]
                for j in range(i + 1, len(pts)):
                    b = pts[j]
                    c = ((a[0] + b[0]) // 2,
                         (a[1] + b[1]) // 2,
                         (a[2] + b[2]) // 2)
                    if c not in have:
                        new.add(c)
            if not new:
                return -1
            if t in new:
                return k
            have |= new
