
var copyRandomList = function(head) {
    if (head === null) return null;

    const map = new Map();

    // Step 1: Create a copy of every node
    let current = head;

    while (current !== null) {
        map.set(current, new Node(current.val));
        current = current.next;
    }

    // Step 2: Connect next and random pointers
    current = head;

    while (current !== null) {
        const copy = map.get(current);

        copy.next = current.next
            ? map.get(current.next)
            : null;

        copy.random = current.random
            ? map.get(current.random)
            : null;

        current = current.next;
    }

    return map.get(head);
};

