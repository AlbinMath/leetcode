import heapq

class Loc:
    __slots__ = ("score", "name")

    def __init__(self, score: int, name: str):
        self.score = score
        self.name = name

    def better(self, other) -> bool:
        if self.score != other.score:
            return self.score > other.score
        return self.name < other.name


class Best(Loc):          # best on top (for `rest`)
    def __lt__(self, other):
        return self.better(other)


class Worst(Loc):         # worst on top (for `top`)
    def __lt__(self, other):
        return other.better(self)


class SORTracker:
    def __init__(self):
        self.top = []     # Worst-ordered: locations already returned
        self.rest = []    # Best-ordered: locations not yet returned

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.top, Worst(score, name))
        w = heapq.heappop(self.top)
        heapq.heappush(self.rest, Best(w.score, w.name))

    def get(self) -> str:
        b = heapq.heappop(self.rest)
        heapq.heappush(self.top, Worst(b.score, b.name))
        return b.name
