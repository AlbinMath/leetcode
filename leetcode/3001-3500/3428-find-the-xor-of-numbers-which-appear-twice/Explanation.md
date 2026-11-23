# LeetCode 3158: Find the XOR of Numbers Which Appear Twice

**LeetCode Problem #3158 — Find the XOR of Numbers Which Appear Twice**
Solve LeetCode Find the XOR of Numbers Which Appear Twice using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the XOR of Numbers Which Appear Twice |
| LeetCode | #3158 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array `nums`, where each number in the array appears **either*** *once* *or* *twice.

Return the bitwise* *`XOR` of all the numbers that appear twice in the array, or 0 if no number appears twice.

## Constraints
- `1 <= nums.length <= 50`
- `1 <= nums[i] <= 50`
- Each number in `nums` appears either once or twice.

## Examples
### Example 1
- **Input:** `nums = [1,2,1,3]`
- **Output:** `1`
- **Explanation:** The only number that appears twice in `nums` is 1.

### Example 2
- **Input:** `nums = [1,2,3]`
- **Output:** `0`
- **Explanation:** No number appears twice in `nums`.

### Example 3
- **Input:** `nums = [1,2,2,1]`
- **Output:** `3`
- **Explanation:** Numbers 1 and 2 appeared twice. `1 XOR 2 == 3`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find the XOR of Numbers Which Appear Twice**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,1,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** The only number that appears twice in `nums` is 1.

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

class Solution(object):
    def duplicateNumbersXOR(self, nums):
        res = 0
        for v, c in Counter(nums).items():
            if c == 2:
                res ^= v
        return res
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
- [3233. Find the Count of Numbers Which Are Not Special](../../3501-4000/3507-find-the-count-of-numbers-which-are-not-special/)
- [421. Maximum XOR of Two Numbers in an Array](../../0001-0500/0421-maximum-xor-of-two-numbers-in-an-array/)
- [1738. Find Kth Largest XOR Coordinate Value](../../1501-2000/1860-find-kth-largest-xor-coordinate-value/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/)
