
var sortJumbled = function(mapping, nums) {
    const arr = [];
    for (let i = 0; i < nums.length; i++) {
        const mappedValue = Number(
            nums[i]
                .toString()
                .split("")
                .map(digit => mapping[Number(digit)])
                .join("")
        );

        arr.push({
            original: nums[i],
            mapped: mappedValue,
            index: i
        });
    }
    arr.sort((a, b) => {
        if (a.mapped !== b.mapped) {
            return a.mapped - b.mapped;
        }

        return a.index - b.index;
    });
    return arr.map(item => item.original);
};

