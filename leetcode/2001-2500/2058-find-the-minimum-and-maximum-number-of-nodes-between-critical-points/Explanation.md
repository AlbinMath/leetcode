# LeetCode 2058: Find the Minimum and Maximum Number of Nodes Between Critical Points

**LeetCode Problem #2058 — Find the Minimum and Maximum Number of Nodes Between Critical Points**
Solve LeetCode Find the Minimum and Maximum Number of Nodes Between Critical Points using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find the Minimum and Maximum Number of Nodes Between Critical Points |
| LeetCode | #2058 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **critical point** in a linked list is defined as **either** a **local maxima** or a **local minima**.

A node is a **local maxima** if the current node has a value **strictly greater** than the previous node and the next node.

A node is a **local minima** if the current node has a value **strictly smaller** than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists **both** a previous node and a next node.

Given a linked list `head`, return *an array of length 2 containing *`[minDistance, maxDistance]`* where *`minDistance`* is the **minimum distance** between **any two distinct** critical points and *`maxDistance`* is the **maximum distance** between **any two distinct** critical points. If there are **fewer** than two critical points, return *`[-1, -1]`.

## Constraints
- The number of nodes in the list is in the range `[2, 10^5]`.
- `1 <= Node.val <= 10^5`

## Examples
### Example 1
- **Input:** `head = [3,1]`
- **Output:** `[-1,-1]`
- **Explanation:** There are no critical points in [3,1].

### Example 2
- **Input:** `head = [5,3,1,2,5,1,2]`
- **Output:** `[1,3]`
- **Explanation:** There are three critical points:
- [5,3,

### Example 3
- **Input:** `head = [1,3,2,2,3,2,2,2,7]`
- **Output:** `[3,3]`
- **Explanation:** There are two critical points:
- [1,

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
Traverse the linked list, tracking the position of each critical point (where `prev.val`, `curr.val`, `curr.next.val` form a local min or max). The minimum distance is between consecutive critical points; the maximum is between the first and last.

## Algorithm
1. Initialize state variables / data structure (**Array**).
2. Process elements sequentially using **Two Pointer Convergence & Scanning**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `head = [3,1]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[-1,-1]`.
4. **Verification:** There are no critical points in [3,1].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int first = -1;
        int last = -1;
        int minDist = INT_MAX;

        ListNode* prev = head;
        ListNode* curr = head->next;

        int index = 1;

        while (curr->next != nullptr) {
            ListNode* next = curr->next;

            // Check local maximum or local minimum
            if ((curr->val > prev->val && curr->val > next->val) ||
                (curr->val < prev->val && curr->val < next->val)) {

                if (first == -1) {
                    // First critical point
                    first = index;
                } else {
                    // Distance from previous critical point
                    minDist = min(minDist, index - last);
                }

                last = index;
            }

            prev = curr;
            curr = next;
            index++;
        }

        // Fewer than 2 critical points
        if (first == -1 || first == last) {
            return {-1, -1};
        }

        int maxDist = last - first;

        return {minDist, maxDist};
    }
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [783. Minimum Distance Between BST Nodes](../../0501-1000/0783-minimum-distance-between-bst-nodes/)
- [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](../../1001-1500/1489-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/)
- [1557. Minimum Number of Vertices to Reach All Nodes](../../1501-2000/1557-minimum-number-of-vertices-to-reach-all-nodes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)
