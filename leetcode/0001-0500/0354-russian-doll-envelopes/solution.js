var maxEnvelopes = function(envelopes) {
    envelopes.sort((a, b) => {
        if (a[0] === b[0]) {
            return b[1] - a[1];
        }
        return a[0] - b[0];
    });

    const tails = [];

    for (const envelope of envelopes) {
        const height = envelope[1];
        let left = 0;
        let right = tails.length;

        while (left < right) {
            const mid = Math.floor((left + right) / 2);

            if (tails[mid] < height) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        tails[left] = height;
    }

    return tails.length;
};
