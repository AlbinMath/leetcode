# LeetCode 2213: Longest Substring of One Repeating Character

**LeetCode Problem #2213 — Longest Substring of One Repeating Character**
Solve LeetCode Longest Substring of One Repeating Character using Java and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Substring of One Repeating Character |
| LeetCode | #2213 |
| Difficulty | Hard |
| Language | Java |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `s`. You are also given a **0-indexed** string `queryCharacters` of length `k` and a **0-indexed** array of integer **indices** `queryIndices` of length `k`, both of which are used to describe `k` queries.

The `i^th` query updates the character in `s` at index `queryIndices[i]` to the character `queryCharacters[i]`.

Return *an array* `lengths` *of length *`k`* where* `lengths[i]` *is the **length** of the **longest substring** of *`s`* consisting of **only one repeating** character **after** the* `i^th` *query** is performed.*

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.
- `k == queryCharacters.length == queryIndices.length`
- `1 <= k <= 10^5`
- `queryCharacters` consists of lowercase English letters.
- `0 <= queryIndices[i] < s.length`

## Examples
### Example 1
- **Input:** `s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]`
- **Output:** `[3,3,4]`
- **Explanation:** - 1^st query updates s = " b

### Example 2
- **Input:** `s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]`
- **Output:** `[2,3]`
- **Explanation:** - 1^st query updates s = "ab

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
The code uses a **Segment Tree** where each node stores: the longest repeating prefix, suffix, and overall substring, plus the characters at the boundaries. Merging two segments checks if the suffix of the left and prefix of the right share the same character.

Time complexity is $O((N + Q) \log N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Sorted Array**).
2. Process elements sequentially using **Modified Binary Search**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3,3,4]`.
4. **Verification:** - 1^st query updates s = " b

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Java

## Source Code
- [solution.java](./solution.java)


```java
class Solution {
    class Node {
        char leftChar, rightChar;
        int prefix, suffix, best, len;

        Node(char c) {
            leftChar = rightChar = c;
            prefix = suffix = best = len = 1;
        }
    }

    Node[] tree;

    public int[] longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        int n = s.length();
        tree = new Node[4 * n];

        build(1, 0, n - 1, s);

        int k = queryIndices.length;
        int[] ans = new int[k];

        for (int i = 0; i < k; i++) {
            int pos = queryIndices[i];
            char c = queryCharacters.charAt(i);

            update(1, 0, n - 1, pos, c);

            ans[i] = tree[1].best;
        }

        return ans;
    }

    private void build(int node, int l, int r, String s) {
        if (l == r) {
            tree[node] = new Node(s.charAt(l));
            return;
        }

        int mid = l + (r - l) / 2;

        build(node * 2, l, mid, s);
        build(node * 2 + 1, mid + 1, r, s);

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    private void update(int node, int l, int r, int pos, char c) {
        if (l == r) {
            tree[node] = new Node(c);
            return;
        }

        int mid = l + (r - l) / 2;

        if (pos <= mid) {
            update(node * 2, l, mid, pos, c);
        } else {
            update(node * 2 + 1, mid + 1, r, pos, c);
        }

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    private Node merge(Node a, Node b) {
        Node res = new Node(a.leftChar);

        res.len = a.len + b.len;
        res.leftChar = a.leftChar;
        res.rightChar = b.rightChar;

        // Prefix
        res.prefix = a.prefix;

        if (a.prefix == a.len && a.rightChar == b.leftChar) {
            res.prefix = a.len + b.prefix;
        }

        // Suffix
        res.suffix = b.suffix;

        if (b.suffix == b.len && a.rightChar == b.leftChar) {
            res.suffix = b.len + a.suffix;
        }

        // Best
        res.best = Math.max(a.best, b.best);

        if (a.rightChar == b.leftChar) {
            res.best = Math.max(
                res.best,
                a.suffix + b.prefix
            );
        }

        return res;
    }
}
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3. Longest Substring Without Repeating Characters](../../0001-0500/0003-longest-substring-without-repeating-characters/)
- [395. Longest Substring with At Least K Repeating Characters](../../0001-0500/0395-longest-substring-with-at-least-k-repeating-characters/)
- [1156. Swap For Longest Repeated Character Substring](../../1001-1500/1156-swap-for-longest-repeated-character-substring/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)
