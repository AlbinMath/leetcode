# LeetCode 3978: Unique Middle Element

**LeetCode Problem #3978 — Unique Middle Element**
Solve LeetCode Unique Middle Element using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Unique Middle Element |
| LeetCode | #3978 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of odd length `n`.

Return `true` if the middle element of `nums` appears **exactly** once in the array. Otherwise return `false`.

## Constraints
- `1 <= n == nums.length <= 100`
- `n` is odd.
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `true`
- **Explanation:** The middle element of `nums` is 2, which appears exactly once. 

 Thus, the answer is `true`.

### Example 2
- **Input:** `nums = [1,2,2]`
- **Output:** `false`
- **Explanation:** The middle element of `nums` is 2, which appears twice. 

 Thus, the answer is `false`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Unique Middle Element**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The middle element of `nums` is 2, which appears exactly once. 

 Thus, the answer is `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var isMiddleElementUnique = function(nums) {
    const mid = Math.floor(nums.length / 2);
    const middle = nums[mid];

    let count = 0;

    for (const num of nums) {
        if (num === middle) {
            count++;
        }
    }

    return count === 1;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [3843. First Element with Unique Frequency](../../3501-4000/3843-first-element-with-unique-frequency/)
- [3866. First Unique Even Element](../../3501-4000/3866-first-unique-even-element/)
- [3395. Subsequences with a Unique Middle Mode I](../../3001-3500/3395-subsequences-with-a-unique-middle-mode-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/unique-middle-element/)
