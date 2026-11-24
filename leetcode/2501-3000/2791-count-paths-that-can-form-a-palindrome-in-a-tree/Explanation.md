# LeetCode 2791: Count Paths That Can Form a Palindrome in a Tree

**LeetCode Problem #2791 — Count Paths That Can Form a Palindrome in a Tree**
Solve LeetCode Count Paths That Can Form a Palindrome in a Tree using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Paths That Can Form a Palindrome in a Tree |
| LeetCode | #2791 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **tree** (i.e. a connected, undirected graph that has no cycles) **rooted** at node `0` consisting of `n` nodes numbered from `0` to `n - 1`. The tree is represented by a **0-indexed** array `parent` of size `n`, where `parent[i]` is the parent of node `i`. Since node `0` is the root, `parent[0] == -1`.

You are also given a string `s` of length `n`, where `s[i]` is the character assigned to the edge between `i` and `parent[i]`. `s[0]` can be ignored.

Return *the number of pairs of nodes *`(u, v)`* such that *`u < v`* and the characters assigned to edges on the path from *`u`* to *`v`* can be **rearranged** to form a **palindrome***.

A string is a **palindrome** when it reads the same backwards as forwards.

## Constraints
- `n == parent.length == s.length`
- `1 <= n <= 10^5`
- `0 <= parent[i] <= n - 1` for all `i >= 1`
- `parent[0] == -1`
- `parent` represents a valid tree.
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `parent = [-1,0,0,1,1,2], s = "acaabc"`
- **Output:** `8`
- **Explanation:** The valid pairs are:
- All the pairs (0,1), (0,2), (1,3), (1,4) and (2,5) result in one character which is always a palindrome.
- The pair (2,3) result in the string "aca" which is a palindrome.
- The pair (1,5) result in the string "cac" which is a palindrome.
- The pair (3,5) result in the string "acac" which can be rearranged into the palindrome "acca".

### Example 2
- **Input:** `parent = [-1,0,0,0,0], s = "aaaaa"`
- **Output:** `10`
- **Explanation:** Any pair of nodes (u,v) where u < v is valid.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Count Paths That Can Form a Palindrome in a Tree**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `parent = [-1,0,0,1,1,2], s = "acaabc"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The valid pairs are:
- All the pairs (0,1), (0,2), (1,3), (1,4) and (2,5) result in one character which is always a palindrome.
- The pair (2,3) result in the string "aca" which is a palindrome.
- The pair (1,5) result in the string "cac" which is a palindrome.
- The pair (3,5) result in the string "acac" which can be rearranged into the palindrome "acca".

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
class Solution(object):
    def countPalindromePaths(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        mask = [0] * n
        order = [0]
        for u in order:  # BFS; appending while iterating is fine
            for v in children[u]:
                mask[v] = mask[u] ^ (1 << (ord(s[v]) - 97))
                order.append(v)

        cnt = {}
        ans = 0
        for m in mask:
            ans += cnt.get(m, 0)
            for c in range(26):
                ans += cnt.get(m ^ (1 << c), 0)
            cnt[m] = cnt.get(m, 0) + 1
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
- [1442. Count Triplets That Can Form Two Arrays of Equal XOR](../../1001-1500/1442-count-triplets-that-can-form-two-arrays-of-equal-xor/)
- [1725. Number Of Rectangles That Can Form The Largest Square](../../1501-2000/1725-number-of-rectangles-that-can-form-the-largest-square/)
- [2201. Count Artifacts That Can Be Extracted](../../2001-2500/2201-count-artifacts-that-can-be-extracted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/)
