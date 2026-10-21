
var jump = function(nums) {
    let jumps = 0;
    let currentEnd = 0;
    let farthest = 0;

    for (let i = 0; i < nums.length - 1; i++) {
        // Farthest index reachable from the current range
        farthest = Math.max(farthest, i + nums[i]);

        // Reached the end of the current jump range
        if (i === currentEnd) {
            jumps++;
            currentEnd = farthest;

            // The last index is reachable
            if (currentEnd >= nums.length - 1) {
                break;
            }
        }
    }

    return jumps;
};

