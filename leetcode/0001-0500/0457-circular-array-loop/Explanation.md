# LeetCode 457: Circular Array Loop

**LeetCode Problem #457 — Circular Array Loop**
Solve LeetCode Circular Array Loop using Python and Fast & Slow Pointers. This solution finds the optimal result using Floyd Cycle Detection in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Circular Array Loop |
| LeetCode | #457 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Floyd Cycle Detection |
| Data Structure | Linked List / Pointer |
| Pattern | Fast & Slow Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are playing a game involving a **circular** array of non-zero integers `nums`. Each `nums[i]` denotes the number of indices forward/backward you must move if you are located at index `i`:

If `nums[i]` is positive, move `nums[i]` steps **forward**, and 
 If `nums[i]` is negative, move `abs(nums[i])` steps **backward**.

Since the array is **circular**, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A **cycle** in the array consists of a sequence of indices `seq` of length `k` where:

Following the movement rules above results in the repeating index sequence `seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...` 
 Every `nums[seq[j]]` is either **all positive** or **all negative**. 
 `k > 1`

Return `true`* if there is a **cycle** in *`nums`*, or *`false`* otherwise*.

## Constraints
- `1 <= nums.length <= 5000`
- `-1000 <= nums[i] <= 1000`
- `nums[i] != 0`

## Examples
### Example 1
- **Input:** `nums = [2,-1,1,2,2]`
- **Output:** `true`
- **Explanation:** The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).

### Example 2
- **Input:** `nums = [-1,-2,-3,-4,-5,6]`
- **Output:** `false`
- **Explanation:** The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
The only cycle is of size 1, so we return false.

### Example 3
- **Input:** `nums = [1,-1,5,1,4]`
- **Output:** `true`
- **Explanation:** The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has a node jumping forward and a node jumping backward, so

## Key Insight
Leverage **Fast & Slow Pointers** with **Linked List / Pointer** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Circular Array Loop**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [2,-1,1,2,2]`.
2. **Processing Steps:** We apply **Floyd Cycle Detection** using our **Linked List / Pointer**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Linked List / Pointer.

## Pattern
**Fast & Slow Pointers**

## Topics
- Two Pointers
- Cycle Detection

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def get_next(idx: int) -> int:
            return (idx + nums[idx]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            is_forward = nums[i] > 0
            slow = i
            fast = i

            while True:
                next_slow = get_next(slow)
                if nums[next_slow] == 0 or (nums[next_slow] > 0) != is_forward:
                    break
                next_fast = get_next(fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != is_forward:
                    break
                next_fast = get_next(next_fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != is_forward:
                    break

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    if slow == get_next(slow):
                        break
                    return True
            curr = i
            while nums[curr] != 0 and (nums[curr] > 0) == is_forward:
                nxt = get_next(curr)
                nums[curr] = 0
                curr = nxt

        return False
```

## Why This Works
By utilizing **Fast & Slow Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3776. Minimum Moves to Balance Circular Array](../../3501-4000/3776-minimum-moves-to-balance-circular-array/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)
- [33. Search in Rotated Sorted Array](../../0001-0500/0033-search-in-rotated-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/circular-array-loop/)
