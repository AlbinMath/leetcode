# LeetCode 508: Most Frequent Subtree Sum

**LeetCode Problem #508 — Most Frequent Subtree Sum**
Solve LeetCode Most Frequent Subtree Sum using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Frequent Subtree Sum |
| LeetCode | #508 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the `root` of a binary tree, return the most frequent **subtree sum**. If there is a tie, return all the values with the highest frequency in any order.

The **subtree sum** of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^5 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `root = [5,2,-3]`
- **Output:** `[2,-3,4]`

### Example 2
- **Input:** `root = [5,2,-5]`
- **Output:** `[2]`

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Most Frequent Subtree Sum**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `root = [5,2,-3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,-3,4]`.

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
var findFrequentTreeSum = function(root) {
    const counts = new Map();
    let maxFreq = 0;
    
    function dfs(node) {
        if (!node) return 0;
        
        const currSum = node.val + dfs(node.left) + dfs(node.right);
        const freq = (counts.get(currSum) || 0) + 1;
        counts.set(currSum, freq);
        
        if (freq > maxFreq) {
            maxFreq = freq;
        }
        
        return currSum;
    }
    
    dfs(root);
    
    const result = [];
    for (const [sum, freq] of counts.entries()) {
        if (freq === maxFreq) {
            result.push(sum);
        }
    }
    
    return result;
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
- [1838. Frequency of the Most Frequent Element](../../1501-2000/1966-frequency-of-the-most-frequent-element/)
- [3044. Most Frequent Prime](../../3001-3500/3314-most-frequent-prime/)
- [3962. Maximum Subarray Sum After at Most K Swaps](../../4001-4500/4246-maximum-subarray-sum-after-at-most-k-swaps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-frequent-subtree-sum/)
