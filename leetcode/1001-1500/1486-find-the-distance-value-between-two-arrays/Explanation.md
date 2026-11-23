# LeetCode 1385: Find the Distance Value Between Two Arrays

**LeetCode Problem #1385 — Find the Distance Value Between Two Arrays**
Solve LeetCode Find the Distance Value Between Two Arrays using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Distance Value Between Two Arrays |
| LeetCode | #1385 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integer arrays `arr1` and `arr2`, and the integer `d`, *return the distance value between the two arrays*.

The distance value is defined as the number of elements `arr1[i]` such that there is not any element `arr2[j]` where `|arr1[i]-arr2[j]| <= d`.

## Constraints
- `1 <= arr1.length, arr2.length <= 500`
- `-1000 <= arr1[i], arr2[j] <= 1000`
- `0 <= d <= 100`

## Examples
### Example 1
- **Input:** `arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2`
- **Output:** `2`
- **Explanation:** For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:

### Example 2
- **Input:** `arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3`
- **Output:** `2`

### Example 3
- **Input:** `arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6`
- **Output:** `1`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find the Distance Value Between Two Arrays**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:

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
    def findTheDistanceValue(
        self, arr1: list[int], arr2: list[int], d: int
    ) -> int:
        count = 0

        for x in arr1:
            valid = True

            for y in arr2:
                if abs(x - y) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count
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
- [1477. Find Two Non-overlapping Sub-arrays Each With Target Sum](../../1501-2000/1573-find-two-non-overlapping-sub-arrays-each-with-target-sum/)
- [2215. Find the Difference of Two Arrays](../../1001-1500/1392-find-the-difference-of-two-arrays/)
- [2657. Find the Prefix Common Array of Two Arrays](../../2501-3000/2766-find-the-prefix-common-array-of-two-arrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/)
