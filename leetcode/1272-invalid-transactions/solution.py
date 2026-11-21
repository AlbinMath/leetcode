class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))

        res = []
        for i, (name, time, amount, city) in enumerate(parsed):
            if amount > 1000:
                res.append(transactions[i])
                continue

            for j, (n2, t2, _, c2) in enumerate(parsed):
                if i != j and name == n2 and city != c2 and abs(time - t2) <= 60:
                    res.append(transactions[i])
                    break

        return res
