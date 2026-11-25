# LeetCode 433: Minimum Genetic Mutation

**LeetCode Problem #433 — Minimum Genetic Mutation**
Solve LeetCode Minimum Genetic Mutation using JavaScript and Sliding Window. This solution finds the optimal result using Dynamic Sliding Window Traversal in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Genetic Mutation |
| LeetCode | #433 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Dynamic Sliding Window Traversal |
| Data Structure | Array / Hash Set |
| Pattern | Sliding Window |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

Suppose we need to investigate a mutation from a gene string `startGene` to a gene string `endGene` where one mutation is defined as one single character changed in the gene string.

For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.

There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in `bank` to make it a valid gene string.

Given the two gene strings `startGene` and `endGene` and the gene bank `bank`, return *the minimum number of mutations needed to mutate from *`startGene`* to *`endGene`. If there is no such a mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

## Constraints
- `0 <= bank.length <= 10`
- `startGene.length == endGene.length == bank[i].length == 8`
- `startGene`, `endGene`, and `bank[i]` consist of only the characters `['A', 'C', 'G', 'T']`.

## Examples
### Example 1
- **Input:** `startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]`
- **Output:** `1`

### Example 2
- **Input:** `startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]`
- **Output:** `2`

## Key Insight
Maintain a dynamic contiguous window with two pointers (`left` and `right`), expanding to include new elements and shrinking when window invariants are violated.

## Approach
To solve **Minimum Genetic Mutation**, we observe the problem requirements and utilize the **Sliding Window** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]`.
2. **Processing Steps:** We apply **Dynamic Sliding Window Traversal** using our **Array / Hash Set**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array / Hash Set.

## Pattern
**Sliding Window**

## Topics
- Sliding Window
- Two Pointers
- Subarrays

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var minMutation = function(startGene, endGene, bank) {
    if (startGene === endGene) return 0;

    const validGenes = new Set(bank);
    if (!validGenes.has(endGene)) return -1;

    const genes = ["A", "C", "G", "T"];
    const queue = [[startGene, 0]];
    const visited = new Set([startGene]);

    let front = 0;

    while (front < queue.length) {
        const [gene, mutations] = queue[front++];

        // Try changing each character
        for (let i = 0; i < gene.length; i++) {
            for (const char of genes) {
                if (gene[i] === char) continue;

                const nextGene =
                    gene.slice(0, i) +
                    char +
                    gene.slice(i + 1);

                if (
                    validGenes.has(nextGene) &&
                    !visited.has(nextGene)
                ) {
                    if (nextGene === endGene) {
                        return mutations + 1;
                    }

                    visited.add(nextGene);
                    queue.push([nextGene, mutations + 1]);
                }
            }
        }
    }

    return -1;
};
```

## Why This Works
By utilizing **Sliding Window**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Shrinking the window too late or missing invalid state checks.
2. Forgetting to update window metrics (e.g. char counts) during contraction.
3. Misinterpreting fixed vs variable window requirements.

## Interview Notes
- **Tests:** Two-pointer window management, state tracking, and contiguous subarray analysis.
- **Follow-up:** How do you handle non-positive integer values in subarray sum windows?

## Related Problems
- [64. Minimum Path Sum](../../0001-0500/0064-minimum-path-sum/)
- [76. Minimum Window Substring](../../0001-0500/0076-minimum-window-substring/)
- [111. Minimum Depth of Binary Tree](../../0001-0500/0111-minimum-depth-of-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-genetic-mutation/)
