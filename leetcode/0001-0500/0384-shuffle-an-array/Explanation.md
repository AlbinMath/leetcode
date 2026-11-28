# LeetCode 384: Shuffle an Array

**LeetCode Problem #384 — Shuffle an Array**
Solve LeetCode Shuffle an Array using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Shuffle an Array |
| LeetCode | #384 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an integer array `nums`, design an algorithm to randomly shuffle the array. All permutations of the array should be **equally likely** as a result of the shuffling.

Implement the `Solution` class:

`Solution(int[] nums)` Initializes the object with the integer array `nums`. 
 `int[] reset()` Resets the array to its original configuration and returns it. 
 `int[] shuffle()` Returns a random shuffling of the array.

## Constraints
- `1 <= nums.length <= 50`
- `-10^6 <= nums[i] <= 10^6`
- All the elements of `nums` are **unique**.
- At most `10^4` calls **in total** will be made to `reset` and `shuffle`.

## Examples
### Example 1
- **Input:** `["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]`
- **Output:** `[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]`
- **Explanation:** Solution solution = new Solution([1, 2, 3]);
solution.shuffle(); // Shuffle the array [1,2,3] and return its result.
 // Any permutation of [1,2,3] must be equally likely to be returned.
 // Example: return [3, 1, 2]
solution.reset(); // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle(); // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Shuffle an Array**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]`.
4. **Verification:** Solution solution = new Solution([1, 2, 3]);
solution.shuffle(); // Shuffle the array [1,2,3] and return its result.
 // Any permutation of [1,2,3] must be equally likely to be returned.
 // Example: return [3, 1, 2]
solution.reset(); // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle(); // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

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
import random

class Solution(object):

    def __init__(self, nums):
        self.original = list(nums)
        self.array = list(nums)

    def reset(self):
        self.array = list(self.original)
        return self.array

    def shuffle(self):
        n = len(self.array)
        for i in range(n):
            swap_idx = random.randrange(i, n)
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
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
- [1470. Shuffle the Array](../../1001-1500/1470-shuffle-the-array/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/shuffle-an-array/)
