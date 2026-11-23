var numberOfGoodPartitions = function(nums) {
    const MOD = 1000000007;
    const last = new Map();

    for (let i = 0; i < nums.length; i++) {
        last.set(nums[i], i);
    }

    let partitions = 0;
    let end = 0;

    for (let i = 0; i < nums.length; i++) {
        end = Math.max(end, last.get(nums[i]));

        if (i === end && i < nums.length - 1) {
            partitions++;
        }
    }

    return Number(2n ** BigInt(partitions) % BigInt(MOD));
};
