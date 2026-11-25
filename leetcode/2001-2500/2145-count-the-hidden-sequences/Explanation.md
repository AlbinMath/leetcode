# LeetCode 2145: Count the Hidden Sequences

**LeetCode Problem #2145 — Count the Hidden Sequences**
Solve LeetCode Count the Hidden Sequences using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count the Hidden Sequences |
| LeetCode | #2145 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array of `n` integers `differences`, which describes the **differences **between each pair of **consecutive **integers of a **hidden** sequence of length `(n + 1)`. More formally, call the hidden sequence `hidden`, then we have that `differences[i] = hidden[i + 1] - hidden[i]`.

You are further given two integers `lower` and `upper` that describe the **inclusive** range of values `[lower, upper]` that the hidden sequence can contain.

For example, given `differences = [1, -3, 4]`, `lower = 1`, `upper = 6`, the hidden sequence is a sequence of length `4` whose elements are in between `1` and `6` (**inclusive**).

`[3, 4, 1, 5]` and `[4, 5, 2, 6]` are possible hidden sequences. 
 `[5, 6, 3, 7]` is not possible since it contains an element greater than `6`. 
 `[1, 2, 3, 4]` is not possible since the differences are not correct.

Return *the number of **possible** hidden sequences there are.* If there are no possible sequences, return `0`.

## Constraints
- `n == differences.length`
- `1 <= n <= 10^5`
- `-10^5 <= differences[i] <= 10^5`
- `-10^5 <= lower <= upper <= 10^5`

## Examples
### Example 1
- **Input:** `differences = [1,-3,4], lower = 1, upper = 6`
- **Output:** `2`
- **Explanation:** The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
Thus, we return 2.

### Example 2
- **Input:** `differences = [3,-4,5,1,-2], lower = -4, upper = 5`
- **Output:** `4`
- **Explanation:** The possible hidden sequences are:
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
Thus, we return 4.

### Example 3
- **Input:** `differences = [4,-7,2], lower = 3, upper = 6`
- **Output:** `0`
- **Explanation:** There are no possible hidden sequences. Thus, we return 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count the Hidden Sequences**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `differences = [1,-3,4], lower = 1, upper = 6`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
Thus, we return 2.

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
var numberOfArrays = function(differences, lower, upper) {
    let current = 0;
    let min = 0;
    let max = 0;

    for (let diff of differences) {
        current += diff;

        min = Math.min(min, current);
        max = Math.max(max, current);
    }

    return Math.max(0, (upper - lower) - (max - min) + 1);
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
- [2954. Count the Number of Infection Sequences](../../2501-3000/2954-count-the-number-of-infection-sequences/)
- [3850. Count Sequences to K](../../3501-4000/3850-count-sequences-to-k/)
- [4002. Count Valid Sequences](../../4001-4500/4002-count-valid-sequences/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-the-hidden-sequences/)
