# LeetCode 128: Longest Consecutive Sequence

**LeetCode Problem #128 — Longest Consecutive Sequence**
Solve LeetCode Longest Consecutive Sequence using JavaScript, Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Consecutive Sequence |
| LeetCode | #128 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an unsorted array of integers `nums`, return *the length of the longest consecutive elements sequence.*

You must write an algorithm that runs in `O(n)` time.

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [100,4,200,1,3,2]`
- **Output:** `4`
- **Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

### Example 2
- **Input:** `nums = [0,3,7,2,5,8,4,6,0,1]`
- **Output:** `9`

### Example 3
- **Input:** `nums = [1,0,1,2]`
- **Output:** `3`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Consecutive Sequence**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [100,4,200,1,3,2]`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var longestConsecutive = function(nums) {
    const numSet = new Set(nums);
    let longest = 0;

    for (const num of numSet) {
        // Start only at the beginning of a sequence
        if (!numSet.has(num - 1)) {
            let currentNum = num;
            let length = 1;

            while (numSet.has(currentNum + 1)) {
                currentNum++;
                length++;
            }

            longest = Math.max(longest, length);
        }
    }

    return longest;
};
```

### Python
```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for x in s:
            if x - 1 not in s:
                y = x
                while y in s:
                    y += 1
                ans = max(ans, y - x)

        return ans
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
- [3872. Longest Arithmetic Sequence After Changing At Most One Element](../../4001-4500/4230-longest-arithmetic-sequence-after-changing-at-most-one-element/)
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)
