# LeetCode 2559: Count Vowel Strings in Ranges

**LeetCode Problem #2559 — Count Vowel Strings in Ranges**
Solve LeetCode Count Vowel Strings in Ranges using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Vowel Strings in Ranges |
| LeetCode | #2559 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** array of strings `words` and a 2D array of integers `queries`.

Each query `queries[i] = [l_i, r_i]` asks us to find the number of strings present at the indices ranging from `l_i` to `r_i` (both **inclusive**) of `words` that start and end with a vowel.

Return *an array *`ans`* of size *`queries.length`*, where *`ans[i]`* is the answer to the *`i`^th* query*.

**Note** that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

## Constraints
- `1 <= words.length <= 10^5`
- `1 <= words[i].length <= 40`
- `words[i]` consists only of lowercase English letters.
- `sum(words[i].length) <= 3 * 10^5`
- `1 <= queries.length <= 10^5`
- `0 <= l_i <= r_i < words.length`

## Examples
### Example 1
- **Input:** `words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]`
- **Output:** `[2,3,0]`
- **Explanation:** The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

### Example 2
- **Input:** `words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]`
- **Output:** `[3,2,1]`
- **Explanation:** Every string satisfies the conditions, so we return [3,2,1].

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Vowel Strings in Ranges**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3,0]`.
4. **Verification:** The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

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
var vowelStrings = function(words, queries) {
    const n = words.length;
    const vowels = new Set(['a', 'e', 'i', 'o', 'u']);
    let prefix = new Array(n + 1).fill(0);

    for (let i = 0; i < n; i++) {
        let word = words[i];

        let first = word[0];
        let last = word[word.length - 1];

        let isValid = vowels.has(first) && vowels.has(last);

        prefix[i + 1] = prefix[i] + (isValid ? 1 : 0);
    }

    let result = [];

    for (let [l, r] of queries) {
        result.push(prefix[r + 1] - prefix[l]);
    }

    return result;
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
- [1641. Count Sorted Vowel Strings](../../1501-2000/1641-count-sorted-vowel-strings/)
- [2586. Count the Number of Vowel Strings in Range](../../2501-3000/2586-count-the-number-of-vowel-strings-in-range/)
- [2062. Count Vowel Substrings of a String](../../2001-2500/2062-count-vowel-substrings-of-a-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-vowel-strings-in-ranges/)
