var returnToBoundaryCount = function(nums) {
    let position = 0;
    let returns = 0;

    for (const step of nums) {
        position += step;
        if (position === 0) {
            returns++;
        }
    }

    return returns;
};
