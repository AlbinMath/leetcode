# LeetCode 385: Mini Parser

**LeetCode Problem #385 — Mini Parser**
Solve LeetCode Mini Parser using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Mini Parser |
| LeetCode | #385 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return *the deserialized* `NestedInteger`.

Each element is either an integer or a list whose elements may also be integers or other lists.

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `s` consists of digits, square brackets `"[]"`, negative sign `'-'`, and commas `','`.
- `s` is the serialization of valid `NestedInteger`.
- All the values in the input are in the range `[-10^6, 10^6]`.

## Examples
### Example 1
- **Input:** `s = "324"`
- **Output:** `324`
- **Explanation:** You should return a NestedInteger object which contains a single integer 324.

### Example 2
- **Input:** `s = "[123,[456,[789]]]"`
- **Output:** `[123,[456,[789]]]`
- **Explanation:** Return a NestedInteger object containing a nested list with 2 elements:
1. An integer containing value 123.
2. A nested list containing two elements:
 i. An integer containing value 456.
 ii. A nested list with one element:
 a. An integer containing value 789

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Mini Parser**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "324"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `324`.
4. **Verification:** You should return a NestedInteger object which contains a single integer 324.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var deserialize = function(s) {
    // If input is a single integer
    if (s[0] !== '[') {
        let ni = new NestedInteger();
        ni.setInteger(Number(s));
        return ni;
    }

    const stack = [];
    let num = 0;
    let sign = 1;
    let readingNumber = false;

    for (let i = 0; i < s.length; i++) {
        const ch = s[i];

        if (ch === '[') {
            const ni = new NestedInteger();
            stack.push(ni);

        } else if (ch === '-' ) {
            sign = -1;
            readingNumber = true;

        } else if (ch >= '0' && ch <= '9') {
            num = num * 10 + Number(ch);
            readingNumber = true;

        } else if (ch === ',' || ch === ']') {

            // Add the completed integer to current list
            if (readingNumber) {
                const ni = new NestedInteger();
                ni.setInteger(num * sign);

                stack[stack.length - 1].add(ni);

                num = 0;
                sign = 1;
                readingNumber = false;
            }

            // Close current list
            if (ch === ']') {
                const current = stack.pop();

                // Attach nested list to its parent
                if (stack.length > 0) {
                    stack[stack.length - 1].add(current);
                } else {
                    return current;
                }
            }
        }
    }
};
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1410. HTML Entity Parser](../../1501-2000/1526-html-entity-parser/)
- [1678. Goal Parser Interpretation](../../1501-2000/1797-goal-parser-interpretation/)
- [20. Valid Parentheses](../../0001-0500/0020-valid-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/mini-parser/)
