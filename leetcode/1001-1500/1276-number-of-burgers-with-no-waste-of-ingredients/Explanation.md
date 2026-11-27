# LeetCode 1276: Number of Burgers with No Waste of Ingredients

**LeetCode Problem #1276 — Number of Burgers with No Waste of Ingredients**
Solve LeetCode Number of Burgers with No Waste of Ingredients using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Burgers with No Waste of Ingredients |
| LeetCode | #1276 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `tomatoSlices` and `cheeseSlices`. The ingredients of different burgers are as follows:

**Jumbo Burger:** `4` tomato slices and `1` cheese slice. 
 **Small Burger:** `2` Tomato slices and `1` cheese slice.

Return `[total_jumbo, total_small]` so that the number of remaining `tomatoSlices` equal to `0` and the number of remaining `cheeseSlices` equal to `0`. If it is not possible to make the remaining `tomatoSlices` and `cheeseSlices` equal to `0` return `[]`.

## Constraints
- `0 <= tomatoSlices, cheeseSlices <= 10^7`

## Examples
### Example 1
- **Input:** `tomatoSlices = 16, cheeseSlices = 7`
- **Output:** `[1,6]`

### Example 2
- **Input:** `tomatoSlices = 17, cheeseSlices = 4`
- **Output:** `[]`

### Example 3
- **Input:** `tomatoSlices = 4, cheeseSlices = 17`
- **Output:** `[]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Burgers with No Waste of Ingredients**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `tomatoSlices = 16, cheeseSlices = 7`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,6]`.

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
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        if (
            tomatoSlices % 2 != 0
            or tomatoSlices < 2 * cheeseSlices
            or tomatoSlices > 4 * cheeseSlices
        ):
            return []
            
        jumbo = tomatoSlices // 2 - cheeseSlices
        small = cheeseSlices - jumbo
        return [jumbo, small]
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
- [363. Max Sum of Rectangle No Larger Than K](../../0001-0500/0363-max-sum-of-rectangle-no-larger-than-k/)
- [1042. Flower Planting With No Adjacent](../../1001-1500/1042-flower-planting-with-no-adjacent/)
- [1317. Convert Integer to the Sum of Two No-Zero Integers](../../1001-1500/1317-convert-integer-to-the-sum-of-two-no-zero-integers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/)
