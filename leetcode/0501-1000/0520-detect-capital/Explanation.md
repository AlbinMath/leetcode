# LeetCode 520: Detect Capital

**LeetCode Problem #520 — Detect Capital**
Solve LeetCode Detect Capital using JavaScript, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Detect Capital |
| LeetCode | #520 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like `"USA"`. 
 All letters in this word are not capitals, like `"leetcode"`. 
 Only the first letter in this word is capital, like `"Google"`.

Given a string `word`, return `true` if the usage of capitals in it is right.

## Constraints
- `1 <= word.length <= 100`
- `word` consists of lowercase and uppercase English letters.

## Examples
### Example 1
- **Input:** `word = "USA"`
- **Output:** `true`

### Example 2
- **Input:** `word = "FlaG"`
- **Output:** `false`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Detect Capital**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `word = "USA"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var detectCapitalUse = function(word) {
    return (
        word === word.toUpperCase() ||
        word === word.toLowerCase() ||
        word[0] === word[0].toUpperCase() &&
        word.slice(1) === word.slice(1).toLowerCase()
    );
};
```

### Python
```python
class Solution:
    def detectCapitalUse(self, word):
        if word.isupper():
            return True

        if word.islower():
            return True

        if word[0].isupper() and word[1:].islower():
            return True

        return False
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
- [1393. Capital Gain/Loss](../../1501-2000/1523-capital-gainloss/)
- [2477. Minimum Fuel Cost to Report to the Capital](../../2501-3000/2568-minimum-fuel-cost-to-report-to-the-capital/)
- [1559. Detect Cycles in 2D Grid](../../1501-2000/1663-detect-cycles-in-2d-grid/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/detect-capital/)
