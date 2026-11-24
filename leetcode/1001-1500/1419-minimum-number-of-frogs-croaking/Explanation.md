# LeetCode 1419: Minimum Number of Frogs Croaking

**LeetCode Problem #1419 — Minimum Number of Frogs Croaking**
Solve LeetCode Minimum Number of Frogs Croaking using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Frogs Croaking |
| LeetCode | #1419 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given the string `croakOfFrogs`, which represents a combination of the string `"croak"` from different frogs, that is, multiple frogs can croak at the same time, so multiple `"croak"` are mixed.

*Return the minimum number of *different* frogs to finish all the croaks in the given string.*

A valid `"croak"` means a frog is printing five letters `'c'`, `'r'`, `'o'`, `'a'`, and `'k'` **sequentially**. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid `"croak"` return `-1`.

## Constraints
- `1 <= croakOfFrogs.length <= 10^5`
- `croakOfFrogs` is either `'c'`, `'r'`, `'o'`, `'a'`, or `'k'`.

## Examples
### Example 1
- **Input:** `croakOfFrogs = "croakcroak"`
- **Output:** `1`
- **Explanation:** One frog yelling "croak

### Example 2
- **Input:** `croakOfFrogs = "crcoakroak"`
- **Output:** `2`
- **Explanation:** The minimum number of frogs is two. 
The first frog could yell "

### Example 3
- **Input:** `croakOfFrogs = "croakcrook"`
- **Output:** `-1`
- **Explanation:** The given string is an invalid combination of "croak

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Frogs Croaking**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `croakOfFrogs = "croakcroak"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** One frog yelling "croak

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        idx = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        stage = [0] * 4  # frogs currently waiting after c, r, o, a
        active = 0       # frogs currently mid-croak
        best = 0

        for ch in croakOfFrogs:
            i = idx[ch]
            if i == 0:
                stage[0] += 1
                active += 1
                best = max(best, active)
            else:
                if stage[i - 1] == 0:
                    return -1
                stage[i - 1] -= 1
                if i < 4:
                    stage[i] += 1
                else:
                    active -= 1

        return best if active == 0 else -1
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)
- [1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix](../../1001-1500/1284-minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-frogs-croaking/)
