
class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        stones = sorted(range(len(aliceValues)),
                        key=lambda i: aliceValues[i] + bobValues[i],
                        reverse=True)
        score = sum((1 if t % 2 == 0 else -1) *
                    (aliceValues[i] if t % 2 == 0 else bobValues[i])
                    for t, i in enumerate(stones))
        return (score > 0) - (score < 0)

