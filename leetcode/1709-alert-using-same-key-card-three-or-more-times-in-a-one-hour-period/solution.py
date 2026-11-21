from collections import defaultdict

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = defaultdict(list)
        for name, t in zip(keyName, keyTime):
            h, m = t.split(':')
            times[name].append(int(h) * 60 + int(m))

        res = []
        for name, ts in times.items():
            ts.sort()
            for i in range(len(ts) - 2):
                if ts[i + 2] - ts[i] <= 60:
                    res.append(name)
                    break

        return sorted(res)
