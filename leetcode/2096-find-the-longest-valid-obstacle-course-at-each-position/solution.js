
var longestObstacleCourseAtEachPosition = function(obstacles) {
    const tails = [];
    const ans = [];

    for (const height of obstacles) {
        let left = 0;
        let right = tails.length;

        // Find the first tails element > height
        while (left < right) {
            const mid = Math.floor((left + right) / 2);

            if (tails[mid] <= height) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        // Course length ending at this obstacle
        ans.push(left + 1);

        // Extend tails or replace an existing ending height
        if (left === tails.length) {
            tails.push(height);
        } else {
            tails[left] = height;
        }
    }

    return ans;
};

