# LeetCode 2785: Sort Vowels in a String

**LeetCode Problem #2785 — Sort Vowels in a String**
Solve LeetCode Sort Vowels in a String using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Vowels in a String |
| LeetCode | #2785 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given a **0-indexed** string `s`, **permute** `s` to get a new string `t` such that:

All consonants remain in their original places. More formally, if there is an index `i` with `0 <= i < s.length` such that `s[i]` is a consonant, then `t[i] = s[i]`. 
 The vowels must be sorted in the **nondecreasing** order of their **ASCII** values. More formally, for pairs of indices `i`, `j` with `0 <= i < j < s.length` such that `s[i]` and `s[j]` are vowels, then `t[i]` must not have a higher ASCII value than `t[j]`.

Return *the resulting string*.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of letters of the English alphabet in **uppercase and lowercase**.

## Examples
### Example 1
- **Input:** `s = "lEetcOde"`
- **Output:** `"lEOtcede"`
- **Explanation:** 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.

### Example 2
- **Input:** `s = "lYmpH"`
- **Output:** `"lYmpH"`
- **Explanation:** There are no vowels in s (all characters in s are consonants), so we return "lYmpH".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Sort Vowels in a String**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "lEetcOde"`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"lEOtcede"`.
4. **Verification:** 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.

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
var sortVowels = function(s) {
    const vowels = new Set(['a', 'e', 'i', 'o', 'u',
                            'A', 'E', 'I', 'O', 'U']);

    const arr = s.split('');
    const vowelList = [];

    for (const ch of arr) {
        if (vowels.has(ch)) {
            vowelList.push(ch);
        }
    }

    vowelList.sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0));

    let index = 0;

    for (let i = 0; i < arr.length; i++) {
        if (vowels.has(arr[i])) {
            arr[i] = vowelList[index++];
        }
    }

    return arr.join('');
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
- [345. Reverse Vowels of a String](../../0001-0500/0345-reverse-vowels-of-a-string/)
- [791. Custom Sort String](../../0501-1000/0791-custom-sort-string/)
- [1585. Check If String Is Transformable With Substring Sort Operations](../../1501-2000/1585-check-if-string-is-transformable-with-substring-sort-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-vowels-in-a-string/)
