# LeetCode 3582: Generate Tag for Video Caption

**LeetCode Problem #3582 — Generate Tag for Video Caption**
Solve LeetCode Generate Tag for Video Caption using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Generate Tag for Video Caption |
| LeetCode | #3582 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string ` caption ` representing the caption for a video.

The following actions must be performed **in order** to generate a **valid tag** for the video:

**Combine all words** in the string into a single *camelCase string* prefixed with `'#'`. A *camelCase string* is one where the first letter of all words *except* the first one is capitalized. All characters after the first character in **each** word must be lowercase.

Remove all characters that are not an English letter, **except** the first `'#'`.

**Truncate** the result to a maximum of 100 characters.

Return the **tag** after performing the actions on `caption`.

## Constraints
- `1 <= caption.length <= 150`
- `caption` consists only of English letters and `' '`.

## Examples
### Example 1
- **Input:** `caption = "Leetcode daily streak achieved"`
- **Output:** `"#leetcodeDailyStreakAchieved"`
- **Explanation:** The first letter for all words except `"leetcode"` should be capitalized.

### Example 2
- **Input:** `caption = "can I Go There"`
- **Output:** `"#canIGoThere"`
- **Explanation:** The first letter for all words except `"can"` should be capitalized.

### Example 3
- **Input:** `caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"`
- **Output:** `"#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"`
- **Explanation:** Since the first word has length 101, we need to truncate the last two letters from the word.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Generate Tag for Video Caption**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `caption = "Leetcode daily streak achieved"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"#leetcodeDailyStreakAchieved"`.
4. **Verification:** The first letter for all words except `"leetcode"` should be capitalized.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        out = []
        for i, w in enumerate(words):
            w = w.lower()
            if i > 0:
                w = w.capitalize()
            out.append(w)
        s = "".join(c for c in "".join(out) if c.isalpha())
        return ("#" + s)[:100]
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [591. Tag Validator](../../0501-1000/0591-tag-validator/)
- [1024. Video Stitching](../../1001-1500/1024-video-stitching/)
- [2456. Most Popular Video Creator](../../2001-2500/2456-most-popular-video-creator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/generate-tag-for-video-caption/)
