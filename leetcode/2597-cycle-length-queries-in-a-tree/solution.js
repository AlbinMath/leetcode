
var cycleLengthQueries = function(n, queries) {
    const answer = [];

    for (const [a, b] of queries) {
        let x = a;
        let y = b;
        let length = 1;

        while (x !== y) {
            if (x > y) {
                x = Math.floor(x / 2);
            } else {
                y = Math.floor(y / 2);
            }

            length++;
        }

        answer.push(length);
    }

    return answer;
};

