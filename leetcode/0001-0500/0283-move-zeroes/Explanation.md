# LeetCode 283: Move Zeroes

**LeetCode Problem #283 — Move Zeroes**
Solve LeetCode Move Zeroes using C++, JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Move Zeroes |
| LeetCode | #283 |
| Difficulty | Easy |
| Language | C++, JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

## Constraints
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `nums = [0,1,0,3,12]`
- **Output:** `[1,3,12,0,0]`

### Example 2
- **Input:** `nums = [0]`
- **Output:** `[0]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Move Zeroes**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,0,3,12]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,3,12,0,0]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++, JavaScript

## Source Code
- [solution.cpp](./solution.cpp)
- [solution.js](./solution.js)


### C++
```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int pos = 0;

        // Move all non-zero elements to the front
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[pos] = nums[i];
                pos++;
            }
        }

        // Fill the remaining positions with zero
        while (pos < nums.size()) {
            nums[pos] = 0;
            pos++;
        }
    }
};
```

### JavaScript
```javascript
var moveZeroes = function(nums) {
    let position = 0;

    // Move all non-zero elements to the front
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            [nums[position], nums[i]] = [nums[i], nums[position]];
            position++;
        }
    }
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
- [73. Set Matrix Zeroes](../../0001-0500/0073-set-matrix-zeroes/)
- [172. Factorial Trailing Zeroes](../../0001-0500/0172-factorial-trailing-zeroes/)
- [474. Ones and Zeroes](../../0001-0500/0474-ones-and-zeroes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/move-zeroes/)
