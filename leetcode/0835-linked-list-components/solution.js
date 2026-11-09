
var numComponents = function(head, nums) {
    // Store nums values in a Set
    let set = new Set(nums);

    let count = 0;
    let current = head;

    while (current) {
        // Start of a new component
        if (
            set.has(current.val) &&
            (!current.next || !set.has(current.next.val))
        ) {
            count++;
        }

        current = current.next;
    }

    return count;
};

