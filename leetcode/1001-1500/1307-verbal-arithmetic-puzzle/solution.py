class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        if max(len(w) for w in words) > len(result):
            return False

        L = len(result)
        leading = set()
        for w in words + [result]:
            if len(w) > 1:
                leading.add(w[0])

        # reversed strings so index = column from the right
        rev_words = [w[::-1] for w in words]
        rev_res = result[::-1]

        assign = {}          # letter -> digit
        used = [False] * 10

        def solve(col: int, wi: int, carry: int, total: int) -> bool:
            # col: current column, wi: next word index to process in this column
            # total: running sum of word digits in this column (plus carry)
            if col == L:
                return carry == 0

            if wi < len(rev_words):
                w = rev_words[wi]
                if col >= len(w):
                    return solve(col, wi + 1, carry, total)
                ch = w[col]
                if ch in assign:
                    return solve(col, wi + 1, carry, total + assign[ch])
                for d in range(10):
                    if used[d] or (d == 0 and ch in leading):
                        continue
                    used[d] = True
                    assign[ch] = d
                    if solve(col, wi + 1, carry, total + d):
                        return True
                    del assign[ch]
                    used[d] = False
                return False

            # all words handled for this column: check the result digit
            s = total + carry
            ch = rev_res[col]
            need = s % 10
            if ch in assign:
                if assign[ch] != need:
                    return False
                return solve(col + 1, 0, s // 10, 0)
            if used[need] or (need == 0 and ch in leading):
                return False
            used[need] = True
            assign[ch] = need
            if solve(col + 1, 0, s // 10, 0):
                return True
            del assign[ch]
            used[need] = False
            return False

        return solve(0, 0, 0, 0)
