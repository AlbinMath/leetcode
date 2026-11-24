# LeetCode 2523: Closest Prime Numbers in Range

**LeetCode Problem #2523 — Closest Prime Numbers in Range**
Solve LeetCode Closest Prime Numbers in Range using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Closest Prime Numbers in Range |
| LeetCode | #2523 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two positive integers `left` and `right`, find the two integers `num1` and `num2` such that:

`left <= num1 < num2 <= right `. 
 Both `num1` and `num2` are prime numbers . 
 `num2 - num1` is the **minimum** amongst all other pairs satisfying the above conditions.

Return the positive integer array `ans = [num1, num2]`. If there are multiple pairs satisfying these conditions, return the one with the **smallest** `num1` value. If no such numbers exist, return `[-1, -1]`*.*

## Constraints
- `1 <= left <= right <= 10^6`

## Examples
### Example 1
- **Input:** `left = 10, right = 19`
- **Output:** `[11,13]`
- **Explanation:** The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

### Example 2
- **Input:** `left = 4, right = 6`
- **Output:** `[-1,-1]`
- **Explanation:** There exists only one prime number in the given range, so the conditions cannot be satisfied.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Closest Prime Numbers in Range**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `left = 10, right = 19`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[11,13]`.
4. **Verification:** The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var closestPrimes = function(left, right) {
    const isPrime = new Uint8Array(right + 1);
    isPrime.fill(1);

    isPrime[0] = 0;
    isPrime[1] = 0;

    for (let i = 2; i * i <= right; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= right; j += i) {
                isPrime[j] = 0;
            }
        }
    }

    let prev = -1;
    let minGap = Infinity;
    let ans = [-1, -1];

    for (let num = left; num <= right; num++) {
        if (isPrime[num]) {
            if (prev !== -1 && num - prev < minGap) {
                minGap = num - prev;
                ans = [prev, num];

                if (minGap === 2) {
                    return ans;
                }
            }

            prev = num;
        }
    }

    return ans;
};
```

### Python
```python
class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        p = bytearray(b'\x01') * (right + 1)
        p[0:2] = b'\x00\x00'
        for i in range(2, int(right**0.5) + 1):
            if p[i]:
                p[i*i:right+1:i] = b'\x00' * ((right - i*i) // i + 1)

        primes = [i for i in range(max(2, left), right + 1) if p[i]]
        ans, gap = [-1, -1], float('inf')
        for a, b in zip(primes, primes[1:]):
            if b - a < gap:
                ans, gap = [a, b], b - a
                if gap == 2:
                    break
        return ans
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
- [201. Bitwise AND of Numbers Range](../../0001-0500/0201-bitwise-and-of-numbers-range/)
- [1523. Count Odd Numbers in an Interval Range](../../1501-2000/1523-count-odd-numbers-in-an-interval-range/)
- [3751. Total Waviness of Numbers in Range I](../../3501-4000/3751-total-waviness-of-numbers-in-range-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/closest-prime-numbers-in-range/)
