class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x: str) -> str:
        if self.parent.setdefault(x, x) != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: str, y: str):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        email_to_name = {}

        # 1. Connect emails within the same account
        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                email_to_name[email] = name
                dsu.union(first_email, email)

        # 2. Group emails by their connected component root
        groups = collections.defaultdict(list)
        for email in email_to_name:
            root = dsu.find(email)
            groups[root].append(email)

        # 3. Format and sort
        res = []
        for root, emails in groups.items():
            res.append([email_to_name[root]] + sorted(emails))

        return res
