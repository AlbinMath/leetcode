# LeetCode 211: Design Add and Search Words Data Structure

**LeetCode Problem #211 — Design Add and Search Words Data Structure**
Solve LeetCode Design Add and Search Words Data Structure using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Add and Search Words Data Structure |
| LeetCode | #211 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

`WordDictionary()` Initializes the object. 
 `void addWord(word)` Adds `word` to the data structure, it can be matched later. 
 `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

## Constraints
- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consist of `'.'` or lowercase English letters.
- There will be at most `2` dots in `word` for `search` queries.
- At most `10^4` calls will be made to `addWord` and `search`.

## Examples
Consider the standard input for **Design Add and Search Words Data Structure**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design Add and Search Words Data Structure**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Complement Lookup / Hash Table Frequency** step by step to the input yields the expected result.

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
var WordDictionary = function() {
    this.root = {};
};

WordDictionary.prototype.addWord = function(word) {
    let node = this.root;

    for (const char of word) {
        if (!node[char]) {
            node[char] = {};
        }
        node = node[char];
    }

    node.isEnd = true;
};

WordDictionary.prototype.search = function(word) {
    function dfs(node, index) {
        if (index === word.length) {
            return node.isEnd === true;
        }

        const char = word[index];

        if (char === ".") {
            for (const key of Object.keys(node)) {
                if (key !== "isEnd" && dfs(node[key], index + 1)) {
                    return true;
                }
            }
            return false;
        }

        if (!node[char]) {
            return false;
        }

        return dfs(node[char], index + 1);
    }

    return dfs(this.root, 0);
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
- [432. All O`one Data Structure](../../0001-0500/0432-all-oone-data-structure/)
- [295. Find Median from Data Stream](../../0001-0500/0295-find-median-from-data-stream/)
- [352. Data Stream as Disjoint Intervals](../../0001-0500/0352-data-stream-as-disjoint-intervals/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
