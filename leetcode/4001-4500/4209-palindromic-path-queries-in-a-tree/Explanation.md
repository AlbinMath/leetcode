# LeetCode 3841: Palindromic Path Queries in a Tree

**LeetCode Problem #3841 — Palindromic Path Queries in a Tree**
Solve LeetCode Palindromic Path Queries in a Tree using JavaScript, Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Palindromic Path Queries in a Tree |
| LeetCode | #3841 |
| Difficulty | Hard |
| Language | JavaScript, Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an undirected tree with `n` nodes labeled 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between nodes `u_i` and `v_i`.

You are also given a string `s` of length `n` consisting of lowercase English letters, where `s[i]` represents the character assigned to node `i`.

You are also given a string array `queries`, where each `queries[i]` is either:

`"update u_i c"`: Change the character at node `u_i` to `c`. Formally, update `s[u_i] = c`. 
 `"query u_i v_i"`: Determine whether the string formed by the characters on the **unique** path from `u_i` to `v_i` (inclusive) can be **rearranged** into a ** palindrome **.

Return a boolean array `answer`, where `answer[j]` is `true` if the `j^th` query of type `"query u_i v_i"​​​​​​​` can be rearranged into a **palindrome**, and `false` otherwise.

## Constraints
- `1 <= n == s.length <= 5 * 10^4`
- `edges.length == n - 1`
- `edges[i] = [u_i, v_i]`
- `0 <= u_i, v_i <= n - 1`
- `s` consists of lowercase English letters.
- The input is generated such that `edges` represents a valid tree.
- `1 <= queries.length <= 5 * 10^4`​​​​​​​
 
 `queries[i] = "update u_i c"` or
- `queries[i] = "query u_i v_i"`
- `0 <= u_i, v_i <= n - 1`
- `c` is a lowercase English letter.

## Examples
### Example 1
- **Input:** `n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]`
- **Output:** `[true,false]`
- **Explanation:** `"query 0 2"`: Path `0 &rarr; 1 &rarr; 2` gives `"aac"`, which can be rearranged to form `"aca"`, a palindrome. Thus, `answer[0] = true`. 
 `"update 1 b"`: Update node 1 to `'b'`, now `s = "abc"`. 
 `"query 0 2"`: Path characters are `"abc"`, which cannot be rearranged to form a palindrome. Thus, `answer[1] = false`. 
 

 Thus, `answer = [true, false]`.

### Example 2
- **Input:** `n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]`
- **Output:** `[false,false,true]`
- **Explanation:** `"query 1 2"`: Path `1 &rarr; 0 &rarr; 2` gives `"bac"`, which cannot be rearranged to form a palindrome. Thus, `answer[0] = false`. 
 `"update 0 b"`: Update node 0 to `'b'`, now `s = "bbca"`. 
 `"query 2 3"`: Path `2 &rarr; 0 &rarr; 3` gives `"cba"`, which cannot be rearranged to form a palindrome. Thus, `answer[1] = false`. 
 `"update 3 a"`: Update node 3 to `'a'`, `s = "bbca"`. 
 `"query 1 3"`: Path `1 &rarr; 0 &rarr; 3` gives `"bba"`, which can be rearranged to form `"bab"`, a palindrome. Thus, `answer[2] = true`. 
 

 Thus, `answer = [false, false, true]`.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Palindromic Path Queries in a Tree**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,false]`.
4. **Verification:** `"query 0 2"`: Path `0 &rarr; 1 &rarr; 2` gives `"aac"`, which can be rearranged to form `"aca"`, a palindrome. Thus, `answer[0] = true`. 
 `"update 1 b"`: Update node 1 to `'b'`, now `s = "abc"`. 
 `"query 0 2"`: Path characters are `"abc"`, which cannot be rearranged to form a palindrome. Thus, `answer[1] = false`. 
 

 Thus, `answer = [true, false]`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var palindromePath = function (n, edges, s, queries) {
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const LOG = Math.max(1, 32 - Math.clz32(n - 1));
    const up = Array.from({ length: LOG }, () => new Int32Array(n));
    const depth = new Int32Array(n);
    const tin = new Int32Array(n);
    const tout = new Int32Array(n);
    const mask = new Int32Array(n);
    for (let i = 0; i < n; i++) mask[i] = 1 << (s.charCodeAt(i) - 97);

    // Iterative DFS: push node for "enter", ~node for "exit"
    let timer = 0;
    const stack = [0];
    up[0][0] = 0;
    while (stack.length) {
        const top = stack.pop();
        if (top < 0) {
            tout[~top] = timer - 1;
            continue;
        }
        const node = top;
        tin[node] = timer++;
        stack.push(~node);
        const par = up[0][node];
        for (const nb of adj[node]) {
            if (nb !== par || (node === 0 && nb !== 0 && false)) {
                if (nb === par && node !== 0) continue;
            }
            if (nb === par && node !== 0) continue;
            if (node === 0 && nb === par) continue; // root's "parent" is itself; no self-loops in a tree
            up[0][nb] = node;
            depth[nb] = depth[node] + 1;
            stack.push(nb);
        }
    }

    for (let k = 1; k < LOG; k++) {
        const prev = up[k - 1], cur = up[k];
        for (let v = 0; v < n; v++) cur[v] = prev[prev[v]];
    }

    const lca = (a, b) => {
        if (depth[a] < depth[b]) { const t = a; a = b; b = t; }
        let diff = depth[a] - depth[b];
        for (let k = 0; diff > 0; k++, diff >>= 1) {
            if (diff & 1) a = up[k][a];
        }
        if (a === b) return a;
        for (let k = LOG - 1; k >= 0; k--) {
            if (up[k][a] !== up[k][b]) {
                a = up[k][a];
                b = up[k][b];
            }
        }
        return up[0][a];
    };

    // XOR Fenwick tree: range-xor update, point query
    const bit = new Int32Array(n + 2);
    const add = (i, val) => {
        for (i += 1; i <= n + 1; i += i & -i) bit[i] ^= val;
    };
    const prefix = (i) => {
        let res = 0;
        for (i += 1; i > 0; i -= i & -i) res ^= bit[i];
        return res;
    };
    const rangeXor = (l, r, val) => {
        add(l, val);
        add(r + 1, val);
    };

    for (let v = 0; v < n; v++) rangeXor(tin[v], tout[v], mask[v]);

    const ans = [];
    for (const q of queries) {
        const parts = q.split(" ");
        if (parts[0] === "update") {
            const x = parseInt(parts[1]);
            const nw = 1 << (parts[2].charCodeAt(0) - 97);
            const delta = mask[x] ^ nw;
            if (delta !== 0) {
                rangeXor(tin[x], tout[x], delta);
                mask[x] = nw;
            }
        } else {
            const u = parseInt(parts[1]);
            const v = parseInt(parts[2]);
            const l = lca(u, v);
            const m = prefix(tin[u]) ^ prefix(tin[v]) ^ mask[l];
            ans.push((m & (m - 1)) === 0);
        }
    }
    return ans;
};
```

### Python
```python
class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Build parent, depth, and traversal order iteratively.
        parent = [-1] * n
        depth = [0] * n
        order = []
        stack = [0]
        parent[0] = 0

        while stack:
            u = stack.pop()
            order.append(u)

            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                stack.append(v)

        # 2. Calculate subtree sizes and heavy children.
        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        # 3. Heavy-Light Decomposition.
        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            start, chain_head = stack.pop()
            u = start

            while u != -1:
                head[u] = chain_head
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        # 4. Segment tree: XOR of character parity masks.
        base = 1
        while base < n:
            base <<= 1

        seg = [0] * (2 * base)
        chars = [1 << (ord(c) - ord('a')) for c in s]

        for u in range(n):
            seg[base + pos[u]] = chars[u]

        for i in range(base - 1, 0, -1):
            seg[i] = seg[i << 1] ^ seg[i << 1 | 1]

        def point_update(p, value):
            p += base
            seg[p] = value
            p >>= 1

            while p:
                seg[p] = seg[p << 1] ^ seg[p << 1 | 1]
                p >>= 1

        def range_query(left, right):
            # Inclusive range [left, right].
            left += base
            right += base
            result = 0

            while left <= right:
                if left & 1:
                    result ^= seg[left]
                    left += 1

                if not (right & 1):
                    result ^= seg[right]
                    right -= 1

                left >>= 1
                right >>= 1

            return result

        # 5. XOR all character masks along a tree path.
        def path_query(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_query(pos[u], pos[v])
            return result

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - ord('a'))

                if chars[u] != new_mask:
                    chars[u] = new_mask
                    point_update(pos[u], new_mask)

            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = path_query(u, v)

                # At most one character may have odd frequency.
                ans.append((mask & (mask - 1)) == 0)

        return ans
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
- [124. Binary Tree Maximum Path Sum](../../0001-0500/0124-binary-tree-maximum-path-sum/)
- [1104. Path In Zigzag Labelled Binary Tree](../../1001-1500/1194-path-in-zigzag-labelled-binary-tree/)
- [1372. Longest ZigZag Path in a Binary Tree](../../1001-1500/1474-longest-zigzag-path-in-a-binary-tree/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)
