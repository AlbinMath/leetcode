
var reverseList = function(head) {
    let prev = null;
    let curr = head;

    while (curr !== null) {
        let nextNode = curr.next; // Save the next node
        curr.next = prev;         // Reverse the link
        prev = curr;              // Move prev forward
        curr = nextNode;          // Move curr forward
    }

    return prev;
};

