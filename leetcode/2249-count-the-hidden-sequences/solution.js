
var numberOfArrays = function(differences, lower, upper) {
    let current = 0;
    let min = 0;
    let max = 0;

    for (let diff of differences) {
        current += diff;

        min = Math.min(min, current);
        max = Math.max(max, current);
    }

    return Math.max(0, (upper - lower) - (max - min) + 1);
};
