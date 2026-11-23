# LeetCode 831: Masking Personal Information

**LeetCode Problem #831 — Masking Personal Information**
Solve LeetCode Masking Personal Information using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Masking Personal Information |
| LeetCode | #831 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a personal information string `s`, representing either an **email address** or a **phone number**. Return *the **masked** personal information using the below rules*.

**Email address:**

An email address is:

A **name** consisting of **at least** two uppercase and lowercase English letters, followed by 
 The `'@'` symbol, followed by 
 The **domain** consisting of uppercase and lowercase English letters with a dot `'.'` somewhere in the middle (not the first or last character).

To mask an email:

The uppercase letters in the **name** and **domain** must be converted to lowercase letters. 
 The middle letters of the **name** (i.e., all but the first and last letters) must be replaced by 5 asterisks `"*****"`.

**Phone number:**

A phone number is formatted as follows:

The phone number contains 10-13 digits. 
 The last 10 digits make up the **local number**. 
 The remaining 0-3 digits, in the beginning, make up the **country code**. 
 **Separation characters** from the set `{'+', '-', '(', ')', ' '}` separate the above digits in some way.

To mask a phone number:

Remove all **separation characters**. 
 The masked phone number should have the form:
 
 `"***-***-XXXX"` if the country code has 0 digits. 
 `"+*-***-***-XXXX"` if the country code has 1 digit. 
 `"+**-***-***-XXXX"` if the country code has 2 digits. 
 `"+***-***-***-XXXX"` if the country code has 3 digits. 
 
 
 `"XXXX"` is the last 4 digits of the **local number**.

## Constraints
- `s` is either a **valid** email or a phone number.
- If `s` is an email:
 
 `8 <= s.length <= 40`
- `s` consists of uppercase and lowercase English letters and exactly one `'@'` symbol and `'.'` symbol.
- If `s` is a phone number:
 
 `10 <= s.length <= 20`
- `s` consists of digits, spaces, and the symbols `'('`, `')'`, `'-'`, and `'+'`.

## Examples
### Example 1
- **Input:** `s = "LeetCode@LeetCode.com"`
- **Output:** `"l*****e@leetcode.com"`
- **Explanation:** s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.

### Example 2
- **Input:** `s = "AB@qq.com"`
- **Output:** `"a*****b@qq.com"`
- **Explanation:** s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
Note that even though "ab" is 2 characters, it still must have 5 asterisks in the middle.

### Example 3
- **Input:** `s = "1(234)567-890"`
- **Output:** `"***-***-7890"`
- **Explanation:** s is a phone number.
There are 10 digits, so the local number is 10 digits and the country code is 0 digits.
Thus, the resulting masked number is "***-***-7890".

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Masking Personal Information**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "LeetCode@LeetCode.com"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"l*****e@leetcode.com"`.
4. **Verification:** s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var maskPII = function(s) {
    if (s.includes("@")) {
        // Email address
        s = s.toLowerCase();
        let at = s.indexOf("@");

        return s[0] + "*****" + s.slice(at - 1);
    } else {
        // Phone number
        let digits = s.replace(/\D/g, "");
        let local = digits.slice(-4);
        let countryCodeLength = digits.length - 10;

        let result = "***-***-" + local;

        if (countryCodeLength > 0) {
            result = "+" + "*".repeat(countryCodeLength) +
                     "-" + result;
        }

        return result;
    }
};
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
- [1965. Employees With Missing Information](../../2001-2500/2110-employees-with-missing-information/)
- [5. Longest Palindromic Substring](../../0001-0500/0005-longest-palindromic-substring/)
- [26. Remove Duplicates from Sorted Array](../../0001-0500/0026-remove-duplicates-from-sorted-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/masking-personal-information/)
