class Solution:
    def specialPalindrome(self, n: int) -> int:
        # group valid digit subsets by their total length
        by_len = {}
        for m in range(1, 1 << 9):
            ds = [i + 1 for i in range(9) if m >> i & 1]
            if sum(d & 1 for d in ds) <= 1:
                by_len.setdefault(sum(ds), []).append(ds)

        def first_above(ds, n):
            cnt = [0] * 10
            mid = ""
            for d in ds:
                cnt[d] = d // 2
                if d & 1:
                    mid = str(d)
            half_len = sum(cnt)

            def gen(cur):
                if len(cur) == half_len:
                    h = "".join(cur)
                    yield int(h + mid + h[::-1])
                    return
                for d in range(1, 10):
                    if cnt[d]:
                        cnt[d] -= 1
                        cur.append(str(d))
                        yield from gen(cur)
                        cur.pop()
                        cnt[d] += 1

            for v in gen([]):
                if v > n:
                    return v
            return None

        for L in range(len(str(n)), 46):
            best = None
            for ds in by_len.get(L, []):
                v = first_above(ds, n)
                if v is not None and (best is None or v < best):
                    best = v
            if best is not None:
                return best
        return -1
