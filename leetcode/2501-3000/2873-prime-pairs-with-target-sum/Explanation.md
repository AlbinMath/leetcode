# LeetCode 2761: Prime Pairs With Target Sum

**LeetCode Problem #2761 — Prime Pairs With Target Sum**
Solve LeetCode Prime Pairs With Target Sum using JavaScript and Dynamic Programming. This solution finds the optimal result using Memoization & State Transition in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Prime Pairs With Target Sum |
| LeetCode | #2761 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Memoization & State Transition |
| Data Structure | DP Table / Array |
| Pattern | Dynamic Programming |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer `n`. We say that two integers `x` and `y` form a prime number pair if:

`1 <= x <= y <= n` 
 `x + y == n` 
 `x` and `y` are prime numbers

Return *the 2D sorted list of prime number pairs* `[x_i, y_i]`. The list should be sorted in **increasing** order of `x_i`. If there are no prime number pairs at all, return *an empty array*.

**Note:** A prime number is a natural number greater than `1` with only two factors, itself and `1`.

## Constraints
- `1 <= n <= 10^6`

## Examples
### Example 1
- **Input:** `n = 10`
- **Output:** `[[3,7],[5,5]]`
- **Explanation:** In this example, there are two prime pairs that satisfy the criteria. 
These pairs are [3,7] and [5,5], and we return them in the sorted order as described in the problem statement.

### Example 2
- **Input:** `n = 2`
- **Output:** `[]`
- **Explanation:** We can show that there is no prime number pair that gives a sum of 2, so we return an empty array.

## Key Insight
Break down the main problem into overlapping subproblems, storing optimal intermediate states in a DP table or memoization array to avoid re-computation.

## Approach
To solve **Prime Pairs With Target Sum**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10`.
2. **Processing Steps:** We apply **Memoization & State Transition** using our **DP Table / Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[3,7],[5,5]]`.
4. **Verification:** In this example, there are two prime pairs that satisfy the criteria. 
These pairs are [3,7] and [5,5], and we return them in the sorted order as described in the problem statement.

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
/**
 * @param {number} n
 * @return {number[][]}
 */
var findPrimePairs = function(n) {
    if (n < 4) return [];

    // 1. Sieve of Eratosthenes to find all primes up to n
    const isPrime = new Uint8Array(n + 1).fill(1);
    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    // 2. Collect all prime pairs [x, n - x] where x <= n - x
    const result = [];
    const limit = Math.floor(n / 2);

    for (let x = 2; x <= limit; x++) {
        const y = n - x;
        if (isPrime[x] && isPrime[y]) {
            result.push([x, y]);
        }
    }

    return result;
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
- [494. Target Sum](../../0001-0500/0494-target-sum/)
- [677. Map Sum Pairs](../../0501-1000/0677-map-sum-pairs/)
- [1074. Number of Submatrices That Sum to Target](../../1001-1500/1145-number-of-submatrices-that-sum-to-target/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/prime-pairs-with-target-sum/)
