# LeetCode 1744: Can You Eat Your Favorite Candy on Your Favorite Day?

**LeetCode Problem #1744 — Can You Eat Your Favorite Candy on Your Favorite Day?**
Solve LeetCode Can You Eat Your Favorite Candy on Your Favorite Day? using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Can You Eat Your Favorite Candy on Your Favorite Day? |
| LeetCode | #1744 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **(0-indexed)** array of positive integers `candiesCount` where `candiesCount[i]` represents the number of candies of the `i^th` type you have. You are also given a 2D array `queries` where `queries[i] = [favoriteType_i, favoriteDay_i, dailyCap_i]`.

You play a game with the following rules:

You start eating candies on day `**0**`. 
 You cannot eat **any** candy of type `i` unless you have eaten **all** candies of type `i - 1`. 
 You must eat **at least** **one** candy per day until you have eaten all the candies.

Construct a boolean array `answer` such that `answer.length == queries.length` and `answer[i]` is `true` if you can eat a candy of type `favoriteType_i` on day `favoriteDay_i` without eating **more than** `dailyCap_i` candies on **any** day, and `false` otherwise. Note that you can eat different types of candy on the same day, provided that you follow rule 2.

Return *the constructed array *`answer`.

## Constraints
- `1 <= candiesCount.length <= 10^5`
- `1 <= candiesCount[i] <= 10^5`
- `1 <= queries.length <= 10^5`
- `queries[i].length == 3`
- `0 <= favoriteType_i < candiesCount.length`
- `0 <= favoriteDay_i <= 10^9`
- `1 <= dailyCap_i <= 10^9`

## Examples
### Example 1
- **Input:** `candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]`
- **Output:** `[true,false,true]`
- **Explanation:** 1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you will eat a candy of type 0 on day 2.
2- You can eat at most 4 candies each day.
 If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and 4 candies (type 0 and type 1) on day 1.
 On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a candy of type 4 on day 2.
3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.

### Example 2
- **Input:** `candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]`
- **Output:** `[false,true,true,false,false]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Can You Eat Your Favorite Candy on Your Favorite Day?**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,false,true]`.
4. **Verification:** 1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you will eat a candy of type 0 on day 2.
2- You can eat at most 4 candies each day.
 If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and 4 candies (type 0 and type 1) on day 1.
 On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a candy of type 4 on day 2.
3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.

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
var canEat = function(candiesCount, queries) {
    const n = candiesCount.length;

    // Build prefix sum
    let prefix = new Array(n);
    prefix[0] = candiesCount[0];

    for (let i = 1; i < n; i++) {
        prefix[i] = prefix[i - 1] + candiesCount[i];
    }

    let answer = [];

    for (let [type, day, cap] of queries) {
        let before = type === 0 ? 0 : prefix[type - 1];
        let through = prefix[type];
        let minEaten = day + 1;
        let maxEaten = BigInt(day + 1) * BigInt(cap);

        let canEatFavorite =
            minEaten <= through &&
            maxEaten > BigInt(before);

        answer.push(canEatFavorite);
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
- [1970. Last Day Where You Can Still Cross](../../1501-2000/1970-last-day-where-you-can-still-cross/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)
- [1420. Build Array Where You Can Find The Maximum Exactly K Comparisons](../../1001-1500/1420-build-array-where-you-can-find-the-maximum-exactly-k-comparisons/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/)
