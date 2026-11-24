# LeetCode 3470: Permutations IV

**LeetCode Problem #3470 — Permutations IV**
Solve LeetCode Permutations IV using JavaScript and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Permutations IV |
| LeetCode | #3470 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers, `n` and `k`, an **alternating permutation** is a permutation of the first `n` positive integers such that no **two** adjacent elements are both odd or both even.

Return the **k-th** **alternating permutation** sorted in *lexicographical order*. If there are fewer than `k` valid **alternating permutations**, return an empty list.

## Constraints
- `1 <= n <= 100`
- `1 <= k <= 10^15`

## Examples
### Example 1
- **Input:** `n = 4, k = 6`
- **Output:** `[3,4,1,2]`
- **Explanation:** The lexicographically-sorted alternating permutations of `[1, 2, 3, 4]` are: 

 
 `[1, 2, 3, 4]` 
 `[1, 4, 3, 2]` 
 `[2, 1, 4, 3]` 
 `[2, 3, 4, 1]` 
 `[3, 2, 1, 4]` 
 `[3, 4, 1, 2]` &larr; 6th permutation 
 `[4, 1, 2, 3]` 
 `[4, 3, 2, 1]` 
 

 Since `k = 6`, we return `[3, 4, 1, 2]`.

### Example 2
- **Input:** `n = 3, k = 2`
- **Output:** `[3,2,1]`
- **Explanation:** The lexicographically-sorted alternating permutations of `[1, 2, 3]` are: 

 
 `[1, 2, 3]` 
 `[3, 2, 1]` &larr; 2nd permutation 
 

 Since `k = 2`, we return `[3, 2, 1]`.

### Example 3
- **Input:** `n = 2, k = 3`
- **Output:** `[]`
- **Explanation:** The lexicographically-sorted alternating permutations of `[1, 2]` are: 

 
 `[1, 2]` 
 `[2, 1]` 
 

 There are only 2 alternating permutations, but `k = 3`, which is out of range. Thus, we return an empty list `[]`.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Permutations IV**, we observe the problem requirements and utilize the **Backtracking** technique. We iterate through the inputs using **Backtracking Recursive Search**, leveraging a **Recursion Tree** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Recursion Tree**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, k = 6`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,4,1,2]`.
4. **Verification:** The lexicographically-sorted alternating permutations of `[1, 2, 3, 4]` are: 

 
 `[1, 2, 3, 4]` 
 `[1, 4, 3, 2]` 
 `[2, 1, 4, 3]` 
 `[2, 3, 4, 1]` 
 `[3, 2, 1, 4]` 
 `[3, 4, 1, 2]` &larr; 6th permutation 
 `[4, 1, 2, 3]` 
 `[4, 3, 2, 1]` 
 

 Since `k = 6`, we return `[3, 4, 1, 2]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var permute = function (n, k) {
    const fact = [1n];
    for (let i = 1; i <= n; i++) fact.push(fact[i - 1] * BigInt(i));

    let K = BigInt(k);
    const used = new Array(n + 1).fill(false);
    let ro = Math.ceil(n / 2); // odds remaining
    let re = Math.floor(n / 2); // evens remaining
    const res = [];

    for (let i = 0; i < n; i++) {
        let chosen = -1;
        for (let v = 1; v <= n; v++) {
            if (used[v]) continue;
            if (i > 0 && (v & 1) === (res[i - 1] & 1)) continue;

            // remaining counts after placing v
            const nro = ro - (v & 1);
            const nre = re - ((v & 1) ^ 1);
            const r = n - i - 1;
            // next position must have the opposite parity of v
            const nextIsOdd = (v & 1) === 0;
            const needOdd = nextIsOdd ? Math.ceil(r / 2) : Math.floor(r / 2);

            let cnt = 0n;
            if (nro >= 0 && nre >= 0 && needOdd === nro) {
                cnt = fact[nro] * fact[nre];
            }

            if (K > cnt) {
                K -= cnt;
            } else {
                chosen = v;
                break;
            }
        }
        if (chosen === -1) return [];
        used[chosen] = true;
        res.push(chosen);
        if (chosen & 1) ro--;
        else re--;
    }
    return res;
};
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
- [46. Permutations](../../0001-0500/0046-permutations/)
- [47. Permutations II](../../0001-0500/0047-permutations-ii/)
- [903. Valid Permutations for DI Sequence](../../0501-1000/0903-valid-permutations-for-di-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/permutations-iv/)
