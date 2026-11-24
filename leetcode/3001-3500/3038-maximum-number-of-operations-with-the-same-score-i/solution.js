var maxOperations = function(nums) {
    const target = nums[0] + nums[1];
    let operations = 1;

    for (let i = 2; i + 1 < nums.length; i += 2) {
        if (nums[i] + nums[i + 1] === target) {
            operations++;
        } else {
            break;
        }
    }

    return operations;
};
