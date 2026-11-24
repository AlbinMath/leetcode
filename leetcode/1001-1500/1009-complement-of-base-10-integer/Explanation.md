# LeetCode 1009: Complement of Base 10 Integer

**LeetCode Problem #1009 — Complement of Base 10 Integer**
Solve LeetCode Complement of Base 10 Integer using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Complement of Base 10 Integer |
| LeetCode | #1009 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

For example, The integer `5` is `"101"` in binary and its **complement** is `"010"` which is the integer `2`.

Given an integer `n`, return *its complement*.

## Constraints
- `0 <= n < 10^9`

## Examples
### Example 1
- **Input:** `n = 5`
- **Output:** `2`
- **Explanation:** 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

### Example 2
- **Input:** `n = 7`
- **Output:** `0`
- **Explanation:** 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

### Example 3
- **Input:** `n = 10`
- **Output:** `5`
- **Explanation:** 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Complement of Base 10 Integer**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 5`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

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
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        mask = (1 << n.bit_length()) - 1

        return n ^ mask
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
- [476. Number Complement](../../0001-0500/0476-number-complement/)
- [483. Smallest Good Base](../../0001-0500/0483-smallest-good-base/)
- [504. Base 7](../../0501-1000/0504-base-7/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/complement-of-base-10-integer/)
