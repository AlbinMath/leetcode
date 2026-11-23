# LeetCode 2102: Sequentially Ordinal Rank Tracker

**LeetCode Problem #2102 — Sequentially Ordinal Rank Tracker**
Solve LeetCode Sequentially Ordinal Rank Tracker using Python and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sequentially Ordinal Rank Tracker |
| LeetCode | #2102 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
A scenic location is represented by its `name` and attractiveness `score`, where `name` is a **unique** string among all locations and `score` is an integer. Locations can be ranked from the best to the worst. The **higher** the score, the better the location. If the scores of two locations are equal, then the location with the **lexicographically smaller** name is better.

You are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports:

**Adding** scenic locations, **one at a time**. 
 **Querying** the `i^th` **best** location of **all locations already added**, where `i` is the number of times the system has been queried (including the current query).
 
 For example, when the system is queried for the `4^th` time, it returns the `4^th` best location of all locations already added.

Note that the test data are generated so that **at any time**, the number of queries **does not exceed** the number of locations added to the system.

Implement the `SORTracker` class:

`SORTracker()` Initializes the tracker system. 
 `void add(string name, int score)` Adds a scenic location with `name` and `score` to the system. 
 `string get()` Queries and returns the `i^th` best location, where `i` is the number of times this method has been invoked (including this invocation).

## Constraints
- `name` consists of lowercase English letters, and is unique among all locations.
- `1 <= name.length <= 10`
- `1 <= score <= 10^5`
- At any time, the number of calls to `get` does not exceed the number of calls to `add`.
- At most `4 * 10^4` calls **in total** will be made to `add` and `get`.

## Examples
### Example 1
- **Input:** `["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]`
- **Output:** `[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]`
- **Explanation:** SORTracker tracker = new SORTracker(); // Initialize the tracker system.
tracker.add("bradford", 2); // Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3); // Add location with name="branford" and score=3 to the system.
tracker.get(); // The sorted locations, from best to worst, are: branford, bradford.
 // Note that branford precedes bradford due to its

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Sequentially Ordinal Rank Tracker**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]`.
4. **Verification:** SORTracker tracker = new SORTracker(); // Initialize the tracker system.
tracker.add("bradford", 2); // Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3); // Add location with name="branford" and score=3 to the system.
tracker.get(); // The sorted locations, from best to worst, are: branford, bradford.
 // Note that branford precedes bradford due to its

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
Python

## Source Code
- [solution.py](./solution.py)


```python
import heapq

class Loc:
    __slots__ = ("score", "name")

    def __init__(self, score: int, name: str):
        self.score = score
        self.name = name

    def better(self, other) -> bool:
        if self.score != other.score:
            return self.score > other.score
        return self.name < other.name


class Best(Loc):          # best on top (for `rest`)
    def __lt__(self, other):
        return self.better(other)


class Worst(Loc):         # worst on top (for `top`)
    def __lt__(self, other):
        return other.better(self)


class SORTracker:
    def __init__(self):
        self.top = []     # Worst-ordered: locations already returned
        self.rest = []    # Best-ordered: locations not yet returned

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.top, Worst(score, name))
        w = heapq.heappop(self.top)
        heapq.heappush(self.rest, Best(w.score, w.name))

    def get(self) -> str:
        b = heapq.heappop(self.rest)
        heapq.heappush(self.top, Worst(b.score, b.name))
        return b.name
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
- [2671. Frequency Tracker](../../2501-3000/2778-frequency-tracker/)
- [3709. Design Exam Scores Tracker](../../4001-4500/4059-design-exam-scores-tracker/)
- [178. Rank Scores](../../0001-0500/0178-rank-scores/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sequentially-ordinal-rank-tracker/)
