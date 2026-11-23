class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        answer = [""] * n

        athletes = []

        for i in range(n):
            athletes.append((score[i], i))

        athletes.sort(reverse=True)

        for rank in range(n):
            index = athletes[rank][1]

            if rank == 0:
                answer[index] = "Gold Medal"
            elif rank == 1:
                answer[index] = "Silver Medal"
            elif rank == 2:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(rank + 1)

        return answer
