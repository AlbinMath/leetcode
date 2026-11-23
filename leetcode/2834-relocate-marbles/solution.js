var relocateMarbles = function(nums, moveFrom, moveTo) {
    const occupied = new Set(nums);

    for (let i = 0; i < moveFrom.length; i++) {
        occupied.delete(moveFrom[i]);
        occupied.add(moveTo[i]);
    }

    return Array.from(occupied).sort((a, b) => a - b);
};
