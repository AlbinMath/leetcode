# LeetCode 1550: Three Consecutive Odds

**LeetCode Problem #1550 — Three Consecutive Odds**
Solve LeetCode Three Consecutive Odds using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Three Consecutive Odds |
| LeetCode | #1550 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array. Otherwise, return `false`.

## Constraints
- `1 <= arr.length <= 1000`
- `1 <= arr[i] <= 1000`

## Examples
### Example 1
- **Input:** `arr = [2,6,4,1]`
- **Output:** `false`

### Example 2
- **Input:** `arr = [1,2,34,3,4,5,7,23,12]`
- **Output:** `true`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Three Consecutive Odds**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,6,4,1]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `false`.

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
class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        count = 0

        for num in arr:
            if num % 2 == 1:
                count += 1

                if count == 3:
                    return True
            else:
                count = 0

        return False
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
- [2177. Find Three Consecutive Integers That Sum to a Given Number](../../2001-2500/2278-find-three-consecutive-integers-that-sum-to-a-given-number/)
- [128. Longest Consecutive Sequence](../../0001-0500/0128-longest-consecutive-sequence/)
- [180. Consecutive Numbers](../../0001-0500/0180-consecutive-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/three-consecutive-odds/)
