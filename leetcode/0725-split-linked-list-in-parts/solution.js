
var splitListToParts = function(head, k) {
    // Step 1: Count total nodes
    let length = 0;
    let current = head;

    while (current) {
        length++;
        current = current.next;
    }

    // Step 2: Calculate part sizes
    let size = Math.floor(length / k);
    let extra = length % k;

    let result = [];
    current = head;

    // Step 3: Split into k parts
    for (let i = 0; i < k; i++) {
        let partHead = current;
        let partSize = size + (i < extra ? 1 : 0);

        // Move to the end of the current part
        for (let j = 0; j < partSize - 1; j++) {
            if (current) {
                current = current.next;
            }
        }

        // Separate the current part
        if (current) {
            let nextPart = current.next;
            current.next = null;
            current = nextPart;
        }

        result.push(partHead);
    }

    return result;
};

