# LeetCode 1912: Design Movie Rental System

**LeetCode Problem #1912 — Design Movie Rental System**
Solve LeetCode Design Movie Rental System using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design Movie Rental System |
| LeetCode | #1912 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You have a movie renting company consisting of `n` shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array `entries` where `entries[i] = [shop_i, movie_i, price_i]` indicates that there is a copy of movie `movie_i` at shop `shop_i` with a rental price of `price_i`. Each shop carries **at most one** copy of a movie `movie_i`.

The system should support the following functions:

**Search**: Finds the **cheapest 5 shops** that have an **unrented copy** of a given movie. The shops should be sorted by **price** in ascending order, and in case of a tie, the one with the **smaller **`shop_i` should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned. 
 **Rent**: Rents an **unrented copy** of a given movie from a given shop. 
 **Drop**: Drops off a **previously rented copy** of a given movie at a given shop. 
 **Report**: Returns the **cheapest 5 rented movies** (possibly of the same movie ID) as a 2D list `res` where `res[j] = [shop_j, movie_j]` describes that the `j^th` cheapest rented movie `movie_j` was rented from the shop `shop_j`. The movies in `res` should be sorted by **price **in ascending order, and in case of a tie, the one with the **smaller **`shop_j` should appear first, and if there is still tie, the one with the **smaller **`movie_j` should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.

Implement the `MovieRentingSystem` class:

`MovieRentingSystem(int n, int[][] entries)` Initializes the `MovieRentingSystem` object with `n` shops and the movies in `entries`. 
 `List<Integer> search(int movie)` Returns a list of shops that have an **unrented copy** of the given `movie` as described above. 
 `void rent(int shop, int movie)` Rents the given `movie` from the given `shop`. 
 `void drop(int shop, int movie)` Drops off a previously rented `movie` at the given `shop`. 
 `List<List<Integer>> report()` Returns a list of cheapest **rented** movies as described above.

**Note:** The test cases will be generated such that `rent` will only be called if the shop has an **unrented** copy of the movie, and `drop` will only be called if the shop had **previously rented** out the movie.

## Constraints
- `1 <= n <= 3 * 10^5`
- `1 <= entries.length <= 10^5`
- `0 <= shop_i < n`
- `1 <= movie_i, price_i <= 10^4`
- Each shop carries **at most one** copy of a movie `movie_i`.
- At most `10^5` calls **in total** will be made to `search`, `rent`, `drop` and `report`.

## Examples
### Example 1
- **Input:** `["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]`
- **Output:** `[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]`
- **Explanation:** MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1); // return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.report(); // return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.search(2); // return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design Movie Rental System**, we observe the problem requirements and utilize the **Array / General** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]`.
4. **Verification:** MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1); // return [1, 0, 2], Movies of ID 1 are unrented at shops 1, 0, and 2. Shop 1 is cheapest; shop 0 and 2 are the same price, so order by shop number.
movieRentingSystem.rent(0, 1); // Rent movie 1 from shop 0. Unrented movies at shop 0 are now [2,3].
movieRentingSystem.rent(1, 2); // Rent movie 2 from shop 1. Unrented movies at shop 1 are now [1].
movieRentingSystem.report(); // return [[0, 1], [1, 2]]. Movie 1 from shop 0 is cheapest, followed by movie 2 from shop 1.
movieRentingSystem.drop(1, 2); // Drop off movie 2 at shop 1. Unrented movies at shop 1 are now [1,2].
movieRentingSystem.search(2); // return [0, 1]. Movies of ID 2 are unrented at shops 0 and 1. Shop 0 is cheapest, followed by shop 1.

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
class CustomMinHeap {
    constructor(compare) {
        this.data = [];
        this.compare = compare;
    }
    size() {
        return this.data.length;
    }
    push(val) {
        this.data.push(val);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.compare(this.data[p], this.data[i]) <= 0) break;
            [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
            i = p;
        }
    }
    pop() {
        const top = this.data[0];
        const last = this.data.pop();
        if (this.data.length > 0) {
            this.data[0] = last;
            let i = 0;
            const n = this.data.length;
            while (true) {
                let best = i;
                const l = (i << 1) + 1;
                const r = (i << 1) + 2;
                if (l < n && this.compare(this.data[l], this.data[best]) < 0) best = l;
                if (r < n && this.compare(this.data[r], this.data[best]) < 0) best = r;
                if (best === i) break;
                [this.data[i], this.data[best]] = [this.data[best], this.data[i]];
                i = best;
            }
        }
        return top;
    }
}

var MovieRentingSystem = function(n, entries) {
    this.prices = new Map();
    this.unrented = new Map();
    this.rentedSet = new Set();
    
    // Order by price ASC, then shop ASC, then movie ASC
    this.rentedHeap = new CustomMinHeap((a, b) => 
        a[0] !== b[0] ? a[0] - b[0] : (a[1] !== b[1] ? a[1] - b[1] : a[2] - b[2])
    );
    
    for (const [shop, movie, price] of entries) {
        this.prices.set(`${shop}:${movie}`, price);
        if (!this.unrented.has(movie)) {
            // Order by price ASC, then shop ASC
            this.unrented.set(movie, new CustomMinHeap((a, b) => 
                a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]
            ));
        }
        this.unrented.get(movie).push([price, shop]);
    }
};

MovieRentingSystem.prototype.search = function(movie) {
    const heap = this.unrented.get(movie);
    if (!heap) return [];
    
    const res = [];
    const restored = [];
    
    while (heap.size() > 0 && res.length < 5) {
        const [price, shop] = heap.pop();
        const key = `${shop}:${movie}`;
        if (this.rentedSet.has(key)) continue;
        
        const prev = restored[restored.length - 1];
        if (prev && prev[0] === price && prev[1] === shop) continue;
        
        res.push(shop);
        restored.push([price, shop]);
    }
    
    for (const item of restored) {
        heap.push(item);
    }
    return res;
};

MovieRentingSystem.prototype.rent = function(shop, movie) {
    const key = `${shop}:${movie}`;
    const price = this.prices.get(key);
    this.rentedSet.add(key);
    this.rentedHeap.push([price, shop, movie]);
};
MovieRentingSystem.prototype.drop = function(shop, movie) {
    const key = `${shop}:${movie}`;
    const price = this.prices.get(key);
    this.rentedSet.delete(key);
    this.unrented.get(movie).push([price, shop]);
};

MovieRentingSystem.prototype.report = function() {
    const res = [];
    const restored = [];
    
    while (this.rentedHeap.size() > 0 && res.length < 5) {
        const [price, shop, movie] = this.rentedHeap.pop();
        const key = `${shop}:${movie}`;
        if (!this.rentedSet.has(key)) continue;
        
        const prev = restored[restored.length - 1];
        if (prev && prev[0] === price && prev[1] === shop && prev[2] === movie) continue;
        
        res.push([shop, movie]);
        restored.push([price, shop, movie]);
    }
    
    for (const item of restored) {
        this.rentedHeap.push(item);
    }
    return res;
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
- [1396. Design Underground System](../../1001-1500/1396-design-underground-system/)
- [1603. Design Parking System](../../1501-2000/1603-design-parking-system/)
- [2349. Design a Number Container System](../../2001-2500/2349-design-a-number-container-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-movie-rental-system/)
