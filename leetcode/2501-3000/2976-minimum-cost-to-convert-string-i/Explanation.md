# LeetCode 2976: Minimum Cost to Convert String I

**LeetCode Problem #2976 — Minimum Cost to Convert String I**
Solve LeetCode Minimum Cost to Convert String I using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Cost to Convert String I |
| LeetCode | #2976 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two **0-indexed** strings `source` and `target`, both of length `n` and consisting of **lowercase** English letters. You are also given two **0-indexed** character arrays `original` and `changed`, and an integer array `cost`, where `cost[i]` represents the cost of changing the character `original[i]` to the character `changed[i]`.

You start with the string `source`. In one operation, you can pick a character `x` from the string and change it to the character `y` at a cost of `z` **if** there exists **any** index `j` such that `cost[j] == z`, `original[j] == x`, and `changed[j] == y`.

Return *the **minimum** cost to convert the string *`source`* to the string *`target`* using **any** number of operations. If it is impossible to convert* `source` *to* `target`, *return* `-1`.

**Note** that there may exist indices `i`, `j` such that `original[j] == original[i]` and `changed[j] == changed[i]`.

## Constraints
- `1 <= source.length == target.length <= 10^5`
- `source`, `target` consist of lowercase English letters.
- `1 <= cost.length == original.length == changed.length <= 2000`
- `original[i]`, `changed[i]` are lowercase English letters.
- `1 <= cost[i] <= 10^6`
- `original[i] != changed[i]`

## Examples
### Example 1
- **Input:** `source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]`
- **Output:** `28`
- **Explanation:** To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.

### Example 2
- **Input:** `source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]`
- **Output:** `12`
- **Explanation:** To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

### Example 3
- **Input:** `source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]`
- **Output:** `-1`
- **Explanation:** It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Cost to Convert String I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `28`.
4. **Verification:** To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.

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
var minimumCost = function (source, target, original, changed, cost) {
    const INF = Infinity;
    const dist = Array.from({ length: 26 }, (_, i) => {
        const row = new Array(26).fill(INF);
        row[i] = 0;
        return row;
    });

    for (let i = 0; i < cost.length; i++) {
        const a = original[i].charCodeAt(0) - 97;
        const b = changed[i].charCodeAt(0) - 97;
        if (cost[i] < dist[a][b]) dist[a][b] = cost[i];
    }

    for (let k = 0; k < 26; k++) {
        for (let i = 0; i < 26; i++) {
            if (dist[i][k] === INF) continue;
            for (let j = 0; j < 26; j++) {
                const d = dist[i][k] + dist[k][j];
                if (d < dist[i][j]) dist[i][j] = d;
            }
        }
    }

    let total = 0;
    for (let i = 0; i < source.length; i++) {
        const d = dist[source.charCodeAt(i) - 97][target.charCodeAt(i) - 97];
        if (d === INF) return -1;
        total += d;
    }
    return total;
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
- [2977. Minimum Cost to Convert String II](../../2501-3000/2977-minimum-cost-to-convert-string-ii/)
- [2027. Minimum Moves to Convert String](../../2001-2500/2027-minimum-moves-to-convert-string/)
- [3864. Minimum Cost to Partition a Binary String](../../3501-4000/3864-minimum-cost-to-partition-a-binary-string/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-cost-to-convert-string-i/)
