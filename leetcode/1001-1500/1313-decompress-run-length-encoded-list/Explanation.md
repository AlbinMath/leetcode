# LeetCode 1313: Decompress Run-Length Encoded List

**LeetCode Problem #1313 — Decompress Run-Length Encoded List**
Solve LeetCode Decompress Run-Length Encoded List using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decompress Run-Length Encoded List |
| LeetCode | #1313 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We are given a list `nums` of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements `[freq, val] = [nums[2*i], nums[2*i+1]]` (with `i >= 0`). For each such pair, there are `freq` elements with value `val` concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.

## Constraints
- `2 <= nums.length <= 100`
- `nums.length % 2 == 0`
- ` 1 <= nums[i] <= 100 `

## Examples
### Example 1
- **Input:** `nums = [1,2,3,4]`
- **Output:** `[2,4,4,4]`
- **Explanation:** The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

### Example 2
- **Input:** `nums = [1,1,2,3]`
- **Output:** `[1,3,3]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Decompress Run-Length Encoded List**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,4,4,4]`.
4. **Verification:** The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        result = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]

            result.extend([val] * freq)

        return result
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
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)
- [718. Maximum Length of Repeated Subarray](../../0501-1000/0718-maximum-length-of-repeated-subarray/)
- [1239. Maximum Length of a Concatenated String with Unique Characters](../../1001-1500/1239-maximum-length-of-a-concatenated-string-with-unique-characters/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/decompress-run-length-encoded-list/)
