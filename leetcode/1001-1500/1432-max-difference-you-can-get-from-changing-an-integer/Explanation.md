# LeetCode 1432: Max Difference You Can Get From Changing an Integer

**LeetCode Problem #1432 — Max Difference You Can Get From Changing an Integer**
Solve LeetCode Max Difference You Can Get From Changing an Integer using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Difference You Can Get From Changing an Integer |
| LeetCode | #1432 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `num`. You will apply the following steps to `num` **two** separate times:

Pick a digit `x (0 <= x <= 9)`. 
 Pick another digit `y (0 <= y <= 9)`. Note `y` can be equal to `x`. 
 Replace all the occurrences of `x` in the decimal representation of `num` by `y`.

Let `a` and `b` be the two results from applying the operation to `num` *independently*.

Return *the max difference* between `a` and `b`.

Note that neither `a` nor `b` may have any leading zeros, and **must not** be 0.

## Constraints
- `1 <= num <= 10^8`

## Examples
### Example 1
- **Input:** `num = 555`
- **Output:** `888`
- **Explanation:** The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888

### Example 2
- **Input:** `num = 9`
- **Output:** `8`
- **Explanation:** The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Max Difference You Can Get From Changing an Integer**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 555`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `888`.
4. **Verification:** The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888

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
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # maximize
        a = s
        for c in s:
            if c != '9':
                a = s.replace(c, '9')
                break

        # minimize
        b = s
        if s[0] != '1':
            b = s.replace(s[0], '1')
        else:
            for c in s[1:]:
                if c != '0' and c != '1':
                    b = s.replace(c, '0')
                    break

        return int(a) - int(b)
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
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1423. Maximum Points You Can Obtain from Cards](../../1001-1500/1423-maximum-points-you-can-obtain-from-cards/)
- [1561. Maximum Number of Coins You Can Get](../../1501-2000/1561-maximum-number-of-coins-you-can-get/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/)
