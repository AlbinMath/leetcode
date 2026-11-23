class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for pos, j in enumerate(preferences[i]):
                rank[i][j] = pos

        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        unhappy = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                if u == y:
                    break
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break
        return unhappy
