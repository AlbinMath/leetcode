# LeetCode 4021: Minimum Operations to Make a Rotated Palindrome I

**LeetCode Problem #4021 — Minimum Operations to Make a Rotated Palindrome I**
Solve LeetCode Minimum Operations to Make a Rotated Palindrome I using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Make a Rotated Palindrome I |
| LeetCode | #4021 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters.

You can perform the following operations any number of times (including zero) and in any order:

**Increment**: Choose any index `i` and replace `s[i]` with the next lowercase English letter. The letter after `'z'` is `'a'`. 
 **Left rotate**: Move the first character of the string to the end.

Return the **minimum** number of operations required to make `s` a palindrome .

## Constraints
- `2 <= s.length <= 2000`
- `s` consists only of lowercase English letters.

## Examples
### Example 1
- **Input:** `s = "abc"`
- **Output:** `2`
- **Explanation:** One optimal solution:

 
 Left rotate the string: `"abc" -> "bca"`. 
 Increment `'a'` to `'b'`: `"bca" -> "bcb"`. 
 `"bcb"` is a palindrome. Thus, the answer is 2.

### Example 2
- **Input:** `s = "yb"`
- **Output:** `3`
- **Explanation:** Increment the first character three times: `"yb" -> "zb" -> "ab" -> "bb"`. 
 `"bb"` is a palindrome. Thus, the answer is 3.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Minimum Operations to Make a Rotated Palindrome I**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "abc"`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One optimal solution:

 
 Left rotate the string: `"abc" -> "bca"`. 
 Increment `'a'` to `'b'`: `"bca" -> "bcb"`. 
 `"bcb"` is a palindrome. Thus, the answer is 2.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        v = [ord(c) - 97 for c in s]
        best = float('inf')
        for r in range(n):
            t = v[r:] + v[:r]
            cost = r
            for i in range(n // 2):
                d = (t[i] - t[n - 1 - i]) % 26
                cost += min(d, 26 - d)
            best = min(best, cost)
        return best
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3766. Minimum Operations to Make Binary Palindrome](../../3501-4000/3766-minimum-operations-to-make-binary-palindrome/)
- [1611. Minimum One Bit Operations to Make Integers Zero](../../1501-2000/1611-minimum-one-bit-operations-to-make-integers-zero/)
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1827-minimum-operations-to-make-the-array-increasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-rotated-palindrome-i/)
