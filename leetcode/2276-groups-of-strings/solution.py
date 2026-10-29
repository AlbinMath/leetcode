from typing import List

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        # Step 1: Pre-aggregate word masks and their frequencies
        mask_count = {}
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - ord('a'))
            mask_count[m] = mask_count.get(m, 0) + 1

        unique_masks = list(mask_count.keys())
        n = len(unique_masks)
        
        # Map each unique mask to an index 0 .. n-1
        mask_to_id = {m: i for i, m in enumerate(unique_masks)}

        # DSU initialized with component weights equal to mask frequencies
        parent = list(range(n))
        size = [mask_count[m] for m in unique_masks]
        num_components = n

        def find(x: int) -> int:
            root = x
            while parent[root] != root:
                root = parent[root]
            while x != root:
                nxt = parent[x]
                parent[x] = root
                x = nxt
            return root

        def union(x: int, y: int):
            nonlocal num_components
            rx, ry = find(x), find(y)
            if rx != ry:
                if size[rx] < size[ry]:
                    rx, ry = ry, rx
                parent[ry] = rx
                size[rx] += size[ry]
                num_components -= 1

        # Step 2: For each unique mask, check valid transitions
        for i, mask in enumerate(unique_masks):
            # Deletions: turn off bit b
            # (Also covers additions symmetrically between words)
            for b in range(26):
                if (mask >> b) & 1:
                    del_mask = mask ^ (1 << b)
                    if del_mask in mask_to_id:
                        union(i, mask_to_id[del_mask])

                    # Replacements: replace bit b with an unset bit j
                    for j in range(26):
                        if not ((mask >> j) & 1):
                            rep_mask = del_mask | (1 << j)
                            if rep_mask in mask_to_id:
                                union(i, mask_to_id[rep_mask])

        max_group_size = max(size[find(i)] for i in range(n))
        return [num_components, max_group_size]
