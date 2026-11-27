# LeetCode 3098: Find the Sum of Subsequence Powers

**LeetCode Problem #3098 — Find the Sum of Subsequence Powers**
Solve LeetCode Find the Sum of Subsequence Powers using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Sum of Subsequence Powers |
| LeetCode | #3098 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n`, and a **positive** integer `k`.

The **power** of a subsequence is defined as the **minimum** absolute difference between **any** two elements in the subsequence.

Return *the **sum** of **powers** of **all** subsequences of *`nums`* which have length* ***equal to*** `k`.

Since the answer may be large, return it **modulo** `10^9 + 7`.

## Constraints
- `2 <= n == nums.length <= 50`
- `-10^8 <= nums[i] <= 10^8 `
- `2 <= k <= n`

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4], k = 3`
- **Output:** `4`
- **Explanation:** There are 4 subsequences in `nums` which have length 3: `[1,2,3]`, `[1,3,4]`, `[1,2,4]`, and `[2,3,4]`. The sum of powers is `|2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4`.

### Example 2
- **Input:** `nums = [2,2], k = 2`
- **Output:** `0`
- **Explanation:** The only subsequence in `nums` which has length 2 is `[2,2]`. The sum of powers is `|2 - 2| = 0`.

### Example 3
- **Input:** `nums = [4,3,-1], k = 2`
- **Output:** `10`
- **Explanation:** There are 3 subsequences in `nums` which have length 2: `[4,3]`, `[4,-1]`, and `[3,-1]`. The sum of powers is `|4 - 3| + |4 - (-1)| + |3 - (-1)| = 10`.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Find the Sum of Subsequence Powers**, we observe the problem requirements and utilize the **Dynamic Programming** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4], k = 3`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** There are 4 subsequences in `nums` which have length 3: `[1,2,3]`, `[1,3,4]`, `[1,2,4]`, and `[2,3,4]`. The sum of powers is `|2 - 3| + |3 - 4| + |2 - 1| + |3 - 4| = 4`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for DP Table / Array.

## Pattern
**Dynamic Programming**

## Topics
- Dynamic Programming
- Memoization
- State Transition

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var sumOfPowers = function(nums, k) {
    const MOD = 1000000007;
    const n = nums.length;

    nums.sort((a, b) => a - b);

    const differences = new Set();

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const diff = nums[j] - nums[i];

            if (diff > 0) {
                differences.add(diff);
            }
        }
    }

    const countAtLeast = function(d) {
        let prev = new Array(n).fill(1);

        for (let len = 2; len <= k; len++) {
            const prefix = new Array(n + 1).fill(0);

            for (let i = 0; i < n; i++) {
                prefix[i + 1] = (prefix[i] + prev[i]) % MOD;
            }

            const curr = new Array(n).fill(0);

            for (let i = 0; i < n; i++) {
                const target = nums[i] - d;

                let left = 0;
                let right = i;

                while (left < right) {
                    const mid = Math.floor((left + right) / 2);

                    if (nums[mid] <= target) {
                        left = mid + 1;
                    } else {
                        right = mid;
                    }
                }

                curr[i] = prefix[left];
            }

            prev = curr;
        }

        let total = 0;

        for (let ways of prev) {
            total = (total + ways) % MOD;
        }

        return total;
    };

    let answer = 0n;
    const bigMOD = BigInt(MOD);

    for (const d of differences) {
        const atLeastD = countAtLeast(d);
        const atLeastNext = countAtLeast(d + 1);

        const exactD = (atLeastD - atLeastNext + MOD) % MOD;

        answer = (
            answer + BigInt(d) * BigInt(exactD)
        ) % bigMOD;
    }

    return Number(answer);
};
```

## Why This Works
By utilizing **Dynamic Programming**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Incorrect base case initialization.
2. Flawed state transition equation.
3. Storing unnecessary state leading to Memory Limit Exceeded (MLE).

## Interview Notes
- **Tests:** Subproblem decomposition, state transition logic, and space optimization.
- **Follow-up:** Can space complexity be reduced from $O(n^2)$ to $O(n)$ or $O(1)$?

## Related Problems
- [2099. Find Subsequence of Length K With the Largest Sum](../../2001-2500/2099-find-subsequence-of-length-k-with-the-largest-sum/)
- [891. Sum of Subsequence Widths](../../0501-1000/0891-sum-of-subsequence-widths/)
- [1425. Constrained Subsequence Sum](../../1001-1500/1425-constrained-subsequence-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-sum-of-subsequence-powers/)
