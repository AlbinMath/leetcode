# LeetCode 3485: Longest Common Prefix of K Strings After Removal

**LeetCode Problem #3485 — Longest Common Prefix of K Strings After Removal**
Solve LeetCode Longest Common Prefix of K Strings After Removal using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Common Prefix of K Strings After Removal |
| LeetCode | #3485 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of strings `words` and an integer `k`.

For each index `i` in the range `[0, words.length - 1]`, find the **length** of the **longest common prefix ** among any `k` strings (selected at **distinct indices**) from the remaining array after removing the `i^th` element.

Return an array `answer`, where `answer[i]` is the answer for `i^th` element. If removing the `i^th` element leaves the array with fewer than `k` strings, `answer[i]` is 0.

## Constraints
- `1 <= k <= words.length <= 10^5`
- `1 <= words[i].length <= 10^4`
- `words[i]` consists of lowercase English letters.
- The sum of `words[i].length` is smaller than or equal `10^5`.

## Examples
### Example 1
- **Input:** `words = ["jump","run","run","jump","run"], k = 2`
- **Output:** `[3,4,4,3,4]`
- **Explanation:** Removing index 0 (`"jump"`):

 
 `words` becomes: `["run", "run", "jump", "run"]`. `"run"` occurs 3 times. Choosing any two gives the longest common prefix `"run"` (length 3). 
 
 
 Removing index 1 (`"run"`):
 
 `words` becomes: `["jump", "run", "jump", "run"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4). 
 
 
 Removing index 2 (`"run"`):
 
 `words` becomes: `["jump", "run", "jump", "run"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4). 
 
 
 Removing index 3 (`"jump"`):
 
 `words` becomes: `["jump", "run", "run", "run"]`. `"run"` occurs 3 times. Choosing any two gives the longest common prefix `"run"` (length 3). 
 
 
 Removing index 4 ("run"):
 
 `words` becomes: `["jump", "run", "run", "jump"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4).

### Example 2
- **Input:** `words = ["dog","racer","car"], k = 2`
- **Output:** `[0,0,0]`
- **Explanation:** Removing any index results in an answer of 0.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Common Prefix of K Strings After Removal**, we observe the problem requirements and utilize the **Prefix Sum** technique. By maintaining a **Prefix Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Prefix Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["jump","run","run","jump","run"], k = 2`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4,4,3,4]`.
4. **Verification:** Removing index 0 (`"jump"`):

 
 `words` becomes: `["run", "run", "jump", "run"]`. `"run"` occurs 3 times. Choosing any two gives the longest common prefix `"run"` (length 3). 
 
 
 Removing index 1 (`"run"`):
 
 `words` becomes: `["jump", "run", "jump", "run"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4). 
 
 
 Removing index 2 (`"run"`):
 
 `words` becomes: `["jump", "run", "jump", "run"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4). 
 
 
 Removing index 3 (`"jump"`):
 
 `words` becomes: `["jump", "run", "run", "run"]`. `"run"` occurs 3 times. Choosing any two gives the longest common prefix `"run"` (length 3). 
 
 
 Removing index 4 ("run"):
 
 `words` becomes: `["jump", "run", "run", "jump"]`. `"jump"` occurs twice. Choosing these two gives the longest common prefix `"jump"` (length 4).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        n = len(words)
        if n - 1 < k:
            return [0] * n

        # trie with counts
        nxt = [{}]
        cnt = [0]
        for w in words:
            node = 0
            for ch in w:
                c = nxt[node].get(ch)
                if c is None:
                    nxt.append({})
                    cnt.append(0)
                    c = len(nxt) - 1
                    nxt[node][ch] = c
                node = c
                cnt[node] += 1

        maxlen = max(len(w) for w in words)
        good = [0] * (maxlen + 2)      # good[d] = nodes at depth d with cnt >= k

        # compute depth of each node via BFS over the trie
        depth = [0] * len(nxt)
        stack = [0]
        while stack:
            u = stack.pop()
            for v in nxt[u].values():
                depth[v] = depth[u] + 1
                stack.append(v)
                if cnt[v] >= k:
                    good[depth[v]] += 1

        ans = [0] * n
        for i, w in enumerate(words):
            # path nodes by depth
            path = []
            node = 0
            for ch in w:
                node = nxt[node][ch]
                path.append(node)
            L = len(path)

            best = 0
            # depths beyond this word's length: only other words' nodes exist there
            for d in range(maxlen, L, -1):
                if good[d] > 0:
                    best = d
                    break
            if best == 0:
                for d in range(L, 0, -1):
                    v = path[d - 1]
                    others = good[d] - (1 if cnt[v] >= k else 0)
                    if others > 0 or cnt[v] >= k + 1:
                        best = d
                        break
            ans[i] = best
        return ans
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [3043. Find the Length of the Longest Common Prefix](../../3001-3500/3043-find-the-length-of-the-longest-common-prefix/)
- [1392. Longest Happy Prefix](../../1001-1500/1392-longest-happy-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/)
