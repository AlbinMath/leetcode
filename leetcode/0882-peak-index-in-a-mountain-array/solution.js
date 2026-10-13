var peakIndexInMountainArray = function(arr) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (arr[mid] < arr[mid + 1]) {
            // Still climbing; peak is to the right
            left = mid + 1;
        } else {
            // Descending or at the peak
            right = mid;
        }
    }

    return left;
};
