# LeetCode 3993: Maximum Value of an Alternating Sequence

**LeetCode Problem #3993 — Maximum Value of an Alternating Sequence**
Solve LeetCode Maximum Value of an Alternating Sequence using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Value of an Alternating Sequence |
| LeetCode | #3993 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three integers `n`, `s`, and `m`.

A sequence `seq` of integers of length `n` is considered **valid** if:

`seq[0] = s`. 
 The sequence is **alternating**, meaning that either:
 
 `seq[0] > seq[1] < seq[2] > ...`, or 
 `seq[0] < seq[1] > seq[2] < ...`. 
 
 
 For every adjacent pair, `|seq[i] - seq[i - 1]| <= m`.

A sequence of length 1 is considered alternating.

Return the **maximum** possible element that can appear in any valid sequence.

## Constraints
- `1 <= n, s <= 10^9`
- `1 <= m <= 10^5`

## Examples
### Example 1
- **Input:** `n = 4, s = 3, m = 5`
- **Output:** `12`
- **Explanation:** One valid sequence is `[3, 8, 7, 12]`. 
 The maximum element in the sequence is 12.

### Example 2
- **Input:** `n = 2, s = 4, m = 3`
- **Output:** `7`
- **Explanation:** One valid sequence is `[4, 7]`. 
 The maximum element in the sequence is 7.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Value of an Alternating Sequence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, s = 3, m = 5`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `12`.
4. **Verification:** One valid sequence is `[3, 8, 7, 12]`. 
 The maximum element in the sequence is 12.

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
var maximumValue = function(n, s, m) {
    if (n === 1) {
        return s;
    }

    return s + m + Math.floor((n - 2) / 2) * (m - 1);
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
- [3287. Find the Maximum Sequence Value of Array](../../3001-3500/3287-find-the-maximum-sequence-value-of-array/)
- [3796. Find Maximum Value in a Constrained Sequence](../../3501-4000/3796-find-maximum-value-in-a-constrained-sequence/)
- [1131. Maximum of Absolute Value Expression](../../1001-1500/1131-maximum-of-absolute-value-expression/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/)
