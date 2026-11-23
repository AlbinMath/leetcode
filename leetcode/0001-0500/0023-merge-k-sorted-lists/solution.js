
var mergeKLists = function(lists) {
    if (lists.length === 0) {
        return null;
    }

    // Merge lists in pairs, doubling the interval each round
    for (let interval = 1; interval < lists.length; interval *= 2) {
        for (let i = 0; i + interval < lists.length; i += interval * 2) {
            lists[i] = mergeTwoLists(lists[i], lists[i + interval]);
        }
    }

    return lists[0];
};

function mergeTwoLists(list1, list2) {
    const dummy = new ListNode(0);
    let tail = dummy;

    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            tail.next = list1;
            list1 = list1.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
        }

        tail = tail.next;
    }

    // Attach whichever list still has nodes
    tail.next = list1 !== null ? list1 : list2;

    return dummy.next;
}

