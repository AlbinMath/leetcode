# LeetCode 726: Number of Atoms

**LeetCode Problem #726 — Number of Atoms**
Solve LeetCode Number of Atoms using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Number of Atoms |
| LeetCode | #726 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a string `formula` representing a chemical formula, return *the count of each atom*.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than `1`. If the count is `1`, no digits will follow.

For example, `"H2O"` and `"H2O2"` are possible, but `"H1O2"` is impossible.

Two formulas are concatenated together to produce another formula.

For example, `"H2O2He3Mg4"` is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, `"(H2O2)"` and `"(H2O2)3"` are formulas.

Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than `1`), followed by the second name (in sorted order), followed by its count (if that count is more than `1`), and so on.

The test cases are generated so that all the values in the output fit in a **32-bit** integer.

## Constraints
- `1 <= formula.length <= 1000`
- `formula` consists of English letters, digits, `'('`, and `')'`.
- `formula` is always valid.

## Examples
### Example 1
- **Input:** `formula = "H2O"`
- **Output:** `"H2O"`
- **Explanation:** The count of elements are {'H': 2, 'O': 1}.

### Example 2
- **Input:** `formula = "Mg(OH)2"`
- **Output:** `"H2MgO2"`
- **Explanation:** The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

### Example 3
- **Input:** `formula = "K4(ON(SO3)2)2"`
- **Output:** `"K4N2O14S4"`
- **Explanation:** The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Number of Atoms**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `formula = "H2O"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"H2O"`.
4. **Verification:** The count of elements are {'H': 2, 'O': 1}.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countOfAtoms = function(formula) {
    const stack = [new Map()];
    let i = 0;

    while (i < formula.length) {
        const ch = formula[i];

        if (ch === '(') {
            stack.push(new Map());
            i++;
        }

        else if (ch === ')') {
            const top = stack.pop();
            i++;

            // Read multiplier after closing parenthesis
            let num = 0;

            while (i < formula.length && 
                   formula[i] >= '0' && formula[i] <= '9') {
                num = num * 10 + Number(formula[i]);
                i++;
            }

            if (num === 0) num = 1;

            // Multiply all elements inside parentheses
            const current = stack[stack.length - 1];

            for (const [element, count] of top) {
                current.set(
                    element,
                    (current.get(element) || 0) + count * num
                );
            }
        }

        else {
            // Read element name
            let element = formula[i];
            i++;

            while (i < formula.length &&
                   formula[i] >= 'a' && formula[i] <= 'z') {
                element += formula[i];
                i++;
            }

            // Read element count
            let num = 0;

            while (i < formula.length &&
                   formula[i] >= '0' && formula[i] <= '9') {
                num = num * 10 + Number(formula[i]);
                i++;
            }

            if (num === 0) num = 1;

            const current = stack[stack.length - 1];

            current.set(
                element,
                (current.get(element) || 0) + num
            );
        }
    }

    // Sort elements alphabetically
    const result = stack[0];
    const elements = [...result.keys()].sort();

    let answer = '';

    for (const element of elements) {
        answer += element;

        const count = result.get(element);

        if (count > 1) {
            answer += count;
        }
    }

    return answer;
};
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [65. Valid Number](../../0001-0500/0065-valid-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/number-of-atoms/)
