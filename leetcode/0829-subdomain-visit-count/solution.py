from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)

        for entry in cpdomains:
            rep, domain = entry.split(' ')
            rep = int(rep)
            labels = domain.split('.')

            for i in range(len(labels)):
                counts['.'.join(labels[i:])] += rep

        return [f"{c} {d}" for d, c in counts.items()]
