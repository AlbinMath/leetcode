# LeetCode 1460: Make Two Arrays Equal by Reversing Subarrays

**LeetCode Problem #1460 — Make Two Arrays Equal by Reversing Subarrays**
Solve LeetCode Make Two Arrays Equal by Reversing Subarrays using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Make Two Arrays Equal by Reversing Subarrays |
| LeetCode | #1460 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integer arrays of equal length `target` and `arr`. In one step, you can select any **non-empty subarray** of `arr` and reverse it. You are allowed to make any number of steps.

Return `true` *if you can make *`arr`* equal to *`target`* or *`false`* otherwise*.

## Constraints
- `target.length == arr.length`
- `1 <= target.length <= 1000`
- `1 <= target[i] <= 1000`
- `1 <= arr[i] <= 1000`

## Examples
### Example 1
- **Input:** `target = [1,2,3,4], arr = [2,4,1,3]`
- **Output:** `true`
- **Explanation:** You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.

### Example 2
- **Input:** `target = [7], arr = [7]`
- **Output:** `true`
- **Explanation:** arr is equal to target without any reverses.

### Example 3
- **Input:** `target = [3,7,9], arr = [3,7,11]`
- **Output:** `false`
- **Explanation:** arr does not have value 9 and it can never be converted to target.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Make Two Arrays Equal by Reversing Subarrays**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `target = [1,2,3,4], arr = [2,4,1,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
from collections import Counter

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)
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
- [3226. Number of Bit Changes to Make Two Integers Equal](../../3001-3500/3226-number-of-bit-changes-to-make-two-integers-equal/)
- [3377. Digit Operations to Make Two Integers Equal](../../3001-3500/3377-digit-operations-to-make-two-integers-equal/)
- [3505. Minimum Operations to Make Elements Within K Subarrays Equal](../../3501-4000/3505-minimum-operations-to-make-elements-within-k-subarrays-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/)
