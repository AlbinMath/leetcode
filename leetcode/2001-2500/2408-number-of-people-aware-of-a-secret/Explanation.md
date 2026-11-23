# LeetCode 2327: Number of People Aware of a Secret

**LeetCode Problem #2327 — Number of People Aware of a Secret**
Solve LeetCode Number of People Aware of a Secret using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of People Aware of a Secret |
| LeetCode | #2327 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
On day `1`, one person discovers a secret.

You are given an integer `delay`, which means that each person will **share** the secret with a new person **every day**, starting from `delay` days after discovering the secret. You are also given an integer `forget`, which means that each person will **forget** the secret `forget` days after discovering it. A person **cannot** share the secret on the same day they forgot it, or on any day afterwards.

Given an integer `n`, return* the number of people who know the secret at the end of day *`n`. Since the answer may be very large, return it **modulo** `10^9 + 7`.

## Constraints
- `2 <= n <= 1000`
- `1 <= delay < forget <= n`

## Examples
### Example 1
- **Input:** `n = 6, delay = 2, forget = 4`
- **Output:** `5`
- **Explanation:** Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)

### Example 2
- **Input:** `n = 4, delay = 1, forget = 3`
- **Output:** `6`
- **Explanation:** Day 1: The first person is named A. (1 person)
Day 2: A shares the secret with B. (2 people)
Day 3: A and B share the secret with 2 new people, C and D. (4 people)
Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of People Aware of a Secret**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 6, delay = 2, forget = 4`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `5`.
4. **Verification:** Day 1: Suppose the first person is named A. (1 person)
Day 2: A is the only person who knows the secret. (1 person)
Day 3: A shares the secret with a new person, B. (2 people)
Day 4: A shares the secret with a new person, C. (3 people)
Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
Day 6: B shares the secret with E, and C shares the secret with F. (5 people)

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {number} n
 * @param {number} delay
 * @param {number} forget
 * @return {number}
 */
var peopleAwareOfSecret = function (n, delay, forget) {
    const MOD = 1000000007;
    const nw = new Array(n + 1).fill(0);
    nw[1] = 1;
    let share = 0; // people able to share on the current day

    for (let d = 2; d <= n; d++) {
        if (d - delay >= 1) share = (share + nw[d - delay]) % MOD;
        if (d - forget >= 1) share = (share - nw[d - forget] + MOD) % MOD;
        nw[d] = share;
    }

    let ans = 0;
    for (let j = Math.max(1, n - forget + 1); j <= n; j++) {
        ans = (ans + nw[j]) % MOD;
    }
    return ans;
};
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1944. Number of Visible People in a Queue](../../1001-1500/1305-number-of-visible-people-in-a-queue/)
- [3025. Find the Number of Ways to Place People I](../../3001-3500/3278-find-the-number-of-ways-to-place-people-i/)
- [3027. Find the Number of Ways to Place People II](../../3001-3500/3277-find-the-number-of-ways-to-place-people-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-people-aware-of-a-secret/)
