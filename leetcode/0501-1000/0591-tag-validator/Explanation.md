# LeetCode 591: Tag Validator

**LeetCode Problem #591 — Tag Validator**
Solve LeetCode Tag Validator using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Tag Validator |
| LeetCode | #591 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.

A code snippet is valid if all the following rules hold:

The code must be wrapped in a valid closed tag . Otherwise, the code is invalid. 
 A closed tag (not necessarily valid) has exactly the following format : `<TAG_NAME>TAG_CONTENT</TAG_NAME>`. Among them, `<TAG_NAME>` is the start tag, and `</TAG_NAME>` is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid. 
 A valid `TAG_NAME` only contain upper-case letters , and has length in range [1,9]. Otherwise, the `TAG_NAME` is invalid . 
 A valid `TAG_CONTENT` may contain other valid closed tags , cdata and any characters (see note1) EXCEPT unmatched `<`, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the `TAG_CONTENT` is invalid . 
 A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested. 
 A `<` is unmatched if you cannot find a subsequent `>`. And when you find a `<` or `</`, all the subsequent characters until the next `>` should be parsed as TAG_NAME (not necessarily valid). 
 The cdata has the following format : `<![CDATA[CDATA_CONTENT]]>`. The range of `CDATA_CONTENT` is defined as the characters between `<![CDATA[` and the first subsequent `]]>`. 
 `CDATA_CONTENT` may contain any characters . The function of cdata is to forbid the validator to parse `CDATA_CONTENT`, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters .

## Constraints
- `1 <= code.length <= 500`
- `code` consists of English letters, digits, `'<'`, `'>'`, `'/'`, `'!'`, `'['`, `']'`, `'.'`, and `' '`.

## Examples
### Example 1
- **Input:** `code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"`
- **Output:** `true`
- **Explanation:** The code is wrapped in a closed tag : <DIV> and </DIV>. 
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 
Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag.
So TAG_CONTENT is valid, and then the code is valid. Thus return true.

### Example 2
- **Input:** `code = "<DIV>>> ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"`
- **Output:** `true`
- **Explanation:** We first separate the code into : start_tag|tag_content|end_tag.
start_tag -> "<DIV>" 
end_tag -> "</DIV>" 
tag_content could also be separated into : text1|cdata|text2.
text1 -> ">> ![cdata[]] " 
cdata -> "<![CDATA[<div>]>]]>" , where the CDATA_CONTENT is "<div>]>" 
text2 -> "]]>>]" 
The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.

### Example 3
- **Input:** `code = "<A> <B> </A> </B>"`
- **Output:** `false`
- **Explanation:** Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Tag Validator**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The code is wrapped in a closed tag : <DIV> and </DIV>. 
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 
Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag.
So TAG_CONTENT is valid, and then the code is valid. Thus return true.

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
    def isValid(self, code: str) -> bool:
        stack = []
        i, n = 0, len(code)

        while i < n:
            if i > 0 and not stack:
                return False

            if code.startswith("<![CDATA[", i):
                j = code.find("]]>", i + 9)
                if j == -1 or not stack:
                    return False
                i = j + 3

            elif code.startswith("</", i):
                j = code.find(">", i)
                if j == -1:
                    return False
                tag = code[i + 2:j]
                if not stack or stack.pop() != tag:
                    return False
                i = j + 1

            elif code[i] == "<":
                j = code.find(">", i)
                if j == -1:
                    return False
                tag = code[i + 1:j]
                if not 1 <= len(tag) <= 9 or not tag.isupper() or not tag.isalpha():
                    return False
                stack.append(tag)
                i = j + 1

            else:
                i += 1

        return not stack
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
- [3582. Generate Tag for Video Caption](../../3501-4000/3582-generate-tag-for-video-caption/)
- [3921. Score Validator](../../3501-4000/3921-score-validator/)
- [2. Add Two Numbers](../../0001-0500/0002-add-two-numbers/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/tag-validator/)
