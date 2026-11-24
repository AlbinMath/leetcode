# LeetCode 1563: Stone Game V

**LeetCode Problem #1563 — Stone Game V**
Solve LeetCode Stone Game V using Java and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game V |
| LeetCode | #1563 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There are several stones **arranged in a row**, and each stone has an associated value which is an integer given in the array `stoneValue`.

In each round of the game, Alice divides the row into **two non-empty rows** (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only **one stone remaining**. Alice's score is initially **zero**.

Return the maximum score that Alice can obtain .

## Constraints
- `1 <= stoneValue.length <= 500`
- `1 <= stoneValue[i] <= 10^6`

## Examples
### Example 1
- **Input:** `stoneValue = [6,2,3,4,5,5]`
- **Output:** `18`
- **Explanation:** In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

### Example 2
- **Input:** `stoneValue = [7,7,7,7,7,7,7]`
- **Output:** `28`

### Example 3
- **Input:** `stoneValue = [4]`
- **Output:** `0`

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Interval DP** where `dp[left][right]` = maximum score from the subarray `[left, right]`.

1. **Prefix Sums:** Compute prefix sums for fast range sum queries.
2. **DP Transition:** For every split point `mid` in `[left, right-1]`:
   - Compute `leftSum` and `rightSum`.
   - If `leftSum < rightSum`: discard right, score `leftSum`, recurse on `[left, mid]`.
   - If `leftSum > rightSum`: discard left, score `rightSum`, recurse on `[mid+1, right]`.
   - If equal: try both options and take the maximum.
3. Return `dp[0][n-1]`.

Time complexity is $O(N^3)$ and space complexity is $O(N^2)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `stoneValue = [6,2,3,4,5,5]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `18`.
4. **Verification:** In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;

        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + stoneValue[i];
        }

        int[][] dp = new int[n][n];

        for (int len = 2; len <= n; len++) {
            for (int left = 0; left + len <= n; left++) {
                int right = left + len - 1;

                for (int mid = left; mid < right; mid++) {
                    int leftSum = prefix[mid + 1] - prefix[left];
                    int rightSum = prefix[right + 1] - prefix[mid + 1];

                    if (leftSum < rightSum) {
                        dp[left][right] = Math.max(
                            dp[left][right],
                            leftSum + dp[left][mid]
                        );
                    } 
                    else if (leftSum > rightSum) {
                        dp[left][right] = Math.max(
                            dp[left][right],
                            rightSum + dp[mid + 1][right]
                        );
                    } 
                    else {
                        dp[left][right] = Math.max(
                            dp[left][right],
                            leftSum + Math.max(
                                dp[left][mid],
                                dp[mid + 1][right]
                            )
                        );
                    }
                }
            }
        }

        return dp[0][n - 1];
    }
}
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1340. Jump Game V](../../1001-1500/1340-jump-game-v/)
- [877. Stone Game](../../0501-1000/0877-stone-game/)
- [1140. Stone Game II](../../1001-1500/1140-stone-game-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-v/)
