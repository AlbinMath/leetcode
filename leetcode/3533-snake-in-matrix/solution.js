var finalPositionOfSnake = function(n, commands) {
    let pos = 0;

    for (const cmd of commands) {
        if (cmd === "UP") pos -= n;
        else if (cmd === "DOWN") pos += n;
        else if (cmd === "LEFT") pos -= 1;
        else pos += 1;
    }

    return pos;
};
