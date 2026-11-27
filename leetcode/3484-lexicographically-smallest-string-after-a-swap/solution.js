
var getSmallestString = function(s) {
    const arr = s.split('');

    for (let i = 0; i < arr.length - 1; i++) {
        const a = Number(arr[i]);
        const b = Number(arr[i + 1]);
        if (a % 2 === b % 2 && a > b) {
            [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
            break;
        }
    }

    return arr.join('');
};

