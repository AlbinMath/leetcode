class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0  # device count of the previous non-empty row
        for row in bank:
            cnt = row.count('1')
            if cnt:
                res += prev * cnt
                prev = cnt
        return res
