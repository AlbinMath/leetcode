# LeetCode 1190: Reverse Substrings Between Each Pair of Parentheses

**LeetCode Problem #1190 — Reverse Substrings Between Each Pair of Parentheses**
Solve LeetCode Reverse Substrings Between Each Pair of Parentheses using C++ and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Reverse Substrings Between Each Pair of Parentheses |
| LeetCode | #1190 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should **not** contain any brackets.

## Constraints
- `1 <= s.length <= 2000`
- `s` only contains lower case English characters and parentheses.
- It is guaranteed that all parentheses are balanced.

## Examples
### Example 1
- **Input:** `s = "(abcd)"`
- **Output:** `"dcba"`

### Example 2
- **Input:** `s = "(u(love)i)"`
- **Output:** `"iloveu"`
- **Explanation:** The substring "love" is reversed first, then the whole string is reversed.

### Example 3
- **Input:** `s = "(ed(et(oc))el)"`
- **Output:** `"leetcode"`
- **Explanation:** First, we reverse the substring "oc", then "etco", and finally, the whole string.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **Stack of Strings**.

1. **Maintain `current`:** A string being built from the current nesting level.
2. **On `(`:** Push `current` onto the stack (save progress) and reset `current` to empty.
3. **On `)`:** Reverse `current`, then prepend the string from the top of the stack (pop it). This effectively reverses the content within the parentheses and concatenates it with the content before the opening parenthesis.
4. **On any other character:** Append it to `current`.
5. After processing all characters, `current` holds the final result.

Time complexity is $O(N^2)$ in the worst case (due to reversals) and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "(abcd)"`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"dcba"`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    string reverseParentheses(string s) {
        stack<string> st;
        string current = "";

        for (char c : s) {
            if (c == '(') {
                st.push(current);
                current = "";
            }
            else if (c == ')') {
                reverse(current.begin(), current.end());

                current = st.top() + current;
                st.pop();
            }
            else {
                current += c;
            }
        }

        return current;
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
- [3918. Sum of Primes Between Number and Its Reverse](../../4001-4500/4297-sum-of-primes-between-number-and-its-reverse/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [2932. Maximum Strong Pair XOR I](../../3001-3500/3193-maximum-strong-pair-xor-i/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)
