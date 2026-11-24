# LeetCode 1872: Stone Game VIII

**LeetCode Problem #1872 — Stone Game VIII**
Solve LeetCode Stone Game VIII using Java and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stone Game VIII |
| LeetCode | #1872 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Alice and Bob take turns playing a game, with **Alice starting first**.

There are `n` stones arranged in a row. On each player's turn, while the number of stones is **more than one**, they will do the following:

Choose an integer `x > 1`, and **remove** the leftmost `x` stones from the row. 
 Add the **sum** of the **removed** stones' values to the player's score. 
 Place a **new stone**, whose value is equal to that sum, on the left side of the row.

The game stops when **only** **one** stone is left in the row.

The **score difference** between Alice and Bob is `(Alice's score - Bob's score)`. Alice's goal is to **maximize** the score difference, and Bob's goal is the **minimize** the score difference.

Given an integer array `stones` of length `n` where `stones[i]` represents the value of the `i^th` stone **from the left**, return *the **score difference** between Alice and Bob if they both play **optimally**.*

## Constraints
- `n == stones.length`
- `2 <= n <= 10^5`
- `-10^4 <= stones[i] <= 10^4`

## Examples
### Example 1
- **Input:** `stones = [-1,2,-3,4,-5]`
- **Output:** `5`
- **Explanation:** - Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
 value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
 the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.

### Example 2
- **Input:** `stones = [7,-6,5,10,5,-2,-6]`
- **Output:** `13`
- **Explanation:** - Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
 stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.

### Example 3
- **Input:** `stones = [-10,-12]`
- **Output:** `-22`
- **Explanation:** - Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
 score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **DP with prefix sums**. After computing prefix sums, the problem reduces to choosing optimal split points. Working backwards, `dp[i]` = max difference the current player can achieve starting from index `i`. The recurrence is `dp[i] = max(dp[i+1], prefix[i] - dp[i+1])`.

Time complexity is $O(N)$ and space complexity is $O(1)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `stones = [-1,2,-3,4,-5]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** - Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
 value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
 the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.

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
    public int stoneGameVIII(int[] stones) {
        int n = stones.length;

        long[] prefix = new long[n];
        prefix[0] = stones[0];

        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + stones[i];
        }

        long best = prefix[n - 1];

        for (int i = n - 2; i >= 1; i--) {
            best = Math.max(prefix[i] - best, best);
        }

        return (int) best;
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
- [877. Stone Game](../../0501-1000/0877-stone-game/)
- [1140. Stone Game II](../../1001-1500/1140-stone-game-ii/)
- [1406. Stone Game III](../../1001-1500/1406-stone-game-iii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stone-game-viii/)
