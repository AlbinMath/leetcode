from collections import Counter, defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = defaultdict(Counter)

        for _, table, food in orders:
            foods.add(food)
            tables[int(table)][food] += 1

        menu = sorted(foods)
        res = [["Table"] + menu]

        for t in sorted(tables):
            res.append([str(t)] + [str(tables[t][f]) for f in menu])

        return res
