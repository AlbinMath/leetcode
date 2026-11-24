# LeetCode 1124: Longest Well-Performing Interval

**LeetCode Problem #1124 — Longest Well-Performing Interval**
Solve LeetCode Longest Well-Performing Interval using Python and Heap. This solution finds the optimal result using Min/Max Heap Priority Selection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Well-Performing Interval |
| LeetCode | #1124 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Min/Max Heap Priority Selection |
| Data Structure | Heap / Priority Queue |
| Pattern | Heap |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
We are given `hours`, a list of the number of hours worked per day for a given employee.

A day is considered to be a *tiring day* if and only if the number of hours worked is (strictly) greater than `8`.

A *well-performing interval* is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

## Constraints
- `1 <= hours.length <= 10^4`
- `0 <= hours[i] <= 16`

## Examples
### Example 1
- **Input:** `hours = [9,9,6,0,6,6,9]`
- **Output:** `3`
- **Explanation:** The longest well-performing interval is [9,9,6].

### Example 2
- **Input:** `hours = [6,6,6]`
- **Output:** `0`

## Key Insight
Leverage **Heap** with **Heap / Priority Queue** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Well-Performing Interval**, we observe the problem requirements and utilize the **Heap** technique. By maintaining a **Heap / Priority Queue**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Heap / Priority Queue** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `hours = [9,9,6,0,6,6,9]`.
2. **Processing Steps:** We apply **Min/Max Heap Priority Selection** using our **Heap / Priority Queue**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The longest well-performing interval is [9,9,6].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Heap / Priority Queue.

## Pattern
**Heap**

## Topics
- Heap
- Priority Queue
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        first = {}
        s = 0
        ans = 0
        for i, h in enumerate(hours):
            s += 1 if h > 8 else -1
            if s > 0:
                ans = i + 1
            else:
                if s not in first:
                    first[s] = i
                if s - 1 in first:
                    ans = max(ans, i - first[s - 1])
        return ans
```

## Why This Works
By utilizing **Heap**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-well-performing-interval/)
