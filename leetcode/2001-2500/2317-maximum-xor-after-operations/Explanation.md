# LeetCode 2317: Maximum XOR After Operations 

**LeetCode Problem #2317 — Maximum XOR After Operations **
Solve LeetCode Maximum XOR After Operations  using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum XOR After Operations  |
| LeetCode | #2317 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a **0-indexed** integer array `nums`. In one operation, select **any** non-negative integer `x` and an index `i`, then **update** `nums[i]` to be equal to `nums[i] AND (nums[i] XOR x)`.

Note that `AND` is the bitwise AND operation and `XOR` is the bitwise XOR operation.

Return *the **maximum** possible bitwise XOR of all elements of *`nums`* after applying the operation **any number** of times*.

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^8`

## Examples
### Example 1
- **Input:** `nums = [3,2,4,6]`
- **Output:** `7`
- **Explanation:** Apply the operation with x = 4 and i = 3, num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2.
Now, nums = [3, 2, 4, 2] and the bitwise XOR of all the elements = 3 XOR 2 XOR 4 XOR 2 = 7.
It can be shown that 7 is the maximum possible bitwise XOR.
Note that other operations may be used to achieve a bitwise XOR of 7.

### Example 2
- **Input:** `nums = [1,2,3,9,2]`
- **Output:** `11`
- **Explanation:** Apply the operation zero times.
The bitwise XOR of all the elements = 1 XOR 2 XOR 3 XOR 9 XOR 2 = 11.
It can be shown that 11 is the maximum possible bitwise XOR.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum XOR After Operations **, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [3,2,4,6]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `7`.
4. **Verification:** Apply the operation with x = 4 and i = 3, num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2.
Now, nums = [3, 2, 4, 2] and the bitwise XOR of all the elements = 3 XOR 2 XOR 4 XOR 2 = 7.
It can be shown that 7 is the maximum possible bitwise XOR.
Note that other operations may be used to achieve a bitwise XOR of 7.

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
from functools import reduce
import operator
from typing import List


class Solution:

  def maximumXOR(self, nums: List[int]) -> int:
    return reduce(operator.or_, nums, 0)
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
- [3849. Maximum Bitwise XOR After Rearrangement](../../3501-4000/3849-maximum-bitwise-xor-after-rearrangement/)
- [3035. Maximum Palindromes After Operations](../../3001-3500/3035-maximum-palindromes-after-operations/)
- [3346. Maximum Frequency of an Element After Performing Operations I](../../3001-3500/3346-maximum-frequency-of-an-element-after-performing-operations-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-xor-after-operations/)
