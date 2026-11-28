# LeetCode 2591: Distribute Money to Maximum Children

**LeetCode Problem #2591 — Distribute Money to Maximum Children**
Solve LeetCode Distribute Money to Maximum Children using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Distribute Money to Maximum Children |
| LeetCode | #2591 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `money` denoting the amount of money (in dollars) that you have and another integer `children` denoting the number of children that you must distribute the money to.

You have to distribute the money according to the following rules:

All money must be distributed. 
 Everyone must receive at least `1` dollar. 
 Nobody receives `4` dollars.

Return *the **maximum** number of children who may receive **exactly** *`8` *dollars if you distribute the money according to the aforementioned rules*. If there is no way to distribute the money, return `-1`.

## Constraints
- `1 <= money <= 200`
- `2 <= children <= 30`

## Examples
### Example 1
- **Input:** `money = 20, children = 3`
- **Output:** `1`
- **Explanation:** The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child. 
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.

### Example 2
- **Input:** `money = 16, children = 2`
- **Output:** `2`
- **Explanation:** Each child can be given 8 dollars.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Distribute Money to Maximum Children**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `money = 20, children = 3`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
- 8 dollars to the first child.
- 9 dollars to the second child. 
- 3 dollars to the third child.
It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.

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
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        k = min(money // 7, children)
        left = money - 7 * k
        if k == children and left != 0:
            return children - 1
        if k == children - 1 and left == 3:
            return children - 2
        return k
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
- [2928. Distribute Candies Among Children I](../../2501-3000/2928-distribute-candies-among-children-i/)
- [2929. Distribute Candies Among Children II](../../2501-3000/2929-distribute-candies-among-children-ii/)
- [2226. Maximum Candies Allocated to K Children](../../2001-2500/2226-maximum-candies-allocated-to-k-children/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/distribute-money-to-maximum-children/)
