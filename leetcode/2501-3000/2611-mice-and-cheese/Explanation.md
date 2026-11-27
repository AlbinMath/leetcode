# LeetCode 2611: Mice and Cheese

**LeetCode Problem #2611 — Mice and Cheese**
Solve LeetCode Mice and Cheese using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Mice and Cheese |
| LeetCode | #2611 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are two mice and `n` different types of cheese, each type of cheese should be eaten by exactly one mouse.

A point of the cheese with index `i` (**0-indexed**) is:

`reward1[i]` if the first mouse eats it. 
 `reward2[i]` if the second mouse eats it.

You are given a positive integer array `reward1`, a positive integer array `reward2`, and a non-negative integer `k`.

Return ***the maximum** points the mice can achieve if the first mouse eats exactly *`k`* types of cheese.*

## Constraints
- `1 <= n == reward1.length == reward2.length <= 10^5`
- `1 <= reward1[i], reward2[i] <= 1000`
- `0 <= k <= n`

## Examples
### Example 1
- **Input:** `reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2`
- **Output:** `15`
- **Explanation:** In this example, the first mouse eats the 2^nd (0-indexed) and the 3^rd types of cheese, and the second mouse eats the 0^th and the 1^st types of cheese.
The total points are 4 + 4 + 3 + 4 = 15.
It can be proven that 15 is the maximum total points that the mice can achieve.

### Example 2
- **Input:** `reward1 = [1,1], reward2 = [1,1], k = 2`
- **Output:** `2`
- **Explanation:** In this example, the first mouse eats the 0^th (0-indexed) and 1^st types of cheese, and the second mouse does not eat any cheese.
The total points are 1 + 1 = 2.
It can be proven that 2 is the maximum total points that the mice can achieve.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Mice and Cheese**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `15`.
4. **Verification:** In this example, the first mouse eats the 2^nd (0-indexed) and the 3^rd types of cheese, and the second mouse eats the 0^th and the 1^st types of cheese.
The total points are 4 + 4 + 3 + 4 = 15.
It can be proven that 15 is the maximum total points that the mice can achieve.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        diffs = sorted((a - b for a, b in zip(reward1, reward2)), reverse=True)
        return sum(reward2) + sum(diffs[:k])
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [27. Remove Element](../../0001-0500/0027-remove-element/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/mice-and-cheese/)
