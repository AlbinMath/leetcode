
var getStrongest = function(arr, k) {
    arr.sort((a, b) => a - b);
    const m = arr[Math.floor((arr.length - 1) / 2)];
    arr.sort((a, b) => {
        const diffA = Math.abs(a - m);
        const diffB = Math.abs(b - m);
        if (diffA !== diffB) {
            return diffB - diffA;
        }

        return b - a;
    });

    return arr.slice(0, k);
};

