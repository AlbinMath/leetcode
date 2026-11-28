# LeetCode 3863: Minimum Operations to Sort a String

**LeetCode Problem #3863 — Minimum Operations to Sort a String**
Solve LeetCode Minimum Operations to Sort a String using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Sort a String |
| LeetCode | #3863 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters.

In one operation, you can select any ** substring ** of `s` that is **not** the entire string and **sort** it in **non-descending alphabetical** order.

Return the **minimum** number of operations required to make `s` sorted in **non-descending** order. If it is not possible, return -1.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "dog"`
- **Output:** `1`
- **Explanation:** ​​​​​​​ 

 
 Sort substring `"og"` to `"go"`. 
 Now, `s = "dgo"`, which is sorted in ascending order. Thus, the answer is 1.

### Example 2
- **Input:** `s = "card"`
- **Output:** `2`
- **Explanation:** Sort substring `"car"` to `"acr"`, so `s = "acrd"`. 
 Sort substring `"rd"` to `"dr"`, making `s = "acdr"`, which is sorted in ascending order. Thus, the answer is 2.

### Example 3
- **Input:** `s = "gf"`
- **Output:** `-1`
- **Explanation:** It is impossible to sort `s` under the given

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Operations to Sort a String**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "dog"`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** ​​​​​​​ 

 
 Sort substring `"og"` to `"go"`. 
 Now, `s = "dgo"`, which is sorted in ascending order. Thus, the answer is 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0
        if n == 2:
            return -1
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        # s[0] strictly greater than all others, s[-1] strictly smaller than all others
        if s[0] == mx and s.count(mx) == 1 and s[-1] == mn and s.count(mn) == 1:
            return 3
        return 2
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1585. Check If String Is Transformable With Substring Sort Operations](../../1501-2000/1585-check-if-string-is-transformable-with-substring-sort-operations/)
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1830-minimum-number-of-operations-to-make-string-sorted/)
- [3223. Minimum Length of String After Operations](../../3001-3500/3223-minimum-length-of-string-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-string/)
