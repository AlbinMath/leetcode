# LeetCode 166: Fraction to Recurring Decimal

**LeetCode Problem #166 — Fraction to Recurring Decimal**
Solve LeetCode Fraction to Recurring Decimal using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fraction to Recurring Decimal |
| LeetCode | #166 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given two integers representing the `numerator` and `denominator` of a fraction, return *the fraction in string format*.

If the fractional part is repeating, enclose the repeating part in parentheses

If multiple answers are possible, return **any of them**.

It is **guaranteed** that the length of the answer string is less than `10^4` for all the given inputs.

**Note** that if the fraction can be represented as a *finite length string*, you **must** return it.

## Constraints
- `-2^31 <= numerator, denominator <= 2^31 - 1`
- `denominator != 0`

## Examples
### Example 1
- **Input:** `numerator = 1, denominator = 2`
- **Output:** `"0.5"`

### Example 2
- **Input:** `numerator = 2, denominator = 1`
- **Output:** `"2"`

### Example 3
- **Input:** `numerator = 4, denominator = 333`
- **Output:** `"0.(012)"`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Fraction to Recurring Decimal**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `numerator = 1, denominator = 2`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"0.5"`.

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
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if (numerator < 0) != (denominator < 0):
            res.append('-')

        num, den = abs(numerator), abs(denominator)
        res.append(str(num // den))
        rem = num % den
        if rem == 0:
            return ''.join(res)

        res.append('.')
        seen = {}  # remainder -> index in res where its digit goes

        while rem:
            if rem in seen:
                res.insert(seen[rem], '(')
                res.append(')')
                break
            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den

        return ''.join(res)
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
- [592. Fraction Addition and Subtraction](../../0501-1000/0592-fraction-addition-and-subtraction/)
- [1. Two Sum](../../0001-0500/0001-two-sum/)
- [49. Group Anagrams](../../0001-0500/0049-group-anagrams/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fraction-to-recurring-decimal/)
