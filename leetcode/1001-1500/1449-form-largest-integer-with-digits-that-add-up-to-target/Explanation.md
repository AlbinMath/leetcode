# LeetCode 1449: Form Largest Integer With Digits That Add up to Target

**LeetCode Problem #1449 — Form Largest Integer With Digits That Add up to Target**
Solve LeetCode Form Largest Integer With Digits That Add up to Target using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Form Largest Integer With Digits That Add up to Target |
| LeetCode | #1449 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `cost` and an integer `target`, return *the **maximum** integer you can paint under the following rules*:

The cost of painting a digit `(i + 1)` is given by `cost[i]` (**0-indexed**). 
 The total cost used must be equal to `target`. 
 The integer does not have `0` digits.

Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return `"0"`.

## Constraints
- `cost.length == 9`
- `1 <= cost[i], target <= 5000`

## Examples
### Example 1
- **Input:** `cost = [4,3,2,5,6,7,2,5,5], target = 9`
- **Output:** `"7772"`
- **Explanation:** The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.

### Example 2
- **Input:** `cost = [7,6,5,5,5,6,8,7,8], target = 12`
- **Output:** `"85"`
- **Explanation:** The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.

### Example 3
- **Input:** `cost = [2,4,6,2,4,6,4,4,4], target = 5`
- **Output:** `"0"`
- **Explanation:** It is impossible to paint any integer with total cost equal to target.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Form Largest Integer With Digits That Add up to Target**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `cost = [4,3,2,5,6,7,2,5,5], target = 9`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"7772"`.
4. **Verification:** The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        NEG_INF = float('-inf')
        dp = [NEG_INF] * (target + 1)
        dp[0] = 0
        
        for t in range(1, target + 1):
            for c in cost:
                if t >= c and dp[t - c] + 1 > dp[t]:
                    dp[t] = dp[t - c] + 1
                    
        if dp[target] < 0:
            return "0"
            
        res = []
        rem = target
        for d in range(9, 0, -1):
            c = cost[d - 1]
            while rem >= c and dp[rem] == dp[rem - c] + 1:
                res.append(str(d))
                rem -= c
                
        return "".join(res)
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [1725. Number Of Rectangles That Can Form The Largest Square](../../1501-2000/1725-number-of-rectangles-that-can-form-the-largest-square/)
- [2441. Largest Positive Integer That Exists With Its Negative](../../2001-2500/2441-largest-positive-integer-that-exists-with-its-negative/)
- [989. Add to Array-Form of Integer](../../0501-1000/0989-add-to-array-form-of-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/)
