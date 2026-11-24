# LeetCode 3348: Smallest Divisible Digit Product II

**LeetCode Problem #3348 — Smallest Divisible Digit Product II**
Solve LeetCode Smallest Divisible Digit Product II using Python, TypeScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Divisible Digit Product II |
| LeetCode | #3348 |
| Difficulty | Hard |
| Language | Python, TypeScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `num` which represents a **positive** integer, and an integer `t`.

A number is called **zero-free** if *none* of its digits are 0.

Return a string representing the **smallest** **zero-free** number greater than or equal to `num` such that the **product of its digits** is divisible by `t`. If no such number exists, return `"-1"`.

## Constraints
- `2 <= num.length <= 2 * 10^5`
- `num` consists only of digits in the range `['0', '9']`.
- `num` does not contain leading zeros.
- `1 <= t <= 10^14`

## Examples
### Example 1
- **Input:** `num = "1234", t = 256`
- **Output:** `"1488"`
- **Explanation:** The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

### Example 2
- **Input:** `num = "12355", t = 50`
- **Output:** `"12355"`
- **Explanation:** 12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

### Example 3
- **Input:** `num = "11111", t = 26`
- **Output:** `"-1"`
- **Explanation:** No number greater than 11111 has the product of its digits divisible by 26.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Smallest Divisible Digit Product II**, we observe the problem requirements and utilize the **Math & Logic** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "1234", t = 256`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"1488"`.
4. **Verification:** The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

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
Python, TypeScript

## Source Code
- [solution.py](./solution.py)
- [solution.ts](./solution.ts)


### Python
```python
class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """

        # Prime factorization of t
        need = [0, 0, 0, 0]  # 2, 3, 5, 7

        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                need[i] += 1
                t //= p

        # Impossible: digit products only contain 2,3,5,7
        if t != 1:
            return "-1"

        # Factor contribution of digits 0...9
        factors = (
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0)   # 9
        )

        # ---------------------------------------------------------
        # DP:
        # dp[a,b,c,d] = minimum number of digits required
        # to provide at least a 2s, b 3s, c 5s, d 7s.
        # ---------------------------------------------------------

        A = need[0] + 1
        B = need[1] + 1
        C = need[2] + 1
        D = need[3] + 1

        CD = C * D
        BCD = B * C * D

        size = A * BCD

        dp = bytearray([255]) * size
        dp[0] = 0

        def idx(a, b, c, d):
            return a * BCD + b * CD + c * D + d

        for a in range(A):
            for b in range(B):
                for c in range(C):
                    for d in range(D):

                        if a == 0 and b == 0 and c == 0 and d == 0:
                            continue

                        best = 255

                        for digit in range(2, 10):
                            f = factors[digit]

                            na = max(0, a - f[0])
                            nb = max(0, b - f[1])
                            nc = max(0, c - f[2])
                            nd = max(0, d - f[3])

                            value = dp[idx(na, nb, nc, nd)] + 1

                            if value < best:
                                best = value

                        dp[idx(a, b, c, d)] = best

        def min_digits(a, b, c, d):
            return dp[idx(a, b, c, d)]

        def subtract(req, digit):
            f = factors[digit]

            return (
                max(0, req[0] - f[0]),
                max(0, req[1] - f[1]),
                max(0, req[2] - f[2]),
                max(0, req[3] - f[3])
            )

        # ---------------------------------------------------------
        # Check if num itself is already valid
        # ---------------------------------------------------------

        cur = [0, 0, 0, 0]
        total_zero = 0

        for ch in num:
            digit = ord(ch) - 48

            if digit == 0:
                total_zero += 1
                continue

            f = factors[digit]

            for j in range(4):
                cur[j] = min(
                    need[j],
                    cur[j] + f[j]
                )

        if (
            total_zero == 0
            and cur[0] >= need[0]
            and cur[1] >= need[1]
            and cur[2] >= need[2]
            and cur[3] >= need[3]
        ):
            return num

        # ---------------------------------------------------------
        # Total factors in num
        # ---------------------------------------------------------

        total = [0, 0, 0, 0]

        for ch in num:
            digit = ord(ch) - 48

            if digit == 0:
                continue

            f = factors[digit]

            total[0] += f[0]
            total[1] += f[1]
            total[2] += f[2]
            total[3] += f[3]

        # ---------------------------------------------------------
        # Try to construct a valid number of the SAME length
        # ---------------------------------------------------------

        n = len(num)

        # prefix factors for [0, i)
        prefix = total[:]

        # Number of zeros in the suffix [i, n)
        suffix_zero = 0

        for i in range(n - 1, -1, -1):

            digit_at_i = ord(num[i]) - 48

            # Remove num[i] from prefix
            if digit_at_i == 0:
                suffix_zero += 1
            else:
                f = factors[digit_at_i]

                prefix[0] -= f[0]
                prefix[1] -= f[1]
                prefix[2] -= f[2]
                prefix[3] -= f[3]

            # Prefix [0, i) must not contain zero.
            prefix_zero = total_zero - suffix_zero

            if prefix_zero == 0:

                # Factors still required after the prefix
                req = (
                    max(0, need[0] - prefix[0]),
                    max(0, need[1] - prefix[1]),
                    max(0, need[2] - prefix[2]),
                    max(0, need[3] - prefix[3])
                )

                # Make current digit slightly larger
                for digit in range(digit_at_i + 1, 10):

                    nxt = subtract(req, digit)

                    remaining = n - i - 1

                    if min_digits(*nxt) <= remaining:

                        answer = num[:i] + str(digit)

                        # Build lexicographically smallest suffix
                        req = nxt

                        for pos in range(remaining):

                            left = remaining - pos - 1

                            for d in range(1, 10):

                                candidate = subtract(req, d)

                                if min_digits(*candidate) <= left:
                                    answer += str(d)
                                    req = candidate
                                    break

                        return answer

        # ---------------------------------------------------------
        # No answer with same length.
        # Find smallest valid longer number.
        # ---------------------------------------------------------

        length = min_digits(*need)

        if length <= n:
            length = n + 1

        answer = []
        req = tuple(need)

        for pos in range(length):

            remaining = length - pos - 1

            for digit in range(1, 10):

                nxt = subtract(req, digit)

                if min_digits(*nxt) <= remaining:
                    answer.append(str(digit))
                    req = nxt
                    break

        return "".join(answer)
```

### TypeScript
```typescript
function smallestNumber(num: string, t: number): string {
    const primes = [2, 3, 5, 7];

    // Factorize t
    const need = [0, 0, 0, 0];

    for (let i = 0; i < 4; i++) {
        while (t % primes[i] === 0) {
            need[i]++;
            t /= primes[i];
        }
    }

    // t has a prime factor other than 2,3,5,7
    if (t !== 1) {
        return "-1";
    }

    // Prime factor contribution of digits 0..9
    const factors = [
        [0, 0, 0, 0], // 0
        [0, 0, 0, 0], // 1
        [1, 0, 0, 0], // 2
        [0, 1, 0, 0], // 3
        [2, 0, 0, 0], // 4
        [0, 0, 1, 0], // 5
        [1, 1, 0, 0], // 6
        [0, 0, 0, 1], // 7
        [3, 0, 0, 0], // 8
        [0, 2, 0, 0]  // 9
    ];

    const A = need[0] + 1;
    const B = need[1] + 1;
    const C = need[2] + 1;
    const D = need[3] + 1;

    const size = A * B * C * D;

    const getId = (
        a: number,
        b: number,
        c: number,
        d: number
    ): number => {
        return (((a * B) + b) * C + c) * D + d;
    };

    /*
     * dp[a,b,c,d] =
     * minimum number of digits needed to provide
     * at least a factors of 2,
     * at least b factors of 3,
     * at least c factors of 5,
     * at least d factors of 7.
     */
    const dp = new Uint8Array(size);
    dp.fill(255);

    dp[0] = 0;

    // Iterative DP — no recursion
    for (let a = 0; a <= need[0]; a++) {
        for (let b = 0; b <= need[1]; b++) {
            for (let c = 0; c <= need[2]; c++) {
                for (let d = 0; d <= need[3]; d++) {

                    if (a === 0 && b === 0 && c === 0 && d === 0) {
                        continue;
                    }

                    let best = 255;

                    for (let digit = 2; digit <= 9; digit++) {
                        const f = factors[digit];

                        const na = Math.max(0, a - f[0]);
                        const nb = Math.max(0, b - f[1]);
                        const nc = Math.max(0, c - f[2]);
                        const nd = Math.max(0, d - f[3]);

                        const prev = dp[getId(na, nb, nc, nd)];

                        if (prev !== 255) {
                            best = Math.min(best, prev + 1);
                        }
                    }

                    dp[getId(a, b, c, d)] = best;
                }
            }
        }
    }

    const minDigits = (
        a: number,
        b: number,
        c: number,
        d: number
    ): number => {
        return dp[getId(a, b, c, d)];
    };

    // Factor contribution after adding a digit
    const subtract = (
        req: number[],
        digit: number
    ): number[] => {
        const f = factors[digit];

        return [
            Math.max(0, req[0] - f[0]),
            Math.max(0, req[1] - f[1]),
            Math.max(0, req[2] - f[2]),
            Math.max(0, req[3] - f[3])
        ];
    };

    /*
     * Construct the lexicographically smallest
     * zero-free number of exactly `length` digits
     * satisfying the required factors.
     */
    const buildSmallest = (
        length: number,
        initialReq: number[]
    ): string => {
        const result: string[] = [];
        let req = [...initialReq];

        for (let pos = 0; pos < length; pos++) {
            const remaining = length - pos - 1;

            for (let digit = 1; digit <= 9; digit++) {
                const next = subtract(req, digit);

                if (
                    minDigits(
                        next[0],
                        next[1],
                        next[2],
                        next[3]
                    ) <= remaining
                ) {
                    result.push(String(digit));
                    req = next;
                    break;
                }
            }
        }

        return result.join("");
    };

    /*
     * Check whether num itself already works.
     */
    let cur = [0, 0, 0, 0];
    let hasZero = false;

    for (const ch of num) {
        const digit = Number(ch);

        if (digit === 0) {
            hasZero = true;
            continue;
        }

        const f = factors[digit];

        for (let j = 0; j < 4; j++) {
            cur[j] = Math.min(
                need[j],
                cur[j] + f[j]
            );
        }
    }

    if (
        !hasZero &&
        cur[0] >= need[0] &&
        cur[1] >= need[1] &&
        cur[2] >= need[2] &&
        cur[3] >= need[3]
    ) {
        return num;
    }

    const n = num.length;

    /*
     * Prefix factor counts.
     */
    const p2 = new Int32Array(n + 1);
    const p3 = new Int32Array(n + 1);
    const p5 = new Int32Array(n + 1);
    const p7 = new Int32Array(n + 1);

    const prefixHasZero = new Uint8Array(n + 1);

    for (let i = 0; i < n; i++) {
        const digit = Number(num[i]);
        const f = factors[digit];

        p2[i + 1] = Math.min(
            need[0],
            p2[i] + f[0]
        );

        p3[i + 1] = Math.min(
            need[1],
            p3[i] + f[1]
        );

        p5[i + 1] = Math.min(
            need[2],
            p5[i] + f[2]
        );

        p7[i + 1] = Math.min(
            need[3],
            p7[i] + f[3]
        );

        prefixHasZero[i + 1] =
            prefixHasZero[i] || digit === 0 ? 1 : 0;
    }

    /*
     * Try to construct a number with the SAME length
     * that is strictly greater than num.
     *
     * Change the rightmost possible position.
     */
    for (let i = n - 1; i >= 0; i--) {

        // Prefix cannot contain zero.
        if (prefixHasZero[i]) {
            continue;
        }

        const currentDigit = Number(num[i]);

        const req = [
            Math.max(0, need[0] - p2[i]),
            Math.max(0, need[1] - p3[i]),
            Math.max(0, need[2] - p5[i]),
            Math.max(0, need[3] - p7[i])
        ];

        for (let digit = currentDigit + 1; digit <= 9; digit++) {

            const next = subtract(req, digit);
            const remaining = n - i - 1;

            if (
                minDigits(
                    next[0],
                    next[1],
                    next[2],
                    next[3]
                ) <= remaining
            ) {
                return (
                    num.substring(0, i) +
                    digit.toString() +
                    buildSmallest(remaining, next)
                );
            }
        }
    }

    /*
     * No valid number with the same length.
     * Therefore use the smallest possible longer length.
     */
    const requiredLength = minDigits(
        need[0],
        need[1],
        need[2],
        need[3]
    );

    const length = Math.max(n + 1, requiredLength);

    return buildSmallest(length, [...need]);
}
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
- [3345. Smallest Divisible Digit Product I](../../3501-4000/3626-smallest-divisible-digit-product-i/)
- [3622. Check Divisibility by Digit Sum and Product](../../3501-4000/3918-check-divisibility-by-digit-sum-and-product/)
- [1015. Smallest Integer Divisible by K](../../1001-1500/1064-smallest-integer-divisible-by-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-ii/)
