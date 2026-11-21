from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for entry in paths:
            directory, *files = entry.split(' ')
            for f in files:
                open_idx = f.index('(')
                name = f[:open_idx]
                content = f[open_idx + 1:-1]  # drop the trailing ')'
                groups[content].append(f"{directory}/{name}")

        return [g for g in groups.values() if len(g) > 1]
