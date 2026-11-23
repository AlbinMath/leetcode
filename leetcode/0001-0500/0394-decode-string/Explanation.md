# LeetCode 394: Decode String

**LeetCode Problem #394 — Decode String**
Solve LeetCode Decode String using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Decode String |
| LeetCode | #394 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed `10^5`.

## Constraints
- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be **a valid** input.
- All the integers in `s` are in the range `[1, 300]`.

## Examples
### Example 1
- **Input:** `s = "3[a]2[bc]"`
- **Output:** `"aaabcbc"`

### Example 2
- **Input:** `s = "3[a2[c]]"`
- **Output:** `"accaccacc"`

### Example 3
- **Input:** `s = "2[abc]3[cd]ef"`
- **Output:** `"abcabccdcdcdef"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Decode String**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "3[a]2[bc]"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"aaabcbc"`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var decodeString = function(s) {
    const stack = [];
    let currentNum = 0;
    let currentStr = "";

    for (const char of s) {
        if (char >= '0' && char <= '9') {
            // Build the repetition number
            currentNum = currentNum * 10 + Number(char);
        } else if (char === '[') {
            // Save the current state before entering brackets
            stack.push([currentStr, currentNum]);
            currentStr = "";
            currentNum = 0;
        } else if (char === ']') {
            // Restore the previous state and repeat the inner string
            const [previousStr, repeatCount] = stack.pop();
            currentStr = previousStr + currentStr.repeat(repeatCount);
        } else {
            // Append ordinary letters
            currentStr += char;
        }
    }

    return currentStr;
};
```

### Python
```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((cur, num))
                cur, num = "", 0
            elif c == ']':
                prev, k = stack.pop()
                cur = prev + cur * k
            else:
                cur += c

        return cur
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)
- [28. Find the Index of the First Occurrence in a String](../../0001-0500/0028-find-the-index-of-the-first-occurrence-in-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/decode-string/)
