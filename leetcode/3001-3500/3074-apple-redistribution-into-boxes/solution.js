
var minimumBoxes = function(apple, capacity) {
    let totalApples = apple.reduce((sum, x) => sum + x, 0);
    capacity.sort((a, b) => b - a);

    let count = 0;
    for (let cap of capacity) {
        totalApples -= cap;
        count++;

        if (totalApples <= 0) {
            return count;
        }
    }

    return count;
};

