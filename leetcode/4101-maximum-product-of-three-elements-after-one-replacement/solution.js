
var maxProduct = function(nums) {
    let max1 = 0;
    let max2 = 0;

    for (const num of nums) {
        const value = Math.abs(num);

        if (value >= max1) {
            max2 = max1;
            max1 = value;
        } else if (value > max2) {
            max2 = value;
        }
    }

    return 100000 * max1 * max2;
};

