
var mergeNodes = function(head) {
    let current = head.next;
    let result = head;

    while (current) {
        let sum = 0;

        // Calculate sum between zeros
        while (current && current.val !== 0) {
            sum += current.val;
            current = current.next;
        }

        // Store sum in the result node
        result.val = sum;

        // Move to the next group
        if (current && current.next) {
            result.next = current;
            result = result.next;
        } else {
            result.next = null;
        }

        if (current) {
            current = current.next;
        }
    }

    return head;
};

