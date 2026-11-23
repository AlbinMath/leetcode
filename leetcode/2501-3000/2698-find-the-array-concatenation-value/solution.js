var findTheArrayConcVal = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    let total = 0;

    while (left < right) {
        total += Number(`${nums[left]}${nums[right]}`);
        left++;
        right--;
    }

    if (left === right) {
        total += nums[left];
    }

    return total;
};
