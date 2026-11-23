class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        count = {ch: [0] * n for ch in votes[0]}

        for vote in votes:
            for pos, ch in enumerate(vote):
                count[ch][pos] += 1

        teams = sorted(count, key=lambda ch: ([-c for c in count[ch]], ch))
        return ''.join(teams)
