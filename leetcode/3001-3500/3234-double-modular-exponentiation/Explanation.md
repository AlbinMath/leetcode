# LeetCode 2961: Double Modular Exponentiation

**LeetCode Problem #2961 — Double Modular Exponentiation**
Solve LeetCode Double Modular Exponentiation using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Double Modular Exponentiation |
| LeetCode | #2961 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** 2D array `variables` where `variables[i] = [a_i, b_i, c_i, m_i]`, and an integer `target`.

An index `i` is **good** if the following formula holds:

`0 <= i < variables.length` 
 `((a_i^b_i % 10)^c_i) % m_i == target`

Return *an array consisting of **good** indices in **any order***.

## Constraints
- `1 <= variables.length <= 100`
- `variables[i] == [a_i, b_i, c_i, m_i]`
- `1 <= a_i, b_i, c_i, m_i <= 10^3`
- ` 0 <= target <= 10^3 `

## Examples
### Example 1
- **Input:** `variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2`
- **Output:** `[0,2]`
- **Explanation:** For each index i in the variables array:
1) For the index 0, variables[0] = [2,3,3,10], (2^3 % 10)^3 % 10 = 2.
2) For the index 1, variables[1] = [3,3,3,1], (3^3 % 10)^3 % 1 = 0.
3) For the index 2, variables[2] = [6,1,1,4], (6^1 % 10)^1 % 4 = 2.
Therefore we return [0,2] as the answer.

### Example 2
- **Input:** `variables = [[39,3,1000,1000]], target = 17`
- **Output:** `[]`
- **Explanation:** For each index i in the variables array:
1) For the index 0, variables[0] = [39,3,1000,1000], (39^3 % 10)^1000 % 1000 = 1.
Therefore we return [] as the answer.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Double Modular Exponentiation**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[0,2]`.
4. **Verification:** For each index i in the variables array:
1) For the index 0, variables[0] = [2,3,3,10], (2^3 % 10)^3 % 10 = 2.
2) For the index 1, variables[1] = [3,3,3,1], (3^3 % 10)^3 % 1 = 0.
3) For the index 2, variables[2] = [6,1,1,4], (6^1 % 10)^1 % 4 = 2.
Therefore we return [0,2] as the answer.

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
var getGoodIndices = function(variables, target) {
    const modPow = (base, exp, mod) => {
        if (mod === 1) return 0;
        let result = 1;
        base %= mod;
        while (exp > 0) {
            if (exp & 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    };

    const goodIndices = [];
    for (let i = 0; i < variables.length; i++) {
        const [a, b, c, m] = variables[i];
        const first = modPow(a, b, 10);
        const second = modPow(first, c, m);
        if (second === target) {
            goodIndices.push(i);
        }
    }

    return goodIndices;
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
- [1346. Check If N and Its Double Exist](../../1001-1500/1468-check-if-n-and-its-double-exist/)
- [2119. A Number After a Double Reversal](../../2001-2500/2238-a-number-after-a-double-reversal/)
- [2816. Double a Number Represented as a Linked List](../../2501-3000/2871-double-a-number-represented-as-a-linked-list/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/double-modular-exponentiation/)
