# LeetCode 1338: Reduce Array Size to The Half

**LeetCode Problem #1338 — Reduce Array Size to The Half**
Solve LeetCode Reduce Array Size to The Half using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reduce Array Size to The Half |
| LeetCode | #1338 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `arr`. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return *the minimum size of the set so that **at least** half of the integers of the array are removed*.

## Constraints
- `2 <= arr.length <= 10^5`
- `arr.length` is even.
- `1 <= arr[i] <= 10^5`

## Examples
### Example 1
- **Input:** `arr = [3,3,3,3,5,5,5,2,2,7]`
- **Output:** `2`
- **Explanation:** Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

### Example 2
- **Input:** `arr = [7,7,7,7,7,7]`
- **Output:** `1`
- **Explanation:** The only possible set you can choose is {7}. This will make the new array empty.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Reduce Array Size to The Half**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [3,3,3,3,5,5,5,2,2,7]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

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
from collections import Counter
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) // 2
        frequencies = sorted(Counter(arr).values(), reverse=True)
        
        removed = 0
        for set_size, freq in enumerate(frequencies, start=1):
            removed += freq
            if removed >= half:
                return set_size
                
        return 0
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
- [2626. Array Reduce Transformation](../../2501-3000/2626-array-reduce-transformation/)
- [3824. Minimum K to Reduce Array Within Limit](../../3501-4000/3824-minimum-k-to-reduce-array-within-limit/)
- [961. N-Repeated Element in Size 2N Array](../../0501-1000/0961-n-repeated-element-in-size-2n-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reduce-array-size-to-the-half/)
