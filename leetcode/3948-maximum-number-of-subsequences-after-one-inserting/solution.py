class Solution:
    def numOfSubsequences(self, s: str) -> int:
        total_T = s.count('T')
        l = lc = lct = 0
        for ch in s:
            if ch == 'L':
                l += 1
            elif ch == 'C':
                lc += l
            elif ch == 'T':
                lct += lc
        LC_total = lc

        c = ct = 0
        for ch in reversed(s):
            if ch == 'T':
                pass
            elif ch == 'C':
                c += 1
        cnt_c = 0
        CT_total = 0
        for ch in s:
            if ch == 'C':
                cnt_c += 1
            elif ch == 'T':
                CT_total += cnt_c
        best_c = 0
        l_before = 0
        t_after = total_T
        for ch in s:
            best_c = max(best_c, l_before * t_after)  # gap before this char
            if ch == 'L':
                l_before += 1
            elif ch == 'T':
                t_after -= 1
        best_c = max(best_c, l_before * t_after)  # gap at the end

        return lct + max(CT_total, LC_total, best_c)
