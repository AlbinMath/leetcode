# LeetCode 4026: Maximum Gap Between Stations

**LeetCode Problem #4026 — Maximum Gap Between Stations**
Solve LeetCode Maximum Gap Between Stations using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Gap Between Stations |
| LeetCode | #4026 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two strings `skill` and `station` of lengths `n` and `m`, respectively.

`skill[i]` represents the skill of worker `i`, and `station[j]` represents the skill supported by station `j`.

You must assign **every** worker to a **distinct** station. Let `j_i` be the index of the station assigned to worker `i`. A valid assignment must satisfy:

`station[j_i] == skill[i]` for every `0 <= i < n`. 
 The assigned station indices must be **strictly** increasing in worker order, meaning `j_0 < j_1 < ... < j_n - 1`.

The **gap** of an assignment is the **maximum difference** between the station indices assigned to two **consecutive** workers. In other words, it is `max(j_i - j_i - 1)` over all `1 <= i < n`.

If there is only one worker, the gap is 0.

Return the **maximum** possible gap among all valid assignments. It is guaranteed that **at least** one valid assignment exists.

## Constraints
- `skill.length == n`
- `station.length == m`
- `1 <= n <= m <= 10^5`
- `skill` and `station` consist of lowercase English letters.
- It is guaranteed that a valid assignment exists for every worker.

## Examples
### Example 1
- **Input:** `skill = "aa", station = "aaaa"`
- **Output:** `3`
- **Explanation:** The two workers must be assigned to two different `'a'` stations. 
 Assigning them to stations `[0, 3]` gives a gap of 3.

### Example 2
- **Input:** `skill = "xyz", station = "xyzz"`
- **Output:** `2`
- **Explanation:** Assign worker 0 to station `j = 0`, and worker 1 to station `j = 1`. 
 To maximize the gap, assign worker 2 to station `j = 3`. 
 This gives the assignment `[0, 1, 3]` with gaps `[1, 2]`, so the gap is 2.

### Example 3
- **Input:** `skill = "cbc", station = "cbcdbc"`
- **Output:** `4`
- **Explanation:** Assign worker 0 to station `j = 0`, and worker 1 to station `j = 1`. 
 To maximize the gap, assign worker 2 to station `j = 5`. 
 This gives the assignment `[0, 1, 5]` with gaps `[1, 4]`, so the gap is 4.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Gap Between Stations**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `skill = "aa", station = "aaaa"`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The two workers must be assigned to two different `'a'` stations. 
 Assigning them to stations `[0, 3]` gives a gap of 3.

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
var maximumGap = function(skill, station) {
    const n = skill.length;
    const m = station.length;

    const earliest = new Array(n);
    const latest = new Array(n);

    let j = 0;

    for (let i = 0; i < n; i++) {
        while (station[j] !== skill[i]) {
            j++;
        }

        earliest[i] = j;
        j++;
    }

    j = m - 1;

    for (let i = n - 1; i >= 0; i--) {
        while (station[j] !== skill[i]) {
            j--;
        }

        latest[i] = j;
        j--;
    }

    let answer = 0;

    for (let i = 1; i < n; i++) {
        answer = Math.max(
            answer,
            latest[i] - earliest[i - 1]
        );
    }

    return answer;
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
- [1026. Maximum Difference Between Node and Ancestor](../../1001-1500/1026-maximum-difference-between-node-and-ancestor/)
- [1855. Maximum Distance Between a Pair of Values](../../1501-2000/1855-maximum-distance-between-a-pair-of-values/)
- [1913. Maximum Product Difference Between Two Pairs](../../1501-2000/1913-maximum-product-difference-between-two-pairs/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-gap-between-stations/)
