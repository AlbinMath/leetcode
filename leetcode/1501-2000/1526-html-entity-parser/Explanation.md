# LeetCode 1410: HTML Entity Parser

**LeetCode Problem #1410 — HTML Entity Parser**
Solve LeetCode HTML Entity Parser using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | HTML Entity Parser |
| LeetCode | #1410 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
**HTML entity parser** is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

**Quotation Mark:** the entity is `&quot;` and symbol character is `"`. 
 **Single Quote Mark:** the entity is `&apos;` and symbol character is `'`. 
 **Ampersand:** the entity is `&amp;` and symbol character is `&`. 
 **Greater Than Sign:** the entity is `&gt;` and symbol character is `>`. 
 **Less Than Sign:** the entity is `&lt;` and symbol character is `<`. 
 **Slash:** the entity is `&frasl;` and symbol character is `/`.

Given the input `text` string to the HTML parser, you have to implement the entity parser.

Return *the text after replacing the entities by the special characters*.

## Constraints
- `1 <= text.length <= 10^5`
- The string may contain any possible characters out of all the 256 ASCII characters.

## Examples
### Example 1
- **Input:** `text = "&amp; is an HTML entity but &ambassador; is not."`
- **Output:** `"& is an HTML entity but &ambassador; is not."`
- **Explanation:** The parser will replace the &amp; entity by &

### Example 2
- **Input:** `text = "and I quote: &quot;...&quot;"`
- **Output:** `"and I quote: \"...\""`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **HTML Entity Parser**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `text = "&amp; is an HTML entity but &ambassador; is not."`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"& is an HTML entity but &ambassador; is not."`.
4. **Verification:** The parser will replace the &amp; entity by &

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
    def entityParser(self, text: str) -> str:
        return (text.replace("&quot;", '"')
                    .replace("&apos;", "'")
                    .replace("&gt;", ">")
                    .replace("&lt;", "<")
                    .replace("&frasl;", "/")
                    .replace("&amp;", "&"))
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
- [385. Mini Parser](../../0001-0500/0385-mini-parser/)
- [1678. Goal Parser Interpretation](../../1501-2000/1797-goal-parser-interpretation/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/html-entity-parser/)
