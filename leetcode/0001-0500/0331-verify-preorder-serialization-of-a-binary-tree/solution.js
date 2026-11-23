
var isValidSerialization = function(preorder) {
    let slots = 1;

    const nodes = preorder.split(',');

    for (let node of nodes) {
        // No available slot for this node
        if (slots === 0) {
            return false;
        }

        // Consume one slot
        slots--;

        // Non-null node creates two child slots
        if (node !== '#') {
            slots += 2;
        }
    }

    // All slots must be filled
    return slots === 0;
};

