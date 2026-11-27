# LeetCode 2456: Most Popular Video Creator

**LeetCode Problem #2456 — Most Popular Video Creator**
Solve LeetCode Most Popular Video Creator using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Most Popular Video Creator |
| LeetCode | #2456 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two string arrays `creators` and `ids`, and an integer array `views`, all of length `n`. The `i^th` video on a platform was created by `creators[i]`, has an id of `ids[i]`, and has `views[i]` views.

The **popularity** of a creator is the **sum** of the number of views on **all** of the creator's videos. Find the creator with the **highest** popularity and the id of their **most** viewed video.

If multiple creators have the highest popularity, find all of them. 
 If multiple videos have the highest view count for a creator, find the lexicographically **smallest** id.

Note: It is possible for different videos to have the same `id`, meaning that `id`s do not uniquely identify a video. For example, two videos with the same ID are considered as distinct videos with their own viewcount.

Return* *a **2D array** of **strings** `answer` where `answer[i] = [creators_i, id_i]` means that `creators_i` has the **highest** popularity and `id_i` is the **id** of their most **popular** video. The answer can be returned in any order.

## Constraints
- `n == creators.length == ids.length == views.length`
- `1 <= n <= 10^5`
- `1 <= creators[i].length, ids[i].length <= 5`
- `creators[i]` and `ids[i]` consist only of lowercase English letters.
- `0 <= views[i] <= 10^5`

## Examples
### Example 1
- **Input:** `creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]`
- **Output:** `[["alice","one"],["bob","two"]]`
- **Explanation:** The popularity of alice is 5 + 5 = 10. 
The popularity of bob is 10. 
The popularity of chris is 4. 
alice and bob are the most popular creators. 
For bob, the video with the highest view count is "two". 
For alice, the videos with the highest view count are "one" and "three". Since "one" is lexicographically smaller than "three", it is included in the answer.

### Example 2
- **Input:** `creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]`
- **Output:** `[["alice","b"]]`
- **Explanation:** The videos with id "b" and "c" have the highest view count. 
Since "b" is lexicographically smaller than "c", it is included in the answer.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Most Popular Video Creator**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[["alice","one"],["bob","two"]]`.
4. **Verification:** The popularity of alice is 5 + 5 = 10. 
The popularity of bob is 10. 
The popularity of chris is 4. 
alice and bob are the most popular creators. 
For bob, the video with the highest view count is "two". 
For alice, the videos with the highest view count are "one" and "three". Since "one" is lexicographically smaller than "three", it is included in the answer.

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
var mostPopularCreator = function(creators, ids, views) {
    const map = new Map();

    for (let i = 0; i < creators.length; i++) {
        const creator = creators[i];
        const id = ids[i];
        const view = views[i];

        if (!map.has(creator)) {
            map.set(creator, {
                totalViews: 0,
                maxViews: -1,
                bestId: ""
            });
        }

        const data = map.get(creator);

        data.totalViews += view;

        if (
            view > data.maxViews ||
            (view === data.maxViews && id < data.bestId)
        ) {
            data.maxViews = view;
            data.bestId = id;
        }
    }

    let maxPopularity = 0;

    for (const data of map.values()) {
        maxPopularity = Math.max(
            maxPopularity,
            data.totalViews
        );
    }

    const answer = [];

    for (const [creator, data] of map) {
        if (data.totalViews === maxPopularity) {
            answer.push([creator, data.bestId]);
        }
    }

    return answer;
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
- [11. Container With Most Water](../../0001-0500/0011-container-with-most-water/)
- [508. Most Frequent Subtree Sum](../../0501-1000/0508-most-frequent-subtree-sum/)
- [602. Friend Requests II: Who Has the Most Friends](../../0501-1000/0602-friend-requests-ii-who-has-the-most-friends/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/most-popular-video-creator/)
