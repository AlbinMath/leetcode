var hIndex = function(citations) {
    let left = 0;
    let right = citations.length - 1;
    const n = citations.length;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const papers = n - mid;

        if (citations[mid] >= papers) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    return n - left;
};
