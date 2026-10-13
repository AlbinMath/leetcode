
var mostFrequentPrime = function(mat) {
    const m = mat.length;
    const n = mat[0].length;
    const freq = new Map();

    const directions = [
        [0, 1],   // East
        [1, 1],   // South-east
        [1, 0],   // South
        [1, -1],  // South-west
        [0, -1],  // West
        [-1, -1], // North-west
        [-1, 0],  // North
        [-1, 1]   // North-east
    ];

    const isPrime = (num) => {
        if (num < 2) return false;
        if (num === 2) return true;
        if (num % 2 === 0) return false;

        for (let i = 3; i * i <= num; i += 2) {
            if (num % i === 0) return false;
        }

        return true;
    };

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            for (const [dr, dc] of directions) {
                let row = r;
                let col = c;
                let num = 0;

                while (
                    row >= 0 && row < m &&
                    col >= 0 && col < n
                ) {
                    num = num * 10 + mat[row][col];

                    if (num > 10 && isPrime(num)) {
                        freq.set(num, (freq.get(num) || 0) + 1);
                    }

                    row += dr;
                    col += dc;
                }
            }
        }
    }

    let answer = -1;
    let maxFrequency = 0;

    for (const [prime, count] of freq) {
        if (
            count > maxFrequency ||
            (count === maxFrequency && prime > answer)
        ) {
            answer = prime;
            maxFrequency = count;
        }
    }

    return answer;
};

