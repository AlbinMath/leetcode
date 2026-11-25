# LeetCode 2156: Find Substring With Given Hash Value

**LeetCode Problem #2156 — Find Substring With Given Hash Value**
Solve LeetCode Find Substring With Given Hash Value using Python and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Substring With Given Hash Value |
| LeetCode | #2156 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The hash of a **0-indexed** string `s` of length `k`, given integers `p` and `m`, is computed using the following function:

`hash(s, p, m) = (val(s[0]) * p^0 + val(s[1]) * p^1 + ... + val(s[k-1]) * p^k-1) mod m`.

Where `val(s[i])` represents the index of `s[i]` in the alphabet from `val('a') = 1` to `val('z') = 26`.

You are given a string `s` and the integers `power`, `modulo`, `k`, and `hashValue.` Return `sub`,* the **first** **substring** of *`s`* of length *`k`* such that *`hash(sub, power, modulo) == hashValue`.

The test cases will be generated such that an answer always **exists**.

A substring is a contiguous non-empty sequence of characters within a string.

## Constraints
- `1 <= k <= s.length <= 2 * 10^4`
- `1 <= power, modulo <= 10^9`
- `0 <= hashValue < modulo`
- `s` consists of lowercase English letters only.
- The test cases are generated such that an answer always **exists**.

## Examples
### Example 1
- **Input:** `s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0`
- **Output:** `"ee"`
- **Explanation:** The hash of "ee" can be computed to be hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0. 
"ee" is the first substring of length 2 with hashValue 0. Hence, we return "ee".

### Example 2
- **Input:** `s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32`
- **Output:** `"fbx"`
- **Explanation:** The hash of "fbx" can be computed to be hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 31^2) mod 100 = 23132 mod 100 = 32. 
The hash of "bxz" can be computed to be hash("bxz", 31, 100) = (2 * 1 + 24 * 31 + 26 * 31^2) mod 100 = 25732 mod 100 = 32. 
"fbx" is the first substring of length 3 with hashValue 32. Hence, we return "fbx".
Note that "bxz" also has a hash of 32 but it appears later than "fbx".

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Find Substring With Given Hash Value**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"ee"`.
4. **Verification:** The hash of "ee" can be computed to be hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0. 
"ee" is the first substring of length 2 with hashValue 0. Hence, we return "ee".

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        val = lambda ch: ord(ch) - 96

        pk = pow(power, k - 1, modulo)       # p^(k-1) mod m

        # hash of the last window s[n-k:], computed directly
        h = 0
        for i in range(n - 1, n - k - 1, -1):
            h = (h * power + val(s[i])) % modulo   # Horner, highest power first

        best = n - k if h == hashValue else -1

        for i in range(n - k - 1, -1, -1):
            h = ((h - val(s[i + k]) * pk) * power + val(s[i])) % modulo
            if h == hashValue:
                best = i                        # smaller index overrides

        return s[best:best + k]
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [1371. Find the Longest Substring Containing Vowels in Even Counts](../../1001-1500/1371-find-the-longest-substring-containing-vowels-in-even-counts/)
- [1456. Maximum Number of Vowels in a Substring of Given Length](../../1001-1500/1456-maximum-number-of-vowels-in-a-substring-of-given-length/)
- [1542. Find Longest Awesome Substring](../../1501-2000/1542-find-longest-awesome-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-substring-with-given-hash-value/)
