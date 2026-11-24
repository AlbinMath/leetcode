# LeetCode 2424: Longest Uploaded Prefix

**LeetCode Problem #2424 — Longest Uploaded Prefix**
Solve LeetCode Longest Uploaded Prefix using JavaScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longest Uploaded Prefix |
| LeetCode | #2424 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a stream of `n` videos, each represented by a **distinct** number from `1` to `n` that you need to "upload" to a server. You need to implement a data structure that calculates the length of the **longest uploaded prefix** at various points in the upload process.

We consider `i` to be an uploaded prefix if all videos in the range `1` to `i` (**inclusive**) have been uploaded to the server. The longest uploaded prefix is the **maximum **value of `i` that satisfies this definition. 
 
Implement the `LUPrefix `class:

`LUPrefix(int n)` Initializes the object for a stream of `n` videos. 
 `void upload(int video)` Uploads `video` to the server. 
 `int longest()` Returns the length of the **longest uploaded prefix** defined above.

## Constraints
- `1 <= n <= 10^5`
- `1 <= video <= n`
- All values of `video` are **distinct**.
- At most `2 * 10^5` calls **in total** will be made to `upload` and `longest`.
- At least one call will be made to `longest`.

## Examples
### Example 1
- **Input:** `["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]`
- **Output:** `[null, null, 0, null, 1, null, 3]`
- **Explanation:** LUPrefix server = new LUPrefix(4); // Initialize a stream of 4 videos.
server.upload(3); // Upload video 3.
server.longest(); // Since video 1 has not been uploaded yet, there is no prefix.
 // So, we return 0.
server.upload(1); // Upload video 1.
server.longest(); // The prefix [1] is the longest uploaded prefix, so we return 1.
server.upload(2); // Upload video 2.
server.longest(); // The prefix [1,2,3] is the longest uploaded prefix, so we return 3.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longest Uploaded Prefix**, we observe the problem requirements and utilize the **Prefix Sum** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, 0, null, 1, null, 3]`.
4. **Verification:** LUPrefix server = new LUPrefix(4); // Initialize a stream of 4 videos.
server.upload(3); // Upload video 3.
server.longest(); // Since video 1 has not been uploaded yet, there is no prefix.
 // So, we return 0.
server.upload(1); // Upload video 1.
server.longest(); // The prefix [1] is the longest uploaded prefix, so we return 1.
server.upload(2); // Upload video 2.
server.longest(); // The prefix [1,2,3] is the longest uploaded prefix, so we return 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var LUPrefix = function(n) {
    this.uploaded = new Array(n + 1).fill(false);
    this.prefix = 0;
};

LUPrefix.prototype.upload = function(video) {
    this.uploaded[video] = true;

    // Extend the prefix while the next video is uploaded
    while (
        this.prefix + 1 < this.uploaded.length &&
        this.uploaded[this.prefix + 1]
    ) {
        this.prefix++;
    }
};

LUPrefix.prototype.longest = function() {
    return this.prefix;
};
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [1392. Longest Happy Prefix](../../1001-1500/1392-longest-happy-prefix/)
- [3043. Find the Length of the Longest Common Prefix](../../3001-3500/3043-find-the-length-of-the-longest-common-prefix/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longest-uploaded-prefix/)
