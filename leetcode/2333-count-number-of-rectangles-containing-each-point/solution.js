
var countRectangles = function(rectangles, points) {
    const heights = Array.from({ length: 101 }, () => []);

    // Group rectangle lengths by height
    for (const [l, h] of rectangles) {
        heights[h].push(l);
    }

    // Sort lengths for binary search
    for (let h = 1; h <= 100; h++) {
        heights[h].sort((a, b) => a - b);
    }

    function lowerBound(arr, target) {
        let left = 0;
        let right = arr.length;

        while (left < right) {
            const mid = Math.floor((left + right) / 2);

            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }

    const result = [];

    for (const [x, y] of points) {
        let count = 0;

        // A containing rectangle must have height >= y
        for (let h = y; h <= 100; h++) {
            const arr = heights[h];
            const index = lowerBound(arr, x);

            // All lengths from index onward are >= x
            count += arr.length - index;
        }

        result.push(count);
    }

    return result;
};

