# LeetCode 3200: Maximum Height of a Triangle

**LeetCode Problem #3200 — Maximum Height of a Triangle**
Solve LeetCode Maximum Height of a Triangle using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Height of a Triangle |
| LeetCode | #3200 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `red` and `blue` representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1^st row will have 1 ball, the 2^nd row will have 2 balls, the 3^rd row will have 3 balls, and so on.

All the balls in a particular row should be the **same** color, and adjacent rows should have **different** colors.

Return the **maximum*** height of the triangle* that can be achieved.

## Constraints
- `1 <= red, blue <= 100`

## Examples
### Example 1
- **Input:** `red = 2, blue = 4`
- **Output:** `3`
- **Explanation:** The only possible arrangement is shown above.

### Example 2
- **Input:** `red = 2, blue = 1`
- **Output:** `2`
- **Explanation:** The only possible arrangement is shown above.

### Example 3
- **Input:** `red = 1, blue = 1`
- **Output:** `1`

### Example 4
- **Input:** `red = 10, blue = 1`
- **Output:** `2`
- **Explanation:** The only possible arrangement is shown above.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Height of a Triangle**, we observe the problem requirements and utilize the **Tree & Graph** technique. We perform a recursive Depth-First Search (DFS) traversal. The algorithm handles base cases at leaf nodes and aggregates results from subtrees back up to the root.

## Algorithm
1. Define base cases for null/leaf nodes.
2. Recursively traverse child nodes.
3. Combine child results to determine current node output.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `red = 2, blue = 4`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The only possible arrangement is shown above.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(first: int, second: int) -> int:
            have = [first, second]
            h = 0
            while True:
                need = h + 1
                idx = h % 2
                if have[idx] < need:
                    return h
                have[idx] -= need
                h += 1

        return max(height(red, blue), height(blue, red))
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1691. Maximum Height by Stacking Cuboids ](../../1501-2000/1691-maximum-height-by-stacking-cuboids/)
- [1840. Maximum Building Height](../../1501-2000/1840-maximum-building-height/)
- [3588. Find Maximum Area of a Triangle](../../3501-4000/3588-find-maximum-area-of-a-triangle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-height-of-a-triangle/)
