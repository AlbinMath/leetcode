# LeetCode 2296: Design a Text Editor

**LeetCode Problem #2296 — Design a Text Editor**
Solve LeetCode Design a Text Editor using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design a Text Editor |
| LeetCode | #2296 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Design a text editor with a cursor that can do the following:

**Add** text to where the cursor is. 
 **Delete** text from where the cursor is (simulating the backspace key). 
 **Move** the cursor either left or right.

When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that `0 <= cursor.position <= currentText.length` always holds.

Implement the `TextEditor` class:

`TextEditor()` Initializes the object with empty text. 
 `void addText(string text)` Appends `text` to where the cursor is. The cursor ends to the right of `text`. 
 `int deleteText(int k)` Deletes `k` characters to the left of the cursor. Returns the number of characters actually deleted. 
 `string cursorLeft(int k)` Moves the cursor to the left `k` times. Returns the last `min(10, len)` characters to the left of the cursor, where `len` is the number of characters to the left of the cursor. 
 `string cursorRight(int k)` Moves the cursor to the right `k` times. Returns the last `min(10, len)` characters to the left of the cursor, where `len` is the number of characters to the left of the cursor.

## Constraints
- `1 <= text.length, k <= 40`
- `text` consists of lowercase English letters.
- At most `2 * 10^4` calls **in total** will be made to `addText`, `deleteText`, `cursorLeft` and `cursorRight`.

## Examples
### Example 1
- **Input:** `["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]`
- **Output:** `[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]`
- **Explanation:** TextEditor textEditor = new TextEditor(); // The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode"); // The current text is "leetcode|".
textEditor.deleteText(4); // return 4
 // The current text is "leet|". 
 // 4 characters were deleted.
textEditor.addText("practice"); // The current text is "leetpractice|". 
textEditor.cursorRight(3); // return "etpractice"
 // The current text is "leetpractice|". 
 // The cursor cannot be moved beyond the actual text and thus did not move.
 // "etpractice" is the last 10 characters to the left of the cursor.
textEditor.cursorLeft(8); // return "leet"
 // The current text is "leet|practice".
 // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
textEditor.deleteText(10); // return 4
 // The current text is "|practice".
 // Only 4 characters were deleted.
textEditor.cursorLeft(2); // return ""
 // The current text is "|practice".
 // The cursor cannot be moved beyond the actual text and thus did not move. 
 // "" is the last min(10, 0) = 0 characters to the left of the cursor.
textEditor.cursorRight(6); // return "practi"
 // The current text is "practi|ce".
 // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Design a Text Editor**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["TextEditor", "addText", "deleteText", "addText", "cursorRight", "cursorLeft", "deleteText", "cursorLeft", "cursorRight"]
[[], ["leetcode"], [4], ["practice"], [3], [8], [10], [2], [6]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, 4, null, "etpractice", "leet", 4, "", "practi"]`.
4. **Verification:** TextEditor textEditor = new TextEditor(); // The current text is "|". (The '|' character represents the cursor)
textEditor.addText("leetcode"); // The current text is "leetcode|".
textEditor.deleteText(4); // return 4
 // The current text is "leet|". 
 // 4 characters were deleted.
textEditor.addText("practice"); // The current text is "leetpractice|". 
textEditor.cursorRight(3); // return "etpractice"
 // The current text is "leetpractice|". 
 // The cursor cannot be moved beyond the actual text and thus did not move.
 // "etpractice" is the last 10 characters to the left of the cursor.
textEditor.cursorLeft(8); // return "leet"
 // The current text is "leet|practice".
 // "leet" is the last min(10, 4) = 4 characters to the left of the cursor.
textEditor.deleteText(10); // return 4
 // The current text is "|practice".
 // Only 4 characters were deleted.
textEditor.cursorLeft(2); // return ""
 // The current text is "|practice".
 // The cursor cannot be moved beyond the actual text and thus did not move. 
 // "" is the last min(10, 0) = 0 characters to the left of the cursor.
textEditor.cursorRight(6); // return "practi"
 // The current text is "practi|ce".
 // "practi" is the last min(10, 6) = 6 characters to the left of the cursor.

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
class TextEditor:
    def __init__(self):
        self.left = []     # chars left of cursor, in order
        self.right = []    # chars right of cursor, reversed (top = next char)

    def addText(self, text: str) -> None:
        self.left.extend(text)

    def deleteText(self, k: int) -> int:
        k = min(k, len(self.left))
        if k:
            del self.left[-k:]
        return k

    def _last10(self) -> str:
        return ''.join(self.left[-10:])

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left))):
            self.right.append(self.left.pop())
        return self._last10()

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right))):
            self.left.append(self.right.pop())
        return self._last10()
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
- [211. Design Add and Search Words Data Structure](../../0001-0500/0211-design-add-and-search-words-data-structure/)
- [355. Design Twitter](../../0001-0500/0355-design-twitter/)
- [622. Design Circular Queue](../../0501-1000/0622-design-circular-queue/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-a-text-editor/)
