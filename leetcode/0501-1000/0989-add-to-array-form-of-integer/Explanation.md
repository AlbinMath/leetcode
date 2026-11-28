# LeetCode 989: Add to Array-Form of Integer

**LeetCode Problem #989 — Add to Array-Form of Integer**
Solve LeetCode Add to Array-Form of Integer using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Add to Array-Form of Integer |
| LeetCode | #989 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
The **array-form** of an integer `num` is an array representing its digits in left to right order.

For example, for `num = 1321`, the array form is `[1,3,2,1]`.

Given `num`, the **array-form** of an integer, and an integer `k`, return *the **array-form** of the integer* `num + k`.

## Constraints
- `1 <= num.length <= 10^4`
- `0 <= num[i] <= 9`
- `num` does not contain any leading zeros except for the zero itself.
- `1 <= k <= 10^4`

## Examples
### Example 1
- **Input:** `num = [1,2,0,0], k = 34`
- **Output:** `[1,2,3,4]`
- **Explanation:** 1200 + 34 = 1234

### Example 2
- **Input:** `num = [2,7,4], k = 181`
- **Output:** `[4,5,5]`
- **Explanation:** 274 + 181 = 455

### Example 3
- **Input:** `num = [2,1,5], k = 806`
- **Output:** `[1,0,2,1]`
- **Explanation:** 215 + 806 = 1021

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Add to Array-Form of Integer**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = [1,2,0,0], k = 34`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2,3,4]`.
4. **Verification:** 1200 + 34 = 1234

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
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1

        while k > 0:
            if i >= 0:
                k += num[i]
                num[i] = k % 10
                k //= 10
                i -= 1
            else:
                num.insert(0, k % 10)
                k //= 10

        return num
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
- [1449. Form Largest Integer With Digits That Add up to Target](../../1001-1500/1449-form-largest-integer-with-digits-that-add-up-to-target/)
- [1394. Find Lucky Integer in an Array](../../1001-1500/1394-find-lucky-integer-in-an-array/)
- [1526. Minimum Number of Increments on Subarrays to Form a Target Array](../../1501-2000/1526-minimum-number-of-increments-on-subarrays-to-form-a-target-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/add-to-array-form-of-integer/)
