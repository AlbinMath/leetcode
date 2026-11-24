# LeetCode 405: Convert a Number to Hexadecimal

**LeetCode Problem #405 — Convert a Number to Hexadecimal**
Solve LeetCode Convert a Number to Hexadecimal using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Convert a Number to Hexadecimal |
| LeetCode | #405 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a 32-bit integer `num`, return *a string representing its hexadecimal representation*. For negative integers, two&rsquo;s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

**Note: **You are not allowed to use any built-in library method to directly solve this problem.

## Constraints
- `-2^31 <= num <= 2^31 - 1`

## Examples
### Example 1
- **Input:** `num = 26`
- **Output:** `"1a"`

### Example 2
- **Input:** `num = -1`
- **Output:** `"ffffffff"`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Convert a Number to Hexadecimal**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 26`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"1a"`.

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
    def toHex(self, num):
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"

        # Convert negative number to 32-bit two's complement
        if num < 0:
            num = num & 0xFFFFFFFF

        result = ""

        while num > 0:
            digit = num & 15
            result = hex_chars[digit] + result
            num >>= 4

        return result
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
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)
- [1290. Convert Binary Number in a Linked List to Integer](../../1001-1500/1290-convert-binary-number-in-a-linked-list-to-integer/)
- [2059. Minimum Operations to Convert Number](../../2001-2500/2059-minimum-operations-to-convert-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/convert-a-number-to-hexadecimal/)
