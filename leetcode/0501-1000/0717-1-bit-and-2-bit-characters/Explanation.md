# LeetCode 717: 1-bit and 2-bit Characters

**LeetCode Problem #717 — 1-bit and 2-bit Characters**
Solve LeetCode 1-bit and 2-bit Characters using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | 1-bit and 2-bit Characters |
| LeetCode | #717 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
We have two special characters:

The first character can be represented by one bit `0`. 
 The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

## Constraints
- `1 <= bits.length <= 1000`
- `bits[i]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `bits = [1,0,0]`
- **Output:** `true`
- **Explanation:** The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

### Example 2
- **Input:** `bits = [1,1,1,0]`
- **Output:** `false`
- **Explanation:** The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **1-bit and 2-bit Characters**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `bits = [1,0,0]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

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
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i = 0

        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return i == len(bits) - 1
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
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)
- [451. Sort Characters By Frequency](../../0001-0500/0451-sort-characters-by-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/1-bit-and-2-bit-characters/)
