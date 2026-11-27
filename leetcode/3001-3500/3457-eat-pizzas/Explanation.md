# LeetCode 3457: Eat Pizzas!

**LeetCode Problem #3457 — Eat Pizzas!**
Solve LeetCode Eat Pizzas! using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Eat Pizzas! |
| LeetCode | #3457 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `pizzas` of size `n`, where `pizzas[i]` represents the weight of the `i^th` pizza. Every day, you eat **exactly** 4 pizzas. Due to your incredible metabolism, when you eat pizzas of weights `W`, `X`, `Y`, and `Z`, where `W <= X <= Y <= Z`, you gain the weight of only 1 pizza!

On ** odd-numbered ** days **(1-indexed)**, you gain a weight of `Z`. 
 On **even-numbered** days, you gain a weight of `Y`.

Find the **maximum** total weight you can gain by eating **all** pizzas optimally.

**Note**: It is guaranteed that `n` is a multiple of 4, and each pizza can be eaten only once.

## Constraints
- `4 <= n == pizzas.length <= 2 * 10^ 5 `
- `1 <= pizzas[i] <= 10^5`
- `n` is a multiple of 4.

## Examples
### Example 1
- **Input:** `pizzas = [1,2,3,4,5,6,7,8]`
- **Output:** `14`
- **Explanation:** On day 1, you eat pizzas at indices `[1, 2, 4, 7] = [2, 3, 5, 8]`. You gain a weight of 8. 
 On day 2, you eat pizzas at indices `[0, 3, 5, 6] = [1, 4, 6, 7]`. You gain a weight of 6. 
 

 The total weight gained after eating all the pizzas is `8 + 6 = 14`.

### Example 2
- **Input:** `pizzas = [2,1,1,1,1,1,1,1]`
- **Output:** `3`
- **Explanation:** On day 1, you eat pizzas at indices `[4, 5, 6, 0] = [1, 1, 1, 2]`. You gain a weight of 2. 
 On day 2, you eat pizzas at indices `[1, 2, 3, 7] = [1, 1, 1, 1]`. You gain a weight of 1. 
 

 The total weight gained after eating all the pizzas is `2 + 1 = 3.`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Eat Pizzas!**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pizzas = [1,2,3,4,5,6,7,8]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** On day 1, you eat pizzas at indices `[1, 2, 4, 7] = [2, 3, 5, 8]`. You gain a weight of 8. 
 On day 2, you eat pizzas at indices `[0, 3, 5, 6] = [1, 4, 6, 7]`. You gain a weight of 6. 
 

 The total weight gained after eating all the pizzas is `8 + 6 = 14`.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maxWeight = function(pizzas) {
    pizzas.sort((a, b) => a - b);

    const days = pizzas.length / 4;
    const oddDays = Math.ceil(days / 2);
    const evenDays = Math.floor(days / 2);

    let total = 0;
    let right = pizzas.length - 1;

    for (let i = 0; i < oddDays; i++) {
        total += pizzas[right];
        right--;
    }

    for (let i = 0; i < evenDays; i++) {
        total += pizzas[right - 1];
        right -= 2;
    }

    return total;
};
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
- [1553. Minimum Number of Days to Eat N Oranges](../../1501-2000/1553-minimum-number-of-days-to-eat-n-oranges/)
- [1700. Number of Students Unable to Eat Lunch](../../1501-2000/1700-number-of-students-unable-to-eat-lunch/)
- [1744. Can You Eat Your Favorite Candy on Your Favorite Day?](../../1501-2000/1744-can-you-eat-your-favorite-candy-on-your-favorite-day/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/eat-pizzas/)
