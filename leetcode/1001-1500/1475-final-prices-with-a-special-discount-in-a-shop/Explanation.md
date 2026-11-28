# LeetCode 1475: Final Prices With a Special Discount in a Shop

**LeetCode Problem #1475 — Final Prices With a Special Discount in a Shop**
Solve LeetCode Final Prices With a Special Discount in a Shop using TypeScript and Monotonic Stack. This solution finds the optimal result using Monotonic Stack Filtering in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Final Prices With a Special Discount in a Shop |
| LeetCode | #1475 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Monotonic Stack Filtering |
| Data Structure | Stack |
| Pattern | Monotonic Stack |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `prices` where `prices[i]` is the price of the `i^th` item in a shop.

There is a special discount for items in the shop. If you buy the `i^th` item, then you will receive a discount equivalent to `prices[j]` where `j` is the minimum index such that `j > i` and `prices[j] <= prices[i]`. Otherwise, you will not receive any discount at all.

Return an integer array `answer` where `answer[i]` is the final price you will pay for the `i^th` item of the shop, considering the special discount.

## Constraints
- `1 <= prices.length <= 500`
- `1 <= prices[i] <= 1000`

## Examples
### Example 1
- **Input:** `prices = [8,4,6,2,3]`
- **Output:** `[4,2,4,2,3]`
- **Explanation:** For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.

### Example 2
- **Input:** `prices = [1,2,3,4,5]`
- **Output:** `[1,2,3,4,5]`
- **Explanation:** In this case, for all items, you will not receive any discount at all.

### Example 3
- **Input:** `prices = [10,1,1,6]`
- **Output:** `[9,0,1,6]`

## Key Insight
Maintain a stack whose elements are strictly increasing or decreasing to answer 'next greater' or 'previous smaller' query problems in $O(n)$ total operations.

## Approach
The code uses a **Monotonic Stack** to efficiently find the next smaller or equal element for each index. It processes prices left to right, maintaining a stack of indices with unresolved discounts. When a price that qualifies as a discount is found, all applicable items on the stack get their discount applied.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Monotonic Stack Filtering**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `prices = [8,4,6,2,3]`.
2. **Processing Steps:** We apply **Monotonic Stack Filtering** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,2,4,2,3]`.
4. **Verification:** For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Monotonic Stack**

## Topics
- Stack
- Monotonic Stack
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function finalPrices(prices: number[]): number[] {
    const stack: number[] = [];

    for (let i = 0; i < prices.length; i++) {
        while (
            stack.length > 0 &&
            prices[stack[stack.length - 1]] >= prices[i]
        ) {
            const index = stack.pop()!;
            prices[index] -= prices[i];
        }

        stack.push(i);
    }

    return prices;
}
```

## Why This Works
By utilizing **Monotonic Stack**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Pushing elements instead of indices when index distance is required.
2. Using strict inequality (`<`) when non-strict (`<=`) is necessary.
3. Forgetting to flush remaining elements from stack at the end.

## Interview Notes
- **Tests:** Linear stack processing, nearest element relationship analysis.
- **Follow-up:** How do you handle circular array boundaries?

## Related Problems
- [2483. Minimum Penalty for a Shop](../../2001-2500/2483-minimum-penalty-for-a-shop/)
- [1896. Minimum Cost to Change the Final Value of Expression](../../1501-2000/1896-minimum-cost-to-change-the-final-value-of-expression/)
- [2011. Final Value of Variable After Performing Operations](../../2001-2500/2011-final-value-of-variable-after-performing-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)
