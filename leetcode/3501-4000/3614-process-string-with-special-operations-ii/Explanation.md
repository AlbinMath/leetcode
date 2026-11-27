# LeetCode 3614: Process String with Special Operations II

**LeetCode Problem #3614 — Process String with Special Operations II**
Solve LeetCode Process String with Special Operations II using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Process String with Special Operations II |
| LeetCode | #3614 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` consisting of lowercase English letters and the special characters: `'*'`, `'#'`, and `'%'`.

You are also given an integer `k`.

Build a new string `result` by processing `s` according to the following rules from left to right:

If the letter is a **lowercase** English letter append it to `result`. 
 A `'*'` **removes** the last character from `result`, if it exists. 
 A `'#'` **duplicates** the current `result` and **appends** it to itself. 
 A `'%'` **reverses** the current `result`.

Return the `k^th` character of the final string `result`. If `k` is out of the bounds of `result`, return `'.'`.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters and special characters `'*'`, `'#'`, and `'%'`.
- `0 <= k <= 10^15`
- The length of `result` after processing `s` will not exceed `10^15`.

## Examples
### Example 1
- **Input:** `s = "a#b%*", k = 1`
- **Output:** `"a"`
- **Explanation:** `i` 
 `s[i]` 
 Operation 
 Current `result` 
 
 
 
 
 0 
 `'a'` 
 Append `'a'` 
 `"a"` 
 
 
 1 
 `'#'` 
 Duplicate `result` 
 `"aa"` 
 
 
 2 
 `'b'` 
 Append `'b'` 
 `"aab"` 
 
 
 3 
 `'%'` 
 Reverse `result` 
 `"baa"` 
 
 
 4 
 `'*'` 
 Remove the last character 
 `"ba"` 
 
 
 

 The final `result` is `"ba"`. The character at index `k = 1` is `'a'`.

### Example 2
- **Input:** `s = "cd%#*#", k = 3`
- **Output:** `"d"`
- **Explanation:** `i` 
 `s[i]` 
 Operation 
 Current `result` 
 
 
 
 
 0 
 `'c'` 
 Append `'c'` 
 `"c"` 
 
 
 1 
 `'d'` 
 Append `'d'` 
 `"cd"` 
 
 
 2 
 `'%'` 
 Reverse `result` 
 `"dc"` 
 
 
 3 
 `'#'` 
 Duplicate `result` 
 `"dcdc"` 
 
 
 4 
 `'*'` 
 Remove the last character 
 `"dcd"` 
 
 
 5 
 `'#'` 
 Duplicate `result` 
 `"dcddcd"` 
 
 
 

 The final `result` is `"dcddcd"`. The character at index `k = 3` is `'d'`.

### Example 3
- **Input:** `s = "z*#", k = 0`
- **Output:** `"."`
- **Explanation:** `i` 
 `s[i]` 
 Operation 
 Current `result` 
 
 
 
 
 0 
 `'z'` 
 Append `'z'` 
 `"z"` 
 
 
 1 
 `'*'` 
 Remove the last character 
 `""` 
 
 
 2 
 `'#'` 
 Duplicate the string 
 `""` 
 
 
 

 The final `result` is `""`. Since index `k = 0` is out of bounds, the output is `'.'`.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Process String with Special Operations II**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "a#b%*", k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"a"`.
4. **Verification:** `i` 
 `s[i]` 
 Operation 
 Current `result` 
 
 
 
 
 0 
 `'a'` 
 Append `'a'` 
 `"a"` 
 
 
 1 
 `'#'` 
 Duplicate `result` 
 `"aa"` 
 
 
 2 
 `'b'` 
 Append `'b'` 
 `"aab"` 
 
 
 3 
 `'%'` 
 Reverse `result` 
 `"baa"` 
 
 
 4 
 `'*'` 
 Remove the last character 
 `"ba"` 
 
 
 

 The final `result` is `"ba"`. The character at index `k = 1` is `'a'`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:

    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        # length[i] = length of result after processing s[0:i]
        length = [0] * (n + 1)

        for i, ch in enumerate(s):
            cur = length[i]

            if 'a' <= ch <= 'z':
                cur += 1

            elif ch == '*':
                if cur > 0:
                    cur -= 1

            elif ch == '#':
                cur *= 2

            elif ch == '%':
                # Reversing does not change length.
                pass

            length[i + 1] = cur

        # k is outside the final string.
        if k >= length[n]:
            return "."

        # Work backwards.
        for i in range(n - 1, -1, -1):
            ch = s[i]

            prev_len = length[i]
            cur_len = length[i + 1]

            # A normal character was appended.
            if 'a' <= ch <= 'z':
                # The appended character occupies the last position.
                if k == cur_len - 1:
                    return ch

                # Otherwise k belongs to the previous string.
                continue

            # '*' removed the last character.
            elif ch == '*':
                # The remaining characters keep the same indices.
                continue

            # '#' duplicated the string:
            #
            #   result = old + old
            #
            # Map an index from the second copy back to the first.
            elif ch == '#':
                if prev_len > 0:
                    k %= prev_len

            # '%' reversed the string.
            elif ch == '%':
                k = prev_len - 1 - k

        return "."
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [3612. Process String with Special Operations I](../../3501-4000/3612-process-string-with-special-operations-i/)
- [1585. Check If String Is Transformable With Substring Sort Operations](../../1501-2000/1585-check-if-string-is-transformable-with-substring-sort-operations/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1625-lexicographically-smallest-string-after-applying-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-ii/)
