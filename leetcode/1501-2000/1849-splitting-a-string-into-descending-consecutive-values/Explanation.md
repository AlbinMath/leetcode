# LeetCode 1849: Splitting a String Into Descending Consecutive Values

**LeetCode Problem #1849 — Splitting a String Into Descending Consecutive Values**
Solve LeetCode Splitting a String Into Descending Consecutive Values using Python and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Splitting a String Into Descending Consecutive Values |
| LeetCode | #1849 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` that consists of only digits.

Check if we can split `s` into **two or more non-empty substrings** such that the **numerical values** of the substrings are in **descending order** and the **difference** between numerical values of every two **adjacent** **substrings** is equal to `1`.

For example, the string `s = "0090089"` can be split into `["0090", "089"]` with numerical values `[90,89]`. The values are in descending order and adjacent values differ by `1`, so this way is valid. 
 Another example, the string `s = "001"` can be split into `["0", "01"]`, `["00", "1"]`, or `["0", "0", "1"]`. However all the ways are invalid because they have numerical values `[0,1]`, `[0,1]`, and `[0,0,1]` respectively, all of which are not in descending order.

Return `true` *if it is possible to split* `s`​​​​​​ *as described above**, or *`false`* otherwise.*

A **substring** is a contiguous sequence of characters in a string.

## Constraints
- `1 <= s.length <= 20`
- `s` only consists of digits.

## Examples
### Example 1
- **Input:** `s = "1234"`
- **Output:** `false`
- **Explanation:** There is no valid way to split s.

### Example 2
- **Input:** `s = "050043"`
- **Output:** `true`
- **Explanation:** s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

### Example 3
- **Input:** `s = "9080701"`
- **Output:** `false`
- **Explanation:** There is no valid way to split s.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Splitting a String Into Descending Consecutive Values**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1234"`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.
4. **Verification:** There is no valid way to split s.

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
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(pos: int, prev: int) -> bool:
            if pos == n:
                return True
            val = 0
            for j in range(pos, n):
                val = val * 10 + int(s[j])
                if val > prev - 1:
                    break  # pieces only grow as they extend
                if val == prev - 1 and dfs(j + 1, val):
                    return True
            return False

        first = 0
        for i in range(n - 1):  # leave at least one character for a second piece
            first = first * 10 + int(s[i])
            if dfs(i + 1, first):
                return True
        return False
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
- [659. Split Array into Consecutive Subsequences](../../0501-1000/0659-split-array-into-consecutive-subsequences/)
- [1422. Maximum Score After Splitting a String](../../1001-1500/1422-maximum-score-after-splitting-a-string/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1593-split-a-string-into-the-max-number-of-unique-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/)
