# LeetCode 3926: Count Valid Word Occurrences

**LeetCode Problem #3926 — Count Valid Word Occurrences**
Solve LeetCode Count Valid Word Occurrences using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Valid Word Occurrences |
| LeetCode | #3926 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of strings `chunks`. Concatenate all strings in `chunks` in order to form a string `s`.

You are also given an array of strings `queries`.

A **joiner hyphen** is a hyphen character `'-'` in `s` whose previous and next characters both exist and are lowercase English letters.

A **word** is a **maximal** substring of `s` consisting only of lowercase English letters and **joiner hyphens**.

All other characters, including spaces and hyphens that are not **joiner hyphens**, are treated as separators.

Return an integer array `ans`, where `ans[i]` is the number of times `queries[i]` appears as a word in `s`.

## Constraints
- `1 <= chunks.length <= 10^5`
- `1 <= chunks[i].length <= 10^5`
- The total length of all strings in `chunks` does not exceed `10^5`.
- `chunks[i]` consists only of lowercase English letters, spaces, and `'-'`.
- `1 <= queries.length <= 10^5`
- `1 <= queries[i].length <= 10^5`
- The total length of all strings in `queries` does not exceed `10^5`.
- `queries[i]` consists only of lowercase English letters and `'-'`.
- `queries[i]` is a valid word: it does not start or end with `'-'`, and it does not contain two consecutive hyphens.

## Examples
### Example 1
- **Input:** `chunks = ["hello wor","ld hello"], queries = ["hello","world","wor"]`
- **Output:** `[2,1,0]`
- **Explanation:** After concatenating all strings in `chunks`, `s = "hello world hello"`. 
 The words are `"hello"`, `"world"`, and `"hello"`. 
 The substring `"wor"` appears inside `"world"`, but it is not a full word.

### Example 2
- **Input:** `chunks = ["a-b a--b ","a-","b"], queries = ["a-b","a","b"]`
- **Output:** `[2,1,1]`
- **Explanation:** After concatenating all strings in `chunks`, `s = "a-b a--b a-b"`. 
 In `"a-b"`, the hyphen is a joiner hyphen because it is between two lowercase English letters, so `"a-b"` is one word. 
 In `"a--b"`, neither hyphen is a joiner hyphen, so it is split into the words `"a"` and `"b"`. 
 Therefore, the words are `"a-b"`, `"a"`, `"b"`, and `"a-b"`.

### Example 3
- **Input:** `chunks = ["-cat dog- mouse"], queries = ["cat","dog","mouse","cat-dog"]`
- **Output:** `[1,1,1,0]`
- **Explanation:** After concatenating all strings in `chunks`, `s = "-cat dog- mouse"`. 
 The leading hyphen before `"cat"` and the trailing hyphen after `"dog"` are not joiner hyphens, so they are separators. 
 The words are `"cat"`, `"dog"`, and `"mouse"`.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Valid Word Occurrences**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `chunks = ["hello wor","ld hello"], queries = ["hello","world","wor"]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,1,0]`.
4. **Verification:** After concatenating all strings in `chunks`, `s = "hello world hello"`. 
 The words are `"hello"`, `"world"`, and `"hello"`. 
 The substring `"wor"` appears inside `"world"`, but it is not a full word.

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
var countWordOccurrences = function(chunks, queries) {
    const s = chunks.join('');

    const words = s.match(/[a-z]+(?:-[a-z]+)*/g) || [];

    const freq = new Map();

    for (const word of words) {
        freq.set(word, (freq.get(word) || 0) + 1);
    }

    return queries.map(query => freq.get(query) || 0);
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
- [1359. Count All Valid Pickup and Delivery Options](../../1001-1500/1461-count-all-valid-pickup-and-delivery-options/)
- [2284. Sender With Largest Word Count](../../2001-2500/2378-sender-with-largest-word-count/)
- [2867. Count Valid Paths in a Tree](../../3001-3500/3112-count-valid-paths-in-a-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-valid-word-occurrences/)
