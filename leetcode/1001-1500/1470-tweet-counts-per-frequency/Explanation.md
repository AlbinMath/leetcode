# LeetCode 1348: Tweet Counts Per Frequency

**LeetCode Problem #1348 — Tweet Counts Per Frequency**
Solve LeetCode Tweet Counts Per Frequency using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Tweet Counts Per Frequency |
| LeetCode | #1348 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A social media company is trying to monitor activity on their site by analyzing the number of tweets that occur in select periods of time. These periods can be partitioned into smaller **time chunks** based on a certain frequency (every **minute**, **hour**, or **day**).

For example, the period `[10, 10000]` (in **seconds**) would be partitioned into the following **time chunks** with these frequencies:

Every **minute** (60-second chunks): `[10,69]`, `[70,129]`, `[130,189]`, `...`, `[9970,10000]` 
 Every **hour** (3600-second chunks): `[10,3609]`, `[3610,7209]`, `[7210,10000]` 
 Every **day** (86400-second chunks): `[10,10000]`

Notice that the last chunk may be shorter than the specified frequency's chunk size and will always end with the end time of the period (`10000` in the above example).

Design and implement an API to help the company with their analysis.

Implement the `TweetCounts` class:

`TweetCounts()` Initializes the `TweetCounts` object. 
 `void recordTweet(String tweetName, int time)` Stores the `tweetName` at the recorded `time` (in **seconds**). 
 `List<Integer> getTweetCountsPerFrequency(String freq, String tweetName, int startTime, int endTime)` Returns a list of integers representing the number of tweets with `tweetName` in each **time chunk** for the given period of time `[startTime, endTime]` (in **seconds**) and frequency `freq`.
 
 `freq` is one of `"minute"`, `"hour"`, or `"day"` representing a frequency of every **minute**, **hour**, or **day** respectively.

## Constraints
- `0 <= time, startTime, endTime <= 10^9`
- `0 <= endTime - startTime <= 10^4`
- There will be at most `10^4` calls **in total** to `recordTweet` and `getTweetCountsPerFrequency`.

## Examples
Consider the standard input for **Tweet Counts Per Frequency**. Applying **Complement Lookup / Hash Table Frequency** yields the target result step by step.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Tweet Counts Per Frequency**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
Applying **Complement Lookup / Hash Table Frequency** step by step to the input yields the expected result.

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
var TweetCounts = function() {
    this.tweets = new Map();
    this.freqMap = {
        minute: 60,
        hour: 3600,
        day: 86400
    };
};

TweetCounts.prototype.recordTweet = function(tweetName, time) {
    if (!this.tweets.has(tweetName)) {
        this.tweets.set(tweetName, []);
    }
    this.tweets.get(tweetName).push(time);
};

TweetCounts.prototype.getTweetCountsPerFrequency = function(freq, tweetName, startTime, endTime) {
    const delta = this.freqMap[freq];
    const numBuckets = Math.floor((endTime - startTime) / delta) + 1;
    const counts = new Array(numBuckets).fill(0);
    
    const times = this.tweets.get(tweetName) || [];
    for (const t of times) {
        if (t >= startTime && t <= endTime) {
            const idx = Math.floor((t - startTime) / delta);
            counts[idx]++;
        }
    }
    
    return counts;
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
- [1661. Average Time of Process per Machine](../../1501-2000/1801-average-time-of-process-per-machine/)
- [3433. Count Mentions Per User](../../3501-4000/3721-count-mentions-per-user/)
- [192. Word Frequency](../../0001-0500/0192-word-frequency/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/tweet-counts-per-frequency/)
