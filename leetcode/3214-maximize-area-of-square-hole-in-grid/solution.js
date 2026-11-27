
var maximizeSquareHoleArea = function(n, m, hBars, vBars) {
    const getMaxGap = function(bars) {
        bars.sort((a, b) => a - b);

        let maxConsecutive = 1;
        let currentConsecutive = 1;

        for (let i = 1; i < bars.length; i++) {
            if (bars[i] === bars[i - 1] + 1) {
                currentConsecutive++;
            } else {
                currentConsecutive = 1;
            }

            maxConsecutive = Math.max(
                maxConsecutive,
                currentConsecutive
            );
        }

        return maxConsecutive + 1;
    };

    const horizontalGap = getMaxGap(hBars);
    const verticalGap = getMaxGap(vBars);

    const side = Math.min(horizontalGap, verticalGap);

    return side * side;
};

