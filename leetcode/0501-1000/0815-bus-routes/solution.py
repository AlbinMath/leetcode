from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        g = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                g[stop].append(i)

        q, seen = deque([(source, 0)]), {source}
        buses = set()

        while q:
            stop, cnt = q.popleft()
            for bus in g[stop]:
                if bus in buses:
                    continue
                buses.add(bus)
                for nxt in routes[bus]:
                    if nxt == target:
                        return cnt + 1
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, cnt + 1))
        return -1
