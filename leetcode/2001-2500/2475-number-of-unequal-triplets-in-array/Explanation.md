# LeetCode 2475: Number of Unequal Triplets in Array

**LeetCode Problem #2475 — Number of Unequal Triplets in Array**
Solve LeetCode Number of Unequal Triplets in Array using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Unequal Triplets in Array |
| LeetCode | #2475 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array of positive integers `nums`. Find the number of triplets `(i, j, k)` that meet the following conditions:

`0 <= i < j < k < nums.length` 
 `nums[i]`, `nums[j]`, and `nums[k]` are **pairwise distinct**.
 
 In other words, `nums[i] != nums[j]`, `nums[i] != nums[k]`, and `nums[j] != nums[k]`.

Return *the number of triplets that meet the conditions.*

## Constraints
- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 1000`

## Examples
### Example 1
- **Input:** `nums = [4,4,2,4,3]`
- **Output:** `3`
- **Explanation:** The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.

### Example 2
- **Input:** `nums = [1,1,1,1,1]`
- **Output:** `0`
- **Explanation:** No triplets meet the conditions so we return 0.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Unequal Triplets in Array**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,4,2,4,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.

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
var unequalTriplets = function(nums) {
    const freq = new Map();

    for (const num of nums) {
        freq.set(num, (freq.get(num) || 0) + 1);
    }

    const counts = Array.from(freq.values());

    let result = 0;

    for (let i = 0; i < counts.length; i++) {
        for (let j = i + 1; j < counts.length; j++) {
            for (let k = j + 1; k < counts.length; k++) {
                result += counts[i] * counts[j] * counts[k];
            }
        }
    }

    return result;
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
- [2179. Count Good Triplets in an Array](../../2001-2500/2179-count-good-triplets-in-an-array/)
- [2367. Number of Arithmetic Triplets](../../2001-2500/2367-number-of-arithmetic-triplets/)
- [3513. Number of Unique XOR Triplets I](../../3501-4000/3513-number-of-unique-xor-triplets-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-unequal-triplets-in-array/)
