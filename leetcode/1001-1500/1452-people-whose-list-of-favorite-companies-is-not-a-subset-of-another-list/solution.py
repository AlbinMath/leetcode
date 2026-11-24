class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(f) for f in favoriteCompanies]
        n = len(sets)
        res = []

        for i in range(n):
            is_subset = False
            for j in range(n):
                if i != j and len(sets[i]) <= len(sets[j]) and sets[i] <= sets[j]:
                    is_subset = True
                    break
            if not is_subset:
                res.append(i)

        return res
