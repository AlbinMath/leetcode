# LeetCode 806: Number of Lines To Write String

**LeetCode Problem #806 — Number of Lines To Write String**
Solve LeetCode Number of Lines To Write String using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Lines To Write String |
| LeetCode | #806 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of lowercase English letters and an array `widths` denoting **how many pixels wide** each lowercase English letter is. Specifically, `widths[0]` is the width of `'a'`, `widths[1]` is the width of `'b'`, and so on.

You are trying to write `s` across several lines, where **each line is no longer than **`100`** pixels**. Starting at the beginning of `s`, write as many letters on the first line such that the total width does not exceed `100` pixels. Then, from where you stopped in `s`, continue writing as many letters as you can on the second line. Continue this process until you have written all of `s`.

Return *an array *`result`* of length 2 where:*

`result[0]`* is the total number of lines.* 
 `result[1]`* is the width of the last line in pixels.*

## Constraints
- `widths.length == 26`
- `2 <= widths[i] <= 10`
- `1 <= s.length <= 1000`
- `s` contains only lowercase English letters.

## Examples
### Example 1
- **Input:** `widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"`
- **Output:** `[3,60]`
- **Explanation:** You can write s as follows:
abcdefghij // 100 pixels wide
klmnopqrst // 100 pixels wide
uvwxyz // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.

### Example 2
- **Input:** `widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"`
- **Output:** `[2,4]`
- **Explanation:** You can write s as follows:
bbbcccdddaa // 98 pixels wide
a // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Number of Lines To Write String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,60]`.
4. **Verification:** You can write s as follows:
abcdefghij // 100 pixels wide
klmnopqrst // 100 pixels wide
uvwxyz // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.

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
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 1
        current_width = 0

        for ch in s:
            width = widths[ord(ch) - ord('a')]

            if current_width + width > 100:
                lines += 1
                current_width = width
            else:
                current_width += width

        return [lines, current_width]
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
- [434. Number of Segments in a String](../../0001-0500/0434-number-of-segments-in-a-string/)
- [1375. Number of Times Binary String Is Prefix-Aligned](../../1001-1500/1375-number-of-times-binary-string-is-prefix-aligned/)
- [1525. Number of Good Ways to Split a String](../../1501-2000/1525-number-of-good-ways-to-split-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-lines-to-write-string/)
