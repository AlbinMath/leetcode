# LeetCode 1503: Last Moment Before All Ants Fall Out of a Plank

**LeetCode Problem #1503 — Last Moment Before All Ants Fall Out of a Plank**
Solve LeetCode Last Moment Before All Ants Fall Out of a Plank using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Last Moment Before All Ants Fall Out of a Plank |
| LeetCode | #1503 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We have a wooden plank of the length `n` **units**. Some ants are walking on the plank, each ant moves with a speed of **1 unit per second**. Some of the ants move to the **left**, the other move to the **right**.

When two ants moving in two **different** directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time.

When an ant reaches **one end** of the plank at a time `t`, it falls out of the plank immediately.

Given an integer `n` and two integer arrays `left` and `right`, the positions of the ants moving to the left and the right, return *the moment when the last ant(s) fall out of the plank*.

## Constraints
- `1 <= n <= 10^4`
- `0 <= left.length <= n + 1`
- `0 <= left[i] <= n`
- `0 <= right.length <= n + 1`
- `0 <= right[i] <= n`
- `1 <= left.length + right.length <= n + 1`
- All values of `left` and `right` are unique, and each value can appear **only in one** of the two arrays.

## Examples
### Example 1
- **Input:** `n = 4, left = [4,3], right = [0,1]`
- **Output:** `4`
- **Explanation:** In the image above:
-The ant at index 0 is named A and going to the right.
-The ant at index 1 is named B and going to the right.
-The ant at index 3 is named C and going to the left.
-The ant at index 4 is named D and going to the left.
The last moment when an ant was on the plank is t = 4 seconds. After that, it falls immediately out of the plank. (i.e., We can say that at t = 4.0000000001, there are no ants on the plank).

### Example 2
- **Input:** `n = 7, left = [], right = [0,1,2,3,4,5,6,7]`
- **Output:** `7`
- **Explanation:** All ants are going to the right, the ant at index 0 needs 7 seconds to fall.

### Example 3
- **Input:** `n = 7, left = [0,1,2,3,4,5,6,7], right = []`
- **Output:** `7`
- **Explanation:** All ants are going to the left, the ant at index 7 needs 7 seconds to fall.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Last Moment Before All Ants Fall Out of a Plank**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, left = [4,3], right = [0,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** In the image above:
-The ant at index 0 is named A and going to the right.
-The ant at index 1 is named B and going to the right.
-The ant at index 3 is named C and going to the left.
-The ant at index 4 is named D and going to the left.
The last moment when an ant was on the plank is t = 4 seconds. After that, it falls immediately out of the plank. (i.e., We can say that at t = 4.0000000001, there are no ants on the plank).

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
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        a = max(left) if left else 0
        b = n - min(right) if right else 0
        return max(a, b)
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
- [2124. Check if All A's Appears Before All B's](../../2001-2500/2243-check-if-all-as-appears-before-all-bs/)
- [30. Substring with Concatenation of All Words](../../0001-0500/0030-substring-with-concatenation-of-all-words/)
- [432. All O`one Data Structure](../../0001-0500/0432-all-oone-data-structure/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/)
