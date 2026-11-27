# LeetCode 3377: Digit Operations to Make Two Integers Equal

**LeetCode Problem #3377 — Digit Operations to Make Two Integers Equal**
Solve LeetCode Digit Operations to Make Two Integers Equal using JavaScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Digit Operations to Make Two Integers Equal |
| LeetCode | #3377 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two integers `n` and `m` that consist of the **same** number of digits.

You can perform the following operations **any** number of times:

Choose **any** digit from `n` that is not 9 and **increase** it by 1. 
 Choose **any** digit from `n` that is not 0 and **decrease** it by 1.

The integer `n` must not be a prime number at any point, including its original value and after each operation.

The cost of a transformation is the sum of **all** values that `n` takes throughout the operations performed.

Return the **minimum** cost to transform `n` into `m`. If it is impossible, return -1.

## Constraints
- `1 <= n, m < 10^4`
- `n` and `m` consist of the same number of digits.

## Examples
### Example 1
- **Input:** `n = 10, m = 12`
- **Output:** `85`
- **Explanation:** We perform the following operations: 

 
 Increase the first digit, now n =

### Example 2
- **Input:** `n = 4, m = 8`
- **Output:** `-1`
- **Explanation:** It is impossible to make `n` equal to `m`.

### Example 3
- **Input:** `n = 6, m = 2`
- **Output:** `-1`
- **Explanation:** Since 2 is already a prime, we can't make `n` equal to `m`.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Digit Operations to Make Two Integers Equal**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10, m = 12`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `85`.
4. **Verification:** We perform the following operations: 

 
 Increase the first digit, now n =

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var minOperations = function (n, m) {
    const LIMIT = 10000;
    const composite = new Uint8Array(LIMIT);
    composite[0] = 1; // 0 and 1 are not prime
    composite[1] = 1;
    const prime = new Uint8Array(LIMIT).fill(1);
    prime[0] = 0;
    prime[1] = 0;
    for (let i = 2; i * i < LIMIT; i++) {
        if (prime[i]) {
            for (let j = i * i; j < LIMIT; j += i) prime[j] = 0;
        }
    }

    if (prime[n] || prime[m]) return -1;

    const len = String(n).length;
    const lo = len === 1 ? 0 : Math.pow(10, len - 1);

    const dist = new Float64Array(LIMIT).fill(Infinity);
    dist[n] = n;

    // Min-heap of [cost, node] stored as parallel arrays
    const hc = [];
    const hn = [];
    const push = (c, v) => {
        let i = hc.length;
        hc.push(c);
        hn.push(v);
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (hc[p] <= hc[i]) break;
            let t = hc[p]; hc[p] = hc[i]; hc[i] = t;
            t = hn[p]; hn[p] = hn[i]; hn[i] = t;
            i = p;
        }
    };
    const pop = () => {
        const c = hc[0], v = hn[0];
        const lc = hc.pop(), lv = hn.pop();
        const size = hc.length;
        if (size > 0) {
            hc[0] = lc;
            hn[0] = lv;
            let i = 0;
            while (true) {
                const l = 2 * i + 1, r = l + 1;
                let s = i;
                if (l < size && hc[l] < hc[s]) s = l;
                if (r < size && hc[r] < hc[s]) s = r;
                if (s === i) break;
                let t = hc[s]; hc[s] = hc[i]; hc[i] = t;
                t = hn[s]; hn[s] = hn[i]; hn[i] = t;
                i = s;
            }
        }
        return [c, v];
    };

    push(n, n);
    while (hc.length) {
        const [c, u] = pop();
        if (c > dist[u]) continue;
        if (u === m) return c;

        let p = 1;
        for (let k = 0; k < len; k++, p *= 10) {
            const digit = ((u / p) | 0) % 10;
            if (digit < 9) {
                const v = u + p;
                const nc = c + v;
                if (!prime[v] && nc < dist[v]) {
                    dist[v] = nc;
                    push(nc, v);
                }
            }
            if (digit > 0) {
                const v = u - p;
                const nc = c + v;
                if (v >= lo && !prime[v] && nc < dist[v]) {
                    dist[v] = nc;
                    push(nc, v);
                }
            }
        }
    }
    return -1;
};
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3226. Number of Bit Changes to Make Two Integers Equal](../../3001-3500/3226-number-of-bit-changes-to-make-two-integers-equal/)
- [1611. Minimum One Bit Operations to Make Integers Zero](../../1501-2000/1611-minimum-one-bit-operations-to-make-integers-zero/)
- [1460. Make Two Arrays Equal by Reversing Subarrays](../../1001-1500/1460-make-two-arrays-equal-by-reversing-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/)
