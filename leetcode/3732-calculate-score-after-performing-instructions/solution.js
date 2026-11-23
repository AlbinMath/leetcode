var calculateScore = function(instructions, values) {
    const n = instructions.length;
    const visited = new Uint8Array(n);
    let score = 0;
    let i = 0;

    while (i >= 0 && i < n && !visited[i]) {
        visited[i] = 1;
        if (instructions[i] === "add") {
            score += values[i];
            i++;
        } else {
            i += values[i];
        }
    }

    return score;
};
