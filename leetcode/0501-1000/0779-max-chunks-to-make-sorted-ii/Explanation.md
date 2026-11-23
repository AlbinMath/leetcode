# LeetCode 768: Max Chunks To Make Sorted II

**LeetCode Problem #768 — Max Chunks To Make Sorted II**
Solve LeetCode Max Chunks To Make Sorted II using Python and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Max Chunks To Make Sorted II |
| LeetCode | #768 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `arr`.

We split `arr` into some number of **chunks** (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return *the largest number of chunks we can make to sort the array*.

## Constraints
- `1 <= arr.length <= 2000`
- `0 <= arr[i] <= 10^8`

## Examples
### Example 1
- **Input:** `arr = [5,4,3,2,1]`
- **Output:** `1`
- **Explanation:** Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

### Example 2
- **Input:** `arr = [2,1,3,4,4]`
- **Output:** `4`
- **Explanation:** We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Max Chunks To Make Sorted II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [5,4,3,2,1]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for x in arr:
            if not stack or x >= stack[-1]:
                stack.append(x)
            else:
                mx = stack.pop()
                while stack and stack[-1] > x:
                    stack.pop()
                stack.append(mx)
        return len(stack)
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [769. Max Chunks To Make Sorted](../../0501-1000/0780-max-chunks-to-make-sorted/)
- [944. Delete Columns to Make Sorted](../../0501-1000/0981-delete-columns-to-make-sorted/)
- [955. Delete Columns to Make Sorted II](../../0501-1000/0992-delete-columns-to-make-sorted-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/max-chunks-to-make-sorted-ii/)
