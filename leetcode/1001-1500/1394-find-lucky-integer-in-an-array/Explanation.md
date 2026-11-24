# LeetCode 1394: Find Lucky Integer in an Array

**LeetCode Problem #1394 — Find Lucky Integer in an Array**
Solve LeetCode Find Lucky Integer in an Array using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Lucky Integer in an Array |
| LeetCode | #1394 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an array of integers `arr`, a **lucky integer** is an integer that has a frequency in the array equal to its value.

Return *the largest **lucky integer** in the array*. If there is no **lucky integer** return `-1`.

## Constraints
- `1 <= arr.length <= 500`
- `1 <= arr[i] <= 500`

## Examples
### Example 1
- **Input:** `arr = [2,2,3,4]`
- **Output:** `2`
- **Explanation:** The only lucky number in the array is 2 because frequency[2] == 2.

### Example 2
- **Input:** `arr = [1,2,2,3,3,3]`
- **Output:** `3`
- **Explanation:** 1, 2 and 3 are all lucky numbers, return the largest of them.

### Example 3
- **Input:** `arr = [2,2,2,3,3]`
- **Output:** `-1`
- **Explanation:** There are no lucky numbers in the array.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Find Lucky Integer in an Array**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [2,2,3,4]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** The only lucky number in the array is 2 because frequency[2] == 2.

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
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)
        lucky = -1

        for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)

        return lucky
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
- [1985. Find the Kth Largest Integer in the Array](../../1501-2000/1985-find-the-kth-largest-integer-in-the-array/)
- [3132. Find the Integer Added to Array II](../../3001-3500/3132-find-the-integer-added-to-array-ii/)
- [989. Add to Array-Form of Integer](../../0501-1000/0989-add-to-array-form-of-integer/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-lucky-integer-in-an-array/)
