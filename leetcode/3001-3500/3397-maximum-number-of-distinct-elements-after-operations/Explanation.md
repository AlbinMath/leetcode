# LeetCode 3397: Maximum Number of Distinct Elements After Operations

**LeetCode Problem #3397 — Maximum Number of Distinct Elements After Operations**
Solve LeetCode Maximum Number of Distinct Elements After Operations using JavaScript and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Distinct Elements After Operations |
| LeetCode | #3397 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` and an integer `k`.

You are allowed to perform the following **operation** on each element of the array **at most** *once*:

Add an integer in the range `[-k, k]` to the element.

Return the **maximum** possible number of **distinct** elements in `nums` after performing the **operations**.

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,3,3,4], k = 2`
- **Output:** `6`
- **Explanation:** `nums` changes to `[-1, 0, 1, 2, 3, 4]` after performing operations on the first four elements.

### Example 2
- **Input:** `nums = [4,4,4,4], k = 1`
- **Output:** `3`
- **Explanation:** By adding -1 to `nums[0]` and 1 to `nums[1]`, `nums` changes to `[3, 5, 4, 4]`.

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Maximum Number of Distinct Elements After Operations**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,3,3,4], k = 2`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** `nums` changes to `[-1, 0, 1, 2, 3, 4]` after performing operations on the first four elements.

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
var maxDistinctElements = function(nums, k) {
    nums.sort((a, b) => a - b);

    let count = 0;
    let lastUsed = -Infinity;

    for (const num of nums) {
        const smallest = num - k;
        const largest = num + k;
        const chosen = Math.max(smallest, lastUsed + 1);

        if (chosen <= largest) {
            count++;
            lastUsed = chosen;
        }
    }

    return count;
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
- [2442. Count Number of Distinct Integers After Reverse Operations](../../2001-2500/2442-count-number-of-distinct-integers-after-reverse-operations/)
- [2317. Maximum XOR After Operations ](../../2001-2500/2317-maximum-xor-after-operations/)
- [2654. Minimum Number of Operations to Make All Array Elements Equal to 1](../../2501-3000/2654-minimum-number-of-operations-to-make-all-array-elements-equal-to-1/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/)
