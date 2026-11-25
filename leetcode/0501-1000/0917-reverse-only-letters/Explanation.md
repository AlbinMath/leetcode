# LeetCode 917: Reverse Only Letters

**LeetCode Problem #917 — Reverse Only Letters**
Solve LeetCode Reverse Only Letters using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Only Letters |
| LeetCode | #917 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string `s`, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position. 
 All the English letters (lowercase or uppercase) should be reversed.

Return `s`* after reversing it*.

## Constraints
- `1 <= s.length <= 100`
- `s` consists of characters with ASCII values in the range `[33, 122]`.
- `s` does not contain `'\"'` or `'\\'`.

## Examples
### Example 1
- **Input:** `s = "ab-cd"`
- **Output:** `"dc-ba"`

### Example 2
- **Input:** `s = "a-bC-dEf-ghIj"`
- **Output:** `"j-Ih-gfE-dCba"`

### Example 3
- **Input:** `s = "Test1ng-Leet=code-Q!"`
- **Output:** `"Qedo1ct-eeLg=ntse-T!"`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Reverse Only Letters**, we observe the problem requirements and utilize the **Two Pointers** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "ab-cd"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"dc-ba"`.

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
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        left = 0
        right = len(chars) - 1

        while left < right:
            if not chars[left].isalpha():
                left += 1
            elif not chars[right].isalpha():
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return ''.join(chars)
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
- [3823. Reverse Letters Then Special Characters in a String](../../3501-4000/3823-reverse-letters-then-special-characters-in-a-string/)
- [7. Reverse Integer](../../0001-0500/0007-reverse-integer/)
- [25. Reverse Nodes in k-Group](../../0001-0500/0025-reverse-nodes-in-k-group/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-only-letters/)
