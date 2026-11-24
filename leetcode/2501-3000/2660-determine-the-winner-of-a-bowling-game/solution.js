var isWinner = function(player1, player2) {
    const calcScore = (pins) => {
        let total = 0;
        for (let i = 0; i < pins.length; i++) {
            const hasStrikeBonus = (i >= 1 && pins[i - 1] === 10) || (i >= 2 && pins[i - 2] === 10);
            total += hasStrikeBonus ? 2 * pins[i] : pins[i];
        }
        return total;
    };

    const score1 = calcScore(player1);
    const score2 = calcScore(player2);

    if (score1 > score2) return 1;
    if (score2 > score1) return 2;
    return 0;
};
