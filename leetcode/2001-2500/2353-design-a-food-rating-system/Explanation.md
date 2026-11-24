# LeetCode 2353: Design a Food Rating System

**LeetCode Problem #2353 — Design a Food Rating System**
Solve LeetCode Design a Food Rating System using JavaScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Design a Food Rating System |
| LeetCode | #2353 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Design a food rating system that can do the following:

**Modify** the rating of a food item listed in the system. 
 Return the highest-rated food item for a type of cuisine in the system.

Implement the `FoodRatings` class:

`FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by `foods`, `cuisines` and `ratings`, all of which have a length of `n`.

`foods[i]` is the name of the `i^th` food, 
 `cuisines[i]` is the type of cuisine of the `i^th` food, and 
 `ratings[i]` is the initial rating of the `i^th` food. 
 
 
 `void changeRating(String food, int newRating)` Changes the rating of the food item with the name `food`. 
 `String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of `cuisine`. If there is a tie, return the item with the **lexicographically smaller** name.

Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.

## Constraints
- `1 <= n <= 2 * 10^4`
- `n == foods.length == cuisines.length == ratings.length`
- `1 <= foods[i].length, cuisines[i].length <= 10`
- `foods[i]`, `cuisines[i]` consist of lowercase English letters.
- `1 <= ratings[i] <= 10^8`
- All the strings in `foods` are **distinct**.
- `food` will be the name of a food item in the system across all calls to `changeRating`.
- `cuisine` will be a type of cuisine of **at least one** food item in the system across all calls to `highestRated`.
- At most `2 * 10^4` calls **in total** will be made to `changeRating` and `highestRated`.

## Examples
### Example 1
- **Input:** `["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]`
- **Output:** `[null, "kimchi", "ramen", null, "sushi", null, "ramen"]`
- **Explanation:** FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
 // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
 // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
 // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
 // Both "sushi" and "ramen" have a rating of 16.
 // However, "ramen" is lexicographically smaller than "sushi".

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
To solve **Design a Food Rating System**, we observe the problem requirements and utilize the **Hash Map** technique. By maintaining a **Dictionary / Hash Map**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Dictionary / Hash Map** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, "kimchi", "ramen", null, "sushi", null, "ramen"]`.
4. **Verification:** FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
 // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
 // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
 // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
 // Both "sushi" and "ramen" have a rating of 16.
 // However, "ramen" is lexicographically smaller than "sushi".

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
class FoodMaxHeap {
    constructor() {
        this.data = [];
    }
    peek() {
        return this.data[0];
    }
    _higherPriority(a, b) {
        if (a[0] !== b[0]) return a[0] > b[0];
        return a[1] < b[1];
    }
    push(val) {
        this.data.push(val);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this._higherPriority(this.data[p], this.data[i])) break;
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
                if (l < n && this._higherPriority(this.data[l], this.data[best])) best = l;
                if (r < n && this._higherPriority(this.data[r], this.data[best])) best = r;
                if (best === i) break;
                [this.data[i], this.data[best]] = [this.data[best], this.data[i]];
                i = best;
            }
        }
        return top;
    }
}
var FoodRatings = function(foods, cuisines, ratings) {
    this.foodRating = new Map();
    this.foodCuisine = new Map();
    this.cuisineHeaps = new Map();
    
    for (let i = 0; i < foods.length; i++) {
        const food = foods[i];
        const cuisine = cuisines[i];
        const rating = ratings[i];
        
        this.foodRating.set(food, rating);
        this.foodCuisine.set(food, cuisine);
        
        if (!this.cuisineHeaps.has(cuisine)) {
            this.cuisineHeaps.set(cuisine, new FoodMaxHeap());
        }
        this.cuisineHeaps.get(cuisine).push([rating, food]);
    }
};
FoodRatings.prototype.changeRating = function(food, newRating) {
    this.foodRating.set(food, newRating);
    const cuisine = this.foodCuisine.get(food);
    this.cuisineHeaps.get(cuisine).push([newRating, food]);
};
FoodRatings.prototype.highestRated = function(cuisine) {
    const heap = this.cuisineHeaps.get(cuisine);
    while (heap.peek()[0] !== this.foodRating.get(heap.peek()[1])) {
        heap.pop();
    }
    return heap.peek()[1];
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
- [1912. Design Movie Rental System](../../1501-2000/1912-design-movie-rental-system/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/design-a-food-rating-system/)
