
var areNumbersAscending = function(s) {
    const words = s.split(" ");
    let prev = 0;

    for (const word of words) {
        if (!isNaN(word)) {
            const num = Number(word);

            if (num <= prev) {
                return false;
            }

            prev = num;
        }
    }

    return true;
};

