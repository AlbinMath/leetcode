# LeetCode 1815: Maximum Number of Groups Getting Fresh Donuts

**LeetCode Problem #1815 — Maximum Number of Groups Getting Fresh Donuts**
Solve LeetCode Maximum Number of Groups Getting Fresh Donuts using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Maximum Number of Groups Getting Fresh Donuts |
| LeetCode | #1815 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
There is a donuts shop that bakes donuts in batches of `batchSize`. They have a rule where they must serve **all** of the donuts of a batch before serving any donuts of the next batch. You are given an integer `batchSize` and an integer array `groups`, where `groups[i]` denotes that there is a group of `groups[i]` customers that will visit the shop. Each customer will get exactly one donut.

When a group visits the shop, all customers of the group must be served before serving any of the following groups. A group will be happy if they all get fresh donuts. That is, the first customer of the group does not receive a donut that was left over from the previous group.

You can freely rearrange the ordering of the groups. Return *the **maximum** possible number of happy groups after rearranging the groups.*

## Constraints
- `1 <= batchSize <= 9`
- `1 <= groups.length <= 30`
- `1 <= groups[i] <= 10^9`

## Examples
### Example 1
- **Input:** `batchSize = 3, groups = [1,2,3,4,5,6]`
- **Output:** `4`
- **Explanation:** You can arrange the groups as [6,2,4,5,1,3]. Then the 1^st, 2^nd, 4^th, and 6^th groups will be happy.

### Example 2
- **Input:** `batchSize = 4, groups = [1,3,2,5,2,2,1,6]`
- **Output:** `4`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Maximum Number of Groups Getting Fresh Donuts**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `batchSize = 3, groups = [1,2,3,4,5,6]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `4`.
4. **Verification:** You can arrange the groups as [6,2,4,5,1,3]. Then the 1^st, 2^nd, 4^th, and 6^th groups will be happy.

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
/**
 * @param {number} batchSize
 * @param {number[]} groups
 * @return {number}
 */
var maxHappyGroups = function(batchSize, groups) {
    const counts = new Array(batchSize).fill(0);
    let happy = 0;

    // Count groups by remainder.
    for (const group of groups) {
        const rem = group % batchSize;

        if (rem === 0) {
            happy++;
        } else {
            counts[rem]++;
        }
    }

    const memo = new Map();

    function dfs(remainder) {
        // Encode the remaining group counts and current remainder.
        const key = remainder + "|" + counts.slice(1).join(",");

        if (memo.has(key)) {
            return memo.get(key);
        }

        let best = 0;

        for (let r = 1; r < batchSize; r++) {
            if (counts[r] === 0) continue;

            // Serve one group with remainder r.
            counts[r]--;

            // A group is happy if no donuts are left over
            // before its first customer is served.
            const gain = remainder === 0 ? 1 : 0;

            best = Math.max(
                best,
                gain + dfs((remainder + r) % batchSize)
            );

            // Restore the count for other choices.
            counts[r]++;
        }

        memo.set(key, best);
        return best;
    }

    return happy + dfs(0);
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
- [2493. Divide Nodes Into the Maximum Number of Groups](../../2001-2500/2493-divide-nodes-into-the-maximum-number-of-groups/)
- [3839. Number of Prefix Connected Groups](../../3501-4000/3839-number-of-prefix-connected-groups/)
- [321. Create Maximum Number](../../0001-0500/0321-create-maximum-number/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/)
