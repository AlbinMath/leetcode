class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        total = [[0] * n for _ in range(m)]
        cnt = [[0] * n for _ in range(m)]

        for i in range(m - 2):
            for j in range(n - 2):
                ok = True
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if y + 1 < j + 3 and abs(image[x][y] - image[x][y + 1]) > threshold:
                            ok = False
                            break
                        if x + 1 < i + 3 and abs(image[x][y] - image[x + 1][y]) > threshold:
                            ok = False
                            break
                    if not ok:
                        break
                if not ok:
                    continue

                avg = sum(image[x][y] for x in range(i, i + 3) for y in range(j, j + 3)) // 9
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        total[x][y] += avg
                        cnt[x][y] += 1

        return [
            [total[i][j] // cnt[i][j] if cnt[i][j] else image[i][j] for j in range(n)]
            for i in range(m)
        ]
