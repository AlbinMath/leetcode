# LeetCode 3756: Concatenate Non-Zero Digits and Multiply by Sum II

**LeetCode Problem #3756 — Concatenate Non-Zero Digits and Multiply by Sum II**
Solve LeetCode Concatenate Non-Zero Digits and Multiply by Sum II using Java and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Concatenate Non-Zero Digits and Multiply by Sum II |
| LeetCode | #3756 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of length `m` consisting of digits. You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

For each `queries[i]`, extract the ** substring ** `s[l_i..r_i]`. Then, perform the following:

Form a new integer `x` by concatenating all the **non-zero digits** from the substring in their original order. If there are no non-zero digits, `x = 0`. 
 Let `sum` be the **sum of digits** in `x`. The answer is `x * sum`.

Return an array of integers `answer` where `answer[i]` is the answer to the `i^th` query.

Since the answers may be very large, return them **modulo** `10^9 + 7`.

## Constraints
- `1 <= m == s.length <= 10^5`
- `s` consists of digits only.
- `1 <= queries.length <= 10^5`
- `queries[i] = [l_i, r_i]`
- `0 <= l_i <= r_i < m`

## Examples
### Example 1
- **Input:** `s = "10203004", queries = [[0,7],[1,3],[4,6]]`
- **Output:** `[12340, 4, 9]`
- **Explanation:** `s[0..7] = "10203004"`

 
 `x = 1234` 
 `sum = 1 + 2 + 3 + 4 = 10` 
 Therefore, answer is `1234 * 10 = 12340`. 
 
 
 `s[1..3] = "020"`
 
 `x = 2` 
 `sum = 2` 
 Therefore, the answer is `2 * 2 = 4`. 
 
 
 `s[4..6] = "300"`
 
 `x = 3` 
 `sum = 3` 
 Therefore, the answer is `3 * 3 = 9`.

### Example 2
- **Input:** `s = "1000", queries = [[0,3],[1,1]]`
- **Output:** `[1, 0]`
- **Explanation:** `s[0..3] = "1000"`

 
 `x = 1` 
 `sum = 1` 
 Therefore, the answer is `1 * 1 = 1`. 
 
 
 `s[1..1] = "0"`
 
 `x = 0` 
 `sum = 0` 
 Therefore, the answer is `0 * 0 = 0`.

### Example 3
- **Input:** `s = "9876543210", queries = [[0,9]]`
- **Output:** `[444444137]`
- **Explanation:** `s[0..9] = "9876543210"`

 
 `x = 987654321` 
 `sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45` 
 Therefore, the answer is `987654321 * 45 = 44444444445`. 
 We return `44444444445 modulo (10^9 + 7) = 444444137`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Concatenate Non-Zero Digits and Multiply by Sum II**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "10203004", queries = [[0,7],[1,3],[4,6]]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[12340, 4, 9]`.
4. **Verification:** `s[0..7] = "10203004"`

 
 `x = 1234` 
 `sum = 1 + 2 + 3 + 4 = 10` 
 Therefore, answer is `1234 * 10 = 12340`. 
 
 
 `s[1..3] = "020"`
 
 `x = 2` 
 `sum = 2` 
 Therefore, the answer is `2 * 2 = 4`. 
 
 
 `s[4..6] = "300"`
 
 `x = 3` 
 `sum = 3` 
 Therefore, the answer is `3 * 3 = 9`.

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
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    public int[] sumAndMultiply(String s, int[][] queries) {
        final long MOD = 1_000_000_007L;
        int n = s.length();

        // prefixNum[i] = value formed by non-zero digits in s[0..i-1]
        long[] prefixNum = new long[n + 1];

        // prefixSum[i] = sum of non-zero digits in s[0..i-1]
        long[] prefixSum = new long[n + 1];

        // prefixCount[i] = number of non-zero digits in s[0..i-1]
        int[] prefixCount = new int[n + 1];

        for (int i = 0; i < n; i++) {
            int digit = s.charAt(i) - '0';

            prefixNum[i + 1] = prefixNum[i];
            prefixSum[i + 1] = prefixSum[i];
            prefixCount[i + 1] = prefixCount[i];

            if (digit != 0) {
                prefixNum[i + 1] =
                    (prefixNum[i] * 10 + digit) % MOD;

                prefixSum[i + 1] += digit;
                prefixCount[i + 1]++;
            }
        }

        int[] answer = new int[queries.length];

        for (int q = 0; q < queries.length; q++) {
            int l = queries[q][0];
            int r = queries[q][1];

            // Number of non-zero digits in [l, r]
            int count = prefixCount[r + 1] - prefixCount[l];

            if (count == 0) {
                answer[q] = 0;
                continue;
            }

            // Sum of non-zero digits
            long sum = prefixSum[r + 1] - prefixSum[l];

            // To extract the concatenated number from the prefix,
            // remove the digits before l.
            long x;

            if (prefixCount[l] == 0) {
                x = prefixNum[r + 1];
            } else {
                long power = modPow(10, count);

                x = (prefixNum[r + 1]
                        - prefixNum[l] * power % MOD
                        + MOD) % MOD;
            }

            answer[q] = (int) (x * (sum % MOD) % MOD);
        }

        return answer;
    }

    private long modPow(long base, int exp) {
        final long MOD = 1_000_000_007L;
        long result = 1;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * base % MOD;
            }

            base = base * base % MOD;
            exp >>= 1;
        }

        return result;
    }
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
- [3754. Concatenate Non-Zero Digits and Multiply by Sum I](../../4001-4500/4135-concatenate-non-zero-digits-and-multiply-by-sum-i/)
- [689. Maximum Sum of 3 Non-Overlapping Subarrays](../../0501-1000/0689-maximum-sum-of-3-non-overlapping-subarrays/)
- [1031. Maximum Sum of Two Non-Overlapping Subarrays](../../1001-1500/1096-maximum-sum-of-two-non-overlapping-subarrays/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/)
