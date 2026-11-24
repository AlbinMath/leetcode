
var maxCandies = function(status, candies, keys, containedBoxes, initialBoxes) {
    const n = status.length;

    // Track boxes we possess and boxes already opened
    const hasBox = new Array(n).fill(false);
    const opened = new Array(n).fill(false);

    const queue = [];

    // Add initially available boxes
    for (const box of initialBoxes) {
        hasBox[box] = true;

        if (status[box] === 1) {
            queue.push(box);
        }
    }

    let totalCandies = 0;
    let index = 0;

    while (index < queue.length) {
        const box = queue[index++];

        // Avoid processing a box more than once
        if (opened[box]) continue;

        opened[box] = true;

        // Collect candies
        totalCandies += candies[box];

        // Obtain keys from this box
        for (const key of keys[box]) {
            status[key] = 1;

            // If we already possess this box, we can open it
            if (hasBox[key] && !opened[key]) {
                queue.push(key);
            }
        }

        // Discover boxes inside the current box
        for (const nextBox of containedBoxes[box]) {
            hasBox[nextBox] = true;

            // Open immediately if we have its key
            if (status[nextBox] === 1 && !opened[nextBox]) {
                queue.push(nextBox);
            }
        }
    }

    return totalCandies;
};

