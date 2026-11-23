# LeetCode 736: Parse Lisp Expression

**LeetCode Problem #736 — Parse Lisp Expression**
Solve LeetCode Parse Lisp Expression using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Parse Lisp Expression |
| LeetCode | #736 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, let expression, add expression, mult expression, or an assigned variable. Expressions always evaluate to a single integer. 
 (An integer could be positive or negative.) 
 A let expression takes the form `"(let v_1 e_1 v_2 e_2 ... v_n e_n expr)"`, where let is always the string `"let"`, then there are one or more pairs of alternating variables and expressions, meaning that the first variable `v_1` is assigned the value of the expression `e_1`, the second variable `v_2` is assigned the value of the expression `e_2`, and so on sequentially; and then the value of this let expression is the value of the expression `expr`. 
 An add expression takes the form `"(add e_1 e_2)"` where add is always the string `"add"`, there are always two expressions `e_1`, `e_2` and the result is the addition of the evaluation of `e_1` and the evaluation of `e_2`. 
 A mult expression takes the form `"(mult e_1 e_2)"` where mult is always the string `"mult"`, there are always two expressions `e_1`, `e_2` and the result is the multiplication of the evaluation of e1 and the evaluation of e2. 
 For this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally, for your convenience, the names `"add"`, `"let"`, and `"mult"` are protected and will never be used as variable names. 
 Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on the scope.

## Constraints
- `1 <= expression.length <= 2000`
- There are no leading or trailing spaces in `expression`.
- All tokens are separated by a single space in `expression`.
- The answer and all intermediate calculations of that answer are guaranteed to fit in a **32-bit** integer.
- The expression is guaranteed to be legal and evaluate to an integer.

## Examples
### Example 1
- **Input:** `expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"`
- **Output:** `14`
- **Explanation:** In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

### Example 2
- **Input:** `expression = "(let x 3 x 2 x)"`
- **Output:** `2`
- **Explanation:** Assignment in let statements is processed sequentially.

### Example 3
- **Input:** `expression = "(let x 1 y 2 x (add x y) (add x y))"`
- **Output:** `5`
- **Explanation:** The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Parse Lisp Expression**, we observe the problem requirements and utilize the **Bit Manipulation** technique. By maintaining a **Integer Bitmask**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Integer Bitmask** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `14`.
4. **Verification:** In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def evaluate(self, expression: str) -> int:
        s = expression
        n = len(s)
        scopes = []

        def read_token(i):
            j = i
            while j < n and s[j] != ' ' and s[j] != ')':
                j += 1
            return s[i:j], j

        def lookup(name):
            for sc in reversed(scopes):
                if name in sc:
                    return sc[name]

        def parse(i):
            # returns (value, next index)
            if s[i] != '(':
                tok, j = read_token(i)
                if tok[0].isdigit() or tok[0] == '-':
                    return int(tok), j
                return lookup(tok), j

            i += 1  # skip '('
            op, i = read_token(i)
            i += 1  # skip space after keyword

            if op == 'add' or op == 'mult':
                a, i = parse(i)
                i += 1  # skip space
                b, i = parse(i)
                i += 1  # skip ')'
                return (a + b if op == 'add' else a * b), i

            # let
            scopes.append({})
            while True:
                if s[i] == '(':
                    val, i = parse(i)
                    break
                tok, j = read_token(i)
                if s[j] == ')':
                    # last token is the result expression
                    val, i = parse(i)
                    break
                # tok is a variable name
                i = j + 1
                v, i = parse(i)
                scopes[-1][tok] = v
                i += 1  # skip space
            scopes.pop()
            i += 1  # skip ')'
            return val, i

        return parse(0)[0]
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
- [10. Regular Expression Matching](../../0001-0500/0010-regular-expression-matching/)
- [282. Expression Add Operators](../../0001-0500/0282-expression-add-operators/)
- [1106. Parsing A Boolean Expression](../../1001-1500/1197-parsing-a-boolean-expression/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/parse-lisp-expression/)
