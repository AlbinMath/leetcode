# LeetCode 443: String Compression

**LeetCode Problem #443 — String Compression**
Solve LeetCode String Compression using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | String Compression |
| LeetCode | #443 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of **consecutive repeating characters** in `chars`:

If the group's length is `1`, append the character to `s`. 
 Otherwise, append the character followed by the group's length.

The compressed string `s` **should not be returned separately**, but instead, be stored **in the input character array `chars`**. Note that group lengths that are `10` or longer will be split into multiple characters in `chars`.

After you are done **modifying the input array,** return *the new length of the array*.

You must write an algorithm that uses only constant extra space.

**Note: **The characters in the array beyond the returned length do not matter and should be ignored.

## Constraints
- `1 <= chars.length <= 2000`
- `chars[i]` is a lowercase English letter, uppercase English letter, digit, or symbol.

## Examples
### Example 1
- **Input:** `chars = ["a","a","b","b","c","c","c"]`
- **Output:** `6`
- **Explanation:** The groups are `"aa"`, `"bb"`, and `"ccc"`. This compresses to `"a2b2c3"`.
After modifying the input array in-place, the first 6 characters of `chars` should be `["a","2","b","2","c","3"]`.

### Example 2
- **Input:** `chars = ["a"]`
- **Output:** `1`
- **Explanation:** The only group is `"a"`, which remains uncompressed since it is a single character.
After modifying the input array in-place, the first character of `chars` should be `["a"]`.

### Example 3
- **Input:** `chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]`
- **Output:** `4`
- **Explanation:** The groups are `"a"` and `"bbbbbbbbbbbb"`. This compresses to `"ab12"`.
After modifying the input array in-place, the first 4 characters of `chars` should be `["a","b","1","2"]`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **String Compression**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `chars = ["a","a","b","b","c","c","c"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.
4. **Verification:** The groups are `"aa"`, `"bb"`, and `"ccc"`. This compresses to `"a2b2c3"`.
After modifying the input array in-place, the first 6 characters of `chars` should be `["a","2","b","2","c","3"]`.

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
/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    let write = 0;
    let read = 0;

    while (read < chars.length) {
        let char = chars[read];
        let count = 0;

        // Count consecutive occurrences
        while (read < chars.length && chars[read] === char) {
            read++;
            count++;
        }

        // Write the character
        chars[write++] = char;

        // Write the count if greater than 1
        if (count > 1) {
            for (const digit of String(count)) {
                chars[write++] = digit;
            }
        }
    }

    return write;
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
- [1531. String Compression II](../../1501-2000/1637-string-compression-ii/)
- [2267.  Check if There Is a Valid Parentheses String Path](../../2001-2500/2349-check-if-there-is-a-valid-parentheses-string-path/)
- [8. String to Integer (atoi)](../../0001-0500/0008-string-to-integer-atoi/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/string-compression/)
