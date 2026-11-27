
var minOperations = function(s1, s2) {
    const n = s1.length;

    let additions = 0;
    let removalCost = 0;
    let i = 0;

    for (let j = 0; j < n; j++) {
        if (s1[j] === '0' && s2[j] === '1') {
            additions++;
        }
    }

    while (i < n) {
        if (s1[i] === '1' && s2[i] === '0') {
            let len = 0;

            while (
                i < n &&
                s1[i] === '1' &&
                s2[i] === '0'
            ) {
                len++;
                i++;
            }

            removalCost += Math.floor(len / 2);

            if (len % 2 === 1) {
                removalCost += 2;
            }
        } else {
            i++;
        }
    }

    if (n === 1 && removalCost > 0) {
        return -1;
    }

    return additions + removalCost;
};

