# LeetCode 770: Basic Calculator IV

**LeetCode Problem #770 — Basic Calculator IV**
Solve LeetCode Basic Calculator IV using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Basic Calculator IV |
| LeetCode | #770 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an expression such as `expression = "e + 8 - a + 5"` and an evaluation map such as `{"e": 1}` (given in terms of `evalvars = ["e"]` and `evalints = [1]`), return a list of tokens representing the simplified expression, such as `["-1*a","14"]`

An expression alternates chunks and symbols, with a space separating each chunk and symbol. 
 A chunk is either an expression in parentheses, a variable, or a non-negative integer. 
 A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like `"2x"` or `"-x"`.

Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction.

For example, `expression = "1 + 2 * 3"` has an answer of `["7"]`.

The format of the output is as follows:

For each term of free variables with a non-zero coefficient, we write the free variables within a term in sorted order lexicographically.
 
 For example, we would never write a term like `"b*a*c"`, only `"a*b*c"`. 
 
 
 Terms have degrees equal to the number of free variables being multiplied, counting multiplicity. We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
 
 For example, `"a*a*b*c"` has degree `4`. 
 
 
 The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.) A leading coefficient of 1 is still printed. 
 An example of a well-formatted answer is `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]`. 
 Terms (including constant terms) with coefficient `0` are not included.
 
 For example, an expression of `"0"` has an output of `[]`.

**Note:** You may assume that the given expression is always valid. All intermediate results will be in the range of `[-2^31, 2^31 - 1]`.

## Constraints
- `1 <= expression.length <= 250`
- `expression` consists of lowercase English letters, digits, `'+'`, `'-'`, `'*'`, `'('`, `')'`, `' '`.
- `expression` does not contain any leading or trailing spaces.
- All the tokens in `expression` are separated by a single space.
- `0 <= evalvars.length <= 100`
- `1 <= evalvars[i].length <= 20`
- `evalvars[i]` consists of lowercase English letters.
- `evalints.length == evalvars.length`
- `-100 <= evalints[i] <= 100`

## Examples
### Example 1
- **Input:** `expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]`
- **Output:** `["-1*a","14"]`

### Example 2
- **Input:** `expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]`
- **Output:** `["-1*pressure","5"]`

### Example 3
- **Input:** `expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []`
- **Output:** `["1*e*e","-64"]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Basic Calculator IV**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["-1*a","14"]`.

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
from typing import List
from collections import defaultdict

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        env = dict(zip(evalvars, evalints))

        def add(p, q, sign=1):
            r = defaultdict(int, p)
            for k, v in q.items():
                r[k] += sign * v
            return {k: v for k, v in r.items() if v != 0}

        def mul(p, q):
            r = defaultdict(int)
            for k1, v1 in p.items():
                for k2, v2 in q.items():
                    r[tuple(sorted(k1 + k2))] += v1 * v2
            return {k: v for k, v in r.items() if v != 0}

        def make(tok):
            if tok.isdigit():
                v = int(tok)
                return {(): v} if v else {}
            if tok in env:
                v = env[tok]
                return {(): v} if v else {}
            return {(tok,): 1}

        # tokenize
        tokens = []
        i, n = 0, len(expression)
        while i < n:
            c = expression[i]
            if c == ' ':
                i += 1
            elif c in '+-*()':
                tokens.append(c)
                i += 1
            else:
                j = i
                while j < n and expression[j].isalnum():
                    j += 1
                tokens.append(expression[i:j])
                i = j

        prec = {'+': 1, '-': 1, '*': 2}
        vals, ops = [], []

        def apply():
            op = ops.pop()
            b = vals.pop()
            a = vals.pop()
            if op == '+':
                vals.append(add(a, b))
            elif op == '-':
                vals.append(add(a, b, -1))
            else:
                vals.append(mul(a, b))

        for tok in tokens:
            if tok == '(':
                ops.append(tok)
            elif tok == ')':
                while ops[-1] != '(':
                    apply()
                ops.pop()
            elif tok in prec:
                while ops and ops[-1] != '(' and prec[ops[-1]] >= prec[tok]:
                    apply()
                ops.append(tok)
            else:
                vals.append(make(tok))
        while ops:
            apply()

        poly = vals[0]
        keys = sorted(poly, key=lambda k: (-len(k), k))
        res = []
        for k in keys:
            c = poly[k]
            res.append('*'.join([str(c)] + list(k)))
        return res
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
- [224. Basic Calculator](../../0001-0500/0224-basic-calculator/)
- [227. Basic Calculator II](../../0001-0500/0227-basic-calculator-ii/)
- [2642. Design Graph With Shortest Path Calculator](../../2501-3000/2642-design-graph-with-shortest-path-calculator/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/basic-calculator-iv/)
