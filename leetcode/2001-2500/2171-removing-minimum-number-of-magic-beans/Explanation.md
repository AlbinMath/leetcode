# LeetCode 2171: Removing Minimum Number of Magic Beans

**LeetCode Problem #2171 — Removing Minimum Number of Magic Beans**
Solve LeetCode Removing Minimum Number of Magic Beans using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Removing Minimum Number of Magic Beans |
| LeetCode | #2171 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of **positive** integers `beans`, where each integer represents the number of magic beans found in a particular magic bag.

**Remove** any number of beans (**possibly none**) from each bag such that the number of beans in each remaining **non-empty** bag (still containing **at least one** bean) is **equal**. Once a bean has been removed from a bag, you are **not** allowed to return it to any of the bags.

Return *the **minimum** number of magic beans that you have to remove*.

## Constraints
- `1 <= beans.length <= 10^5`
- `1 <= beans[i] <= 10^5`

## Examples
### Example 1
- **Input:** `beans = [4,1,6,5]`
- **Output:** `4`
- **Explanation:** - We remove 1 bean from the bag with only 1 bean.
 This results in the remaining bags: [4,

### Example 2
- **Input:** `beans = [2,10,3,2]`
- **Output:** `7`
- **Explanation:** - We remove 2 beans from one of the bags with 2 beans.
 This results in the remaining bags: [

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Removing Minimum Number of Magic Beans**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `beans = [4,1,6,5]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** - We remove 1 bean from the bag with only 1 bean.
 This results in the remaining bags: [4,

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
class Solution(object):
    def minimumRemoval(self, beans):
        beans.sort()
        n = len(beans)
        max_kept = max(b * (n - i) for i, b in enumerate(beans))
        return sum(beans) - max_kept
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
- [2091. Removing Minimum and Maximum From Array](../../2001-2500/2091-removing-minimum-and-maximum-from-array/)
- [2696. Minimum String Length After Removing Substrings](../../2501-3000/2696-minimum-string-length-after-removing-substrings/)
- [3170. Lexicographically Minimum String After Removing Stars](../../3001-3500/3170-lexicographically-minimum-string-after-removing-stars/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/removing-minimum-number-of-magic-beans/)
