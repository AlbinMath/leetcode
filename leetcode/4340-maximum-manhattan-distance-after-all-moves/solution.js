
var maxDistance = function(moves) {
    let x = 0;
    let y = 0;
    let wildcards = 0;

    for (const move of moves) {
        if (move === 'U') {
            y++;
        } else if (move === 'D') {
            y--;
        } else if (move === 'R') {
            x++;
        } else if (move === 'L') {
            x--;
        } else {
            wildcards++;
        }
    }

    return Math.abs(x) + Math.abs(y) + wildcards;
};

