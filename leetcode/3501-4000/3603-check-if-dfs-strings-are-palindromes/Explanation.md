# LeetCode 3327: Check if DFS Strings Are Palindromes

**LeetCode Problem #3327 — Check if DFS Strings Are Palindromes**
Solve LeetCode Check if DFS Strings Are Palindromes using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check if DFS Strings Are Palindromes |
| LeetCode | #3327 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a tree rooted at node 0, consisting of `n` nodes numbered from `0` to `n - 1`. The tree is represented by an array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node 0 is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to node `i`.

Consider an empty string `dfsStr`, and define a recursive function `dfs(int x)` that takes a node `x` as a parameter and performs the following steps in order:

Iterate over each child `y` of `x` **in increasing order of their numbers**, and call `dfs(y)`. 
 Add the character `s[x]` to the end of the string `dfsStr`.

**Note** that `dfsStr` is shared across all recursive calls of `dfs`.

You need to find a boolean array `answer` of size `n`, where for each index `i` from `0` to `n - 1`, you do the following:

Empty the string `dfsStr` and call `dfs(i)`. 
 If the resulting string `dfsStr` is a palindrome , then set `answer[i]` to `true`. Otherwise, set `answer[i]` to `false`.

Return the array `answer`.

## Constraints
- `n == parent.length == s.length`
- `1 <= n <= 10^5`
- `0 <= parent[i] <= n - 1` for all `i >= 1`.
- `parent[0] == -1`
- `parent` represents a valid tree.
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `parent = [-1,0,0,1,1,2], s = "aababa"`
- **Output:** `[true,true,false,true,true,true]`
- **Explanation:** Calling `dfs(0)` results in the string `dfsStr = "abaaba"`, which is a palindrome. 
 Calling `dfs(1)` results in the string `dfsStr = "aba"`, which is a palindrome. 
 Calling `dfs(2)` results in the string `dfsStr = "ab"`, which is

### Example 2
- **Input:** `parent = [-1,0,0,0,0], s = "aabcb"`
- **Output:** `[true,true,true,true,true]`
- **Explanation:** Every call on `dfs(x)` results in a palindrome string.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Check if DFS Strings Are Palindromes**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `parent = [-1,0,0,1,1,2], s = "aababa"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,true,false,true,true,true]`.
4. **Verification:** Calling `dfs(0)` results in the string `dfsStr = "abaaba"`, which is a palindrome. 
 Calling `dfs(1)` results in the string `dfsStr = "aba"`, which is a palindrome. 
 Calling `dfs(2)` results in the string `dfsStr = "ab"`, which is

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)     # appended in increasing order

        # iterative post-order DFS building the global string
        start = [0] * n
        end = [0] * n
        chars = []
        stack = [(0, 0)]                      # (node, next child index)
        start[0] = 0
        while stack:
            x, idx = stack.pop()
            if idx == 0:
                start[x] = len(chars)
            if idx < len(children[x]):
                stack.append((x, idx + 1))
                stack.append((children[x][idx], 0))
            else:
                chars.append(s[x])
                end[x] = len(chars) - 1

        # Manacher on '#'-separated string
        t = '#' + '#'.join(chars) + '#'
        m = len(t)
        p = [0] * m
        c = r = 0
        for i in range(m):
            if i < r:
                p[i] = min(r - i, p[2 * c - i])
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < m and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]

        ans = [False] * n
        for x in range(n):
            l, rr = start[x], end[x]
            ans[x] = p[l + rr + 1] >= rr - l + 1
        return ans
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [1437. Check If All 1's Are at Least Length K Places Away](../../1501-2000/1548-check-if-all-1s-are-at-least-length-k-places-away/)
- [1657. Determine if Two Strings Are Close](../../1501-2000/1777-determine-if-two-strings-are-close/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/)
