class Solution(object):
    def maximumXor(self, s, t):
        cnt = [t.count('0'), t.count('1')]
        res = []
        for ch in s:
            want = 1 - int(ch)  # bit of t that makes the XOR bit 1
            if cnt[want] > 0:
                cnt[want] -= 1
                res.append('1')
            else:
                cnt[1 - want] -= 1
                res.append('0')
        return ''.join(res)
