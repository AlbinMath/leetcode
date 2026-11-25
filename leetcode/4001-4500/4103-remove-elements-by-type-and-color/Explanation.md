# LeetCode 4103: Remove Elements by Type and Color

**LeetCode Problem #4103 — Remove Elements by Type and Color**
Solve LeetCode Remove Elements by Type and Color using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Remove Elements by Type and Color |
| LeetCode | #4103 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given three integer arrays `types`, `colors`, and `groupSize`, where `types` and `colors` have length `n`, and `groupSize` has length `m`.

`types[i]` represents the type of the element at index `i`. 
 `colors[i]` represents the color of the element at index `i`. 
 `groupSize[t]` represents the required number of elements in a removable group of type `t`.

In one operation, you may remove **exactly** `groupSize[t]` **consecutive** elements if all of them have type `t` and the **same color**.

After each removal, the remaining elements become **adjacent** again while maintaining their relative order.

Return `true` if it is possible to remove all elements using a sequence of valid operations. Otherwise, return `false`.

## Constraints
- `1 <= n == types.length == colors.length <= 10^5`
- `1 <= m == groupSize.length <= 10^5`
- `0 <= types[i] <= m - 1`
- `1 <= colors[i] <= 10^5`
- `1 <= groupSize[t] <= n`

## Examples
### Example 1
- **Input:** `types = [0,1,1,0], colors = [5,3,3,5] , groupSize = [2,2]`
- **Output:** `true`
- **Explanation:** First, remove the consecutive elements at indices 1 and 2. Both elements have type 1, color 3, and the group size is equal to `groupSize[1] = 2`. 
 The remaining sequence is: `types = [0, 0]`, `colors = [5, 5]` 
 Now remove the two remaining elements. They have type 0, color 5, and the group size is equal to `groupSize[0] = 2`. 
 All elements have been removed, so the answer is `true`.

### Example 2
- **Input:** `types = [0,1,0], colors = [9,9,9], groupSize = [3,2]`
- **Output:** `false`
- **Explanation:** No valid operation can be performed because no consecutive group satisfies its required size. 
 Therefore, it is impossible to remove all elements, so the answer is `false`.

### Example 3
- **Input:** `types = [2,0,1,2], colors = [7,5,4,7], groupSize = [3,1,2]`
- **Output:** `false`
- **Explanation:** ​​​​​​​ 

 
 Remove the element at index 2. It has type 1, color 4, and forms a consecutive group of size `groupSize[1] = 1`. 
 The remaining sequence is: `types = [2, 0, 2]`, `colors = [7, 5, 7]`. 
 No further operations can be performed, so the answer is `false`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Remove Elements by Type and Color**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `types = [0,1,1,0], colors = [5,3,3,5] , groupSize = [2,2]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** First, remove the consecutive elements at indices 1 and 2. Both elements have type 1, color 3, and the group size is equal to `groupSize[1] = 2`. 
 The remaining sequence is: `types = [0, 0]`, `colors = [5, 5]` 
 Now remove the two remaining elements. They have type 0, color 5, and the group size is equal to `groupSize[0] = 2`. 
 All elements have been removed, so the answer is `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def canRemoveAll(self, types: List[int], colors: List[int], groupSize: List[int]) -> bool:
        stk = []  # list of [type, color, count]
        
        for t, c in zip(types, colors):
            if stk and stk[-1][0] == t and stk[-1][1] == c:
                stk[-1][2] += 1
            else:
                stk.append([t, c, 1])
                
            if stk[-1][2] == groupSize[t]:
                stk.pop()
                
        return not stk
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2038. Remove Colored Pieces if Both Neighbors are the Same Color](../../2001-2500/2038-remove-colored-pieces-if-both-neighbors-are-the-same-color/)
- [203. Remove Linked List Elements](../../0001-0500/0203-remove-linked-list-elements/)
- [1320. Minimum Distance to Type a Word Using Two Fingers](../../1001-1500/1320-minimum-distance-to-type-a-word-using-two-fingers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/remove-elements-by-type-and-color/)
