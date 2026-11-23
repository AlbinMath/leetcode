# LeetCode 3116: Kth Smallest Amount With Single Denomination Combination

**LeetCode Problem #3116 — Kth Smallest Amount With Single Denomination Combination**
Solve LeetCode Kth Smallest Amount With Single Denomination Combination using Java and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kth Smallest Amount With Single Denomination Combination |
| LeetCode | #3116 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `coins` representing coins of different denominations and an integer `k`.

You have an infinite number of coins of each denomination. However, you are **not allowed** to combine coins of different denominations.

Return the `k^th` **smallest** amount that can be made using these coins.

## Constraints
- `1 <= coins.length <= 15`
- `1 <= coins[i] <= 25`
- `1 <= k <= 2 * 10^9`
- `coins` contains pairwise distinct integers.

## Examples
### Example 1
- **Input:** `coins = [3,6,9], k = 3`
- **Output:** `9`
- **Explanation:** The given coins can make the following amounts: 
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc. 
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc. 
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc. 
All of the coins combined produce: 3, 6,

### Example 2
- **Input:** `coins = [5,2], k = 7`
- **Output:** `12`
- **Explanation:** The given coins can make the following amounts: 
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc. 
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc. 
All of the coins combined produce: 2, 4, 5, 6, 8, 10,

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Kth Smallest Amount With Single Denomination Combination**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `coins = [3,6,9], k = 3`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** The given coins can make the following amounts: 
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc. 
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc. 
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc. 
All of the coins combined produce: 3, 6,

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public long findKthSmallest(int[] coins, int k) {
        long left = 1;
        long right = (long) coins[0] * k;

        for (int coin : coins) {
            right = Math.min(right, (long) coin * k);
        }

        while (left < right) {
            long mid = left + (right - left) / 2;

            if (count(mid, coins) >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private long count(long x, int[] coins) {
        return dfs(0, x, 1, coins, 0);
    }

    private long dfs(int index, long x, long lcm,
                     int[] coins, int chosen) {

        long result = 0;

        for (int i = index; i < coins.length; i++) {
            long newLcm = lcm(lcm, coins[i]);

            // LCM is already larger than x, so no multiple exists
            if (newLcm > x) {
                continue;
            }

            long multiples = x / newLcm;

            if ((chosen & 1) == 0) {
                result += multiples;
            } else {
                result -= multiples;
            }

            result += dfs(i + 1, x, newLcm, coins, chosen + 1);
        }

        return result;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    private long lcm(long a, long b) {
        long g = gcd(a, b);
        return a / g * b;
    }
}
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [230. Kth Smallest Element in a BST](../../0001-0500/0230-kth-smallest-element-in-a-bst/)
- [378. Kth Smallest Element in a Sorted Matrix](../../0001-0500/0378-kth-smallest-element-in-a-sorted-matrix/)
- [668. Kth Smallest Number in Multiplication Table](../../0501-1000/0668-kth-smallest-number-in-multiplication-table/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/)
