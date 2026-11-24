# LeetCode 744: Find Smallest Letter Greater Than Target

**LeetCode Problem #744 — Find Smallest Letter Greater Than Target**
Solve LeetCode Find Smallest Letter Greater Than Target using Python and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Smallest Letter Greater Than Target |
| LeetCode | #744 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an array of characters `letters` that is sorted in **non-decreasing order**, and a character `target`. There are **at least two different** characters in `letters`.

Return *the smallest character in *`letters`* that is lexicographically greater than *`target`. If such a character does not exist, return the first character in `letters`.

## Constraints
- `2 <= letters.length <= 10^4`
- `letters[i]` is a lowercase English letter.
- `letters` is sorted in **non-decreasing** order.
- `letters` contains at least two different characters.
- `target` is a lowercase English letter.

## Examples
### Example 1
- **Input:** `letters = ["c","f","j"], target = "a"`
- **Output:** `"c"`
- **Explanation:** The smallest character that is lexicographically greater than 'a' in letters is 'c'.

### Example 2
- **Input:** `letters = ["c","f","j"], target = "c"`
- **Output:** `"f"`
- **Explanation:** The smallest character that is lexicographically greater than 'c' in letters is 'f'.

### Example 3
- **Input:** `letters = ["x","x","y","y"], target = "z"`
- **Output:** `"x"`
- **Explanation:** There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Smallest Letter Greater Than Target**, we observe the problem requirements and utilize the **Prefix Sum** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `letters = ["c","f","j"], target = "a"`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"c"`.
4. **Verification:** The smallest character that is lexicographically greater than 'a' in letters is 'c'.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters)

        while left < right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left % len(letters)]
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3720. Lexicographically Smallest Permutation Greater Than Target](../../3501-4000/3720-lexicographically-smallest-permutation-greater-than-target/)
- [3734. Lexicographically Smallest Palindromic Permutation Greater Than Target](../../3501-4000/3734-lexicographically-smallest-palindromic-permutation-greater-than-target/)
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../../2501-3000/2996-smallest-missing-integer-greater-than-sequential-prefix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
