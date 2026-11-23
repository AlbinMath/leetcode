class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = set()
        next_k = {}
        res = []

        for name in names:
            if name not in used:
                used.add(name)
                res.append(name)
                continue

            k = next_k.get(name, 1)
            while f"{name}({k})" in used:
                k += 1
            new_name = f"{name}({k})"
            used.add(new_name)
            next_k[name] = k + 1
            res.append(new_name)

        return res
