# LeetCode 504: Base 7

**LeetCode Problem #504 — Base 7**
Solve LeetCode Base 7 using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Base 7 |
| LeetCode | #504 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer `num`, return *a string of its **base 7** representation*.

## Constraints
- `-10^7 <= num <= 10^7`

## Examples
### Example 1
- **Input:** `num = 100`
- **Output:** `"202"`

### Example 2
- **Input:** `num = -7`
- **Output:** `"-10"`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Base 7**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = 100`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"202"`.

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
    def convertToBase7(self, num):
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)

        digits = []

        while num > 0:
            digits.append(str(num % 7))
            num //= 7

        result = ''.join(reversed(digits))

        if negative:
            result = '-' + result

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
- [483. Smallest Good Base](../../0001-0500/0483-smallest-good-base/)
- [1009. Complement of Base 10 Integer](../../1001-1500/1009-complement-of-base-10-integer/)
- [1017. Convert to Base -2](../../1001-1500/1017-convert-to-base-2/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/base-7/)
