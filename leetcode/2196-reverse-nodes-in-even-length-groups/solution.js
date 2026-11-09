
var reverseEvenLengthGroups = function(head) {
    let current = head;
    let groupSize = 1;
    let prevGroupTail = null;

    while (current) {
        // Find actual group length
        let count = 0;
        let temp = current;

        while (temp && count < groupSize) {
            count++;
            temp = temp.next;
        }

        // Reverse only even-length groups
        if (count % 2 === 0) {
            let prev = temp;
            let node = current;

            // Reverse current group
            for (let i = 0; i < count; i++) {
                let nextNode = node.next;
                node.next = prev;
                prev = node;
                node = nextNode;
            }

            // Connect previous group to reversed group
            if (prevGroupTail) {
                prevGroupTail.next = prev;
            } else {
                head = prev;
            }

            prevGroupTail = current;
            current = temp;

        } else {
            // Odd group: no reversal
            for (let i = 0; i < count; i++) {
                prevGroupTail = current;
                current = current.next;
            }
        }

        groupSize++;
    }

    return head;
};

