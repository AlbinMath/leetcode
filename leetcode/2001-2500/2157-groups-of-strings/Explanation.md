# LeetCode 2157: Groups of Strings

**LeetCode Problem #2157 — Groups of Strings**
Solve LeetCode Groups of Strings using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Groups of Strings |
| LeetCode | #2157 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** array of strings `words`. Each string consists of **lowercase English letters** only. No letter occurs more than once in any string of `words`.

Two strings `s1` and `s2` are said to be **connected** if the set of letters of `s2` can be obtained from the set of letters of `s1` by any **one** of the following operations:

Adding exactly one letter to the set of the letters of `s1`. 
 Deleting exactly one letter from the set of the letters of `s1`. 
 Replacing exactly one letter from the set of the letters of `s1` with any letter, **including** itself.

The array `words` can be divided into one or more non-intersecting **groups**. A string belongs to a group if any **one** of the following is true:

It is connected to **at least one** other string of the group. 
 It is the **only** string present in the group.

Note that the strings in `words` should be grouped in such a manner that a string belonging to a group cannot be connected to a string present in any other group. It can be proved that such an arrangement is always unique.

Return *an array* `ans` *of size* `2` *where:*

`ans[0]` *is the **maximum number** of groups* `words` *can be divided into, and* 
 `ans[1]` *is the **size of the largest** group*.

## Constraints
- `1 <= words.length <= 2 * 10^4`
- `1 <= words[i].length <= 26`
- `words[i]` consists of lowercase English letters only.
- No letter occurs more than once in `words[i]`.

## Examples
### Example 1
- **Input:** `words = ["a","b","ab","cde"]`
- **Output:** `[2,3]`
- **Explanation:** - words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2].
- words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2].
- words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by deleting 'a'). So words[2] is connected to words[0] and words[1].
- words[3] is not connected to any string in words.
Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size of the largest group is 3.

### Example 2
- **Input:** `words = ["a","ab","abc"]`
- **Output:** `[1,3]`
- **Explanation:** - words[0] is connected to words[1].
- words[1] is connected to words[0] and words[2].
- words[2] is connected to words[1].
Since all strings are connected to each other, they should be grouped together.
Thus, the size of the largest group is 3.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Groups of Strings**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["a","b","ab","cde"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3]`.
4. **Verification:** - words[0] can be used to obtain words[1] (by replacing 'a' with 'b'), and words[2] (by adding 'b'). So words[0] is connected to words[1] and words[2].
- words[1] can be used to obtain words[0] (by replacing 'b' with 'a'), and words[2] (by adding 'a'). So words[1] is connected to words[0] and words[2].
- words[2] can be used to obtain words[0] (by deleting 'b'), and words[1] (by deleting 'a'). So words[2] is connected to words[0] and words[1].
- words[3] is not connected to any string in words.
Thus, words can be divided into 2 groups ["a","b","ab"] and ["cde"]. The size of the largest group is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
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
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [893. Groups of Special-Equivalent Strings](../../0501-1000/0893-groups-of-special-equivalent-strings/)
- [830. Positions of Large Groups](../../0501-1000/0830-positions-of-large-groups/)
- [839. Similar String Groups](../../0501-1000/0839-similar-string-groups/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/groups-of-strings/)
