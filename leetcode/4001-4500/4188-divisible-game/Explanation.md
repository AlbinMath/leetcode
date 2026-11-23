# LeetCode 3984: Divisible Game

**LeetCode Problem #3984 — Divisible Game**
Solve LeetCode Divisible Game using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Divisible Game |
| LeetCode | #3984 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of length `n`.

Alice and Bob are playing a game. Alice chooses:

An integer `k` such that `k > 1`. 
 Two integers `l` and `r` such that `0 <= l <= r < n`.

Initially, both Alice's and Bob's scores are 0.

For each index `i` in the range `[l, r]` (inclusive):

If `nums[i]` is divisible by `k`, Alice's score **increases** by `nums[i]`. 
 Otherwise, Bob's score **increases** by `nums[i]`.

The **score difference** is Alice's score **minus** Bob's score.

Alice wants to **maximize** the score difference. If there are multiple values of `k` that achieve the **maximum** score difference, she chooses the **smallest** such `k`.

Return the **product** of the **maximum** score difference and the chosen value of `k`. Since the result can be large, return it **modulo** `10^9 + 7`.

## Constraints
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,4,6,8]`
- **Output:** `36`
- **Explanation:** Alice can choose `k = 2`, `l = 1`, and `r = 3`. 
 All values in `nums[1..3]` are divisible by 2, so Alice's score is `4 + 6 + 8 = 18`, while Bob's score is 0. 
 The score difference is 18, which is the maximum possible. Among all values of `k` that achieve this score difference, the smallest is 2. 
 Therefore, the answer is `18 * 2 = 36`.

### Example 2
- **Input:** `nums = [2,1,2]`
- **Output:** `6`
- **Explanation:** Alice can choose `k = 2`, `l = 0`, and `r = 2`. 
 The values `nums[0]` and `nums[2]` are divisible by 2, so Alice's score is `2 + 2 = 4`. The value `nums[1]` is not divisible by 2, so Bob's score is 1. 
 The score difference is `4 - 1 = 3`, which is the maximum possible. Among all values of `k` that achieve this score difference, the smallest is 2. 
 Therefore, the answer is `3 * 2 = 6`.

### Example 3
- **Input:** `nums = [1]`
- **Output:** `1000000005`
- **Explanation:** Alice must choose some `k > 1`. The smallest possible choice is `k = 2`. 
 Since `nums[0]` is not divisible by 2, Alice's score is 0, while Bob's score is 1. 
 The score difference is -1, which is the maximum possible. 
 Therefore, the answer is `-1 * 2 = -2`. Modulo `10^9 + 7`, this equals 1000000005.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Divisible Game**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,6,8]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `36`.
4. **Verification:** Alice can choose `k = 2`, `l = 1`, and `r = 3`. 
 All values in `nums[1..3]` are divisible by 2, so Alice's score is `4 + 6 + 8 = 18`, while Bob's score is 0. 
 The score difference is 18, which is the maximum possible. Among all values of `k` that achieve this score difference, the smallest is 2. 
 Therefore, the answer is `18 * 2 = 36`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var divisibleGame = function(nums) {
    const n = nums.length;
    const MOD = 1000000007n;

    // 1. Prefix sums of nums to compute negative gaps in O(1)
    const pref = new Float64Array(n + 1);
    let minElem = Infinity;
    for (let i = 0; i < n; i++) {
        pref[i + 1] = pref[i] + nums[i];
        if (nums[i] < minElem) minElem = nums[i];
    }

    // 2. Group indices by each distinct prime factor of nums[i]
    // Always include k = 2 as the baseline candidate
    const primeIndices = new Map();
    primeIndices.set(2, []);

    for (let i = 0; i < n; i++) {
        let x = nums[i];
        if (x % 2 === 0) {
            primeIndices.get(2).push(i);
            while (x % 2 === 0) x /= 2;
        }
        for (let d = 3; d * d <= x; d += 2) {
            if (x % d === 0) {
                if (!primeIndices.has(d)) primeIndices.set(d, []);
                primeIndices.get(d).push(i);
                while (x % d === 0) x /= d;
            }
        }
        if (x > 1) {
            if (!primeIndices.has(x)) primeIndices.set(x, []);
            primeIndices.get(x).push(i);
        }
    }

    // Sort candidate primes ascending so ties automatically keep the smallest k
    const primes = Array.from(primeIndices.keys()).sort((a, b) => a - b);

    // Baseline: single smallest element given to Bob with k = 2
    let bestDiff = -minElem;
    let bestK = 2;

    // 3. Run compressed Kadane's algorithm for each candidate prime
    for (const p of primes) {
        const indices = primeIndices.get(p);
        if (indices.length === 0) continue;

        let currentSum = nums[indices[0]];
        let maxSumForP = currentSum;

        for (let idx = 1; idx < indices.length; idx++) {
            const prev = indices[idx - 1];
            const curr = indices[idx];
            // Sum of elements strictly between prev and curr (all subtracted)
            const gapSum = pref[curr] - pref[prev + 1];

            currentSum = Math.max(nums[curr], currentSum - gapSum + nums[curr]);
            if (currentSum > maxSumForP) {
                maxSumForP = currentSum;
            }
        }

        if (maxSumForP > bestDiff) {
            bestDiff = maxSumForP;
            bestK = p;
        }
    }

    const ans = ((BigInt(bestDiff) * BigInt(bestK)) % MOD + MOD) % MOD;
    return Number(ans);
};
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
- [1015. Smallest Integer Divisible by K](../../1001-1500/1064-smallest-integer-divisible-by-k/)
- [1018. Binary Prefix Divisible By 5](../../1001-1500/1071-binary-prefix-divisible-by-5/)
- [1590. Make Sum Divisible by P](../../1501-2000/1694-make-sum-divisible-by-p/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/divisible-game/)
