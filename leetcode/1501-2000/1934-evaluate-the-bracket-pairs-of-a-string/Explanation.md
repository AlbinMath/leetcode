# LeetCode 1807: Evaluate the Bracket Pairs of a String

**LeetCode Problem #1807 — Evaluate the Bracket Pairs of a String**
Solve LeetCode Evaluate the Bracket Pairs of a String using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Evaluate the Bracket Pairs of a String |
| LeetCode | #1807 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a string `s` that contains some bracket pairs, with each pair containing a **non-empty** key.

For example, in the string `"(name)is(age)yearsold"`, there are **two** bracket pairs that contain the keys `"name"` and `"age"`.

You know the values of a wide range of keys. This is represented by a 2D string array `knowledge` where each `knowledge[i] = [key_i, value_i]` indicates that key `key_i` has a value of `value_i`.

You are tasked to evaluate **all** of the bracket pairs. When you evaluate a bracket pair that contains some key `key_i`, you will:

Replace `key_i` and the bracket pair with the key's corresponding `value_i`. 
 If you do not know the value of the key, you will replace `key_i` and the bracket pair with a question mark `"?"` (without the quotation marks).

Each key will appear at most once in your `knowledge`. There will not be any nested brackets in `s`.

Return *the resulting string after evaluating **all** of the bracket pairs.*

## Constraints
- `1 <= s.length <= 10^5`
- `0 <= knowledge.length <= 10^5`
- `knowledge[i].length == 2`
- `1 <= key_i.length, value_i.length <= 10`
- `s` consists of lowercase English letters and round brackets `'('` and `')'`.
- Every open bracket `'('` in `s` will have a corresponding close bracket `')'`.
- The key in each bracket pair of `s` will be non-empty.
- There will not be any nested bracket pairs in `s`.
- `key_i` and `value_i` consist of lowercase English letters.
- Each `key_i` in `knowledge` is unique.

## Examples
### Example 1
- **Input:** `s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]`
- **Output:** `"bobistwoyearsold"`
- **Explanation:** The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

### Example 2
- **Input:** `s = "hi(name)", knowledge = [["a","b"]]`
- **Output:** `"hi?"`
- **Explanation:** As you do not know the value of the key "name", replace "(name)" with "?".

### Example 3
- **Input:** `s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]`
- **Output:** `"yesyesyesaaa"`
- **Explanation:** The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
1. **Map:** Store all key-value pairs in a hash map.
2. **Parse:** Iterate through the string. When encountering `(`, find the matching `)`, extract the key, look it up in the map, and append the value (or `?`) to the result.
3. Regular characters are appended directly.

Time complexity is $O(N + K)$ where $N$ is string length and $K$ is total key-value data, and space complexity is $O(N + K)$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"bobistwoyearsold"`.
4. **Verification:** The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        unordered_map<string, string> mp;

        // Store key-value pairs
        for (auto& k : knowledge) {
            mp[k[0]] = k[1];
        }

        string ans;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                int j = i + 1;

                // Find closing bracket
                while (s[j] != ')') {
                    j++;
                }

                // Extract key
                string key = s.substr(i + 1, j - i - 1);

                // Replace with value or '?'
                if (mp.find(key) != mp.end())
                    ans += mp[key];
                else
                    ans += '?';

                // Skip closing bracket
                i = j;
            } 
            else {
                ans += s[i];
            }
        }

        return ans;
    }
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
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [2744. Find Maximum Number of String Pairs](../../2501-3000/2847-find-maximum-number-of-string-pairs/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/)
