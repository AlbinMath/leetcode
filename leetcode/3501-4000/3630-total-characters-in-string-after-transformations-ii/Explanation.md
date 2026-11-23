# LeetCode 3337: Total Characters in String After Transformations II

**LeetCode Problem #3337 — Total Characters in String After Transformations II**
Solve LeetCode Total Characters in String After Transformations II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Total Characters in String After Transformations II |
| LeetCode | #3337 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters, an integer `t` representing the number of **transformations** to perform, and an array `nums` of size 26. In one **transformation**, every character in `s` is replaced according to the following rules:

Replace `s[i]` with the **next** `nums[s[i] - 'a']` consecutive characters in the alphabet. For example, if `s[i] = 'a'` and `nums[0] = 3`, the character `'a'` transforms into the next 3 consecutive characters ahead of it, which results in `"bcd"`. 
 The transformation **wraps** around the alphabet if it exceeds `'z'`. For example, if `s[i] = 'y'` and `nums[24] = 3`, the character `'y'` transforms into the next 3 consecutive characters ahead of it, which results in `"zab"`.

Return the length of the resulting string after **exactly** `t` transformations.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.
- `1 <= t <= 10^9`
- ` nums.length == 26 `
- ` 1 <= nums[i] <= 25 `

## Examples
### Example 1
- **Input:** `s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]`
- **Output:** `7`

### Example 2
- **Input:** `s = "azbk", t = 1, nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]`
- **Output:** `8`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Total Characters in String After Transformations II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var lengthAfterTransformations = function(s, t, nums) {
    const MOD = 1000000007n;
    const n = 26;

    // Initial frequency
    let freq = Array(n).fill(0n);

    for (const ch of s) {
        freq[ch.charCodeAt(0) - 97]++;
    }

    // Build transformation matrix
    let M = Array.from({ length: n }, () => Array(n).fill(0n));

    for (let j = 0; j < n; j++) {
        for (let k = 1; k <= nums[j]; k++) {
            let d = (j + k) % n;
            M[d][j] = 1n;
        }
    }

    // Matrix multiplication
    function multiply(A, B) {
        let C = Array.from({ length: n }, () => Array(n).fill(0n));

        for (let i = 0; i < n; i++) {
            for (let k = 0; k < n; k++) {
                if (A[i][k] === 0n) continue;

                for (let j = 0; j < n; j++) {
                    if (B[k][j] === 0n) continue;

                    C[i][j] = (
                        C[i][j] + A[i][k] * B[k][j]
                    ) % MOD;
                }
            }
        }

        return C;
    }

    // Matrix-vector multiplication
    function multiplyVector(A, v) {
        let result = Array(n).fill(0n);

        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                result[i] = (
                    result[i] + A[i][j] * v[j]
                ) % MOD;
            }
        }

        return result;
    }

    // Binary exponentiation
    while (t > 0) {
        if (t % 2 === 1) {
            freq = multiplyVector(M, freq);
        }

        M = multiply(M, M);
        t = Math.floor(t / 2);
    }

    // Final length
    let ans = 0n;

    for (const x of freq) {
        ans = (ans + x) % MOD;
    }

    return Number(ans);
};
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3335. Total Characters in String After Transformations I](../../3501-4000/3629-total-characters-in-string-after-transformations-i/)
- [3816. Lexicographically Smallest String After Deleting Duplicate Characters](../../4001-4500/4086-lexicographically-smallest-string-after-deleting-duplicate-characters/)
- [4036. Lexicographically Largest String After Pair Transformations](../../4001-4500/4366-lexicographically-largest-string-after-pair-transformations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/)
