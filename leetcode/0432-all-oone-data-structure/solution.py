class Node:
    __slots__ = ("cnt", "keys", "prev", "next")
    def __init__(self, cnt=0):
        self.cnt = cnt
        self.keys = set()
        self.prev = self.next = None

class AllOne:
    def __init__(self):
        self.head = Node(0)   # sentinel, count 0
        self.tail = Node(-1)  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.where = {}       # key -> Node

    def _insert_after(self, node, cnt):
        new = Node(cnt)
        new.prev, new.next = node, node.next
        node.next.prev = new
        node.next = new
        return new

    def _remove_if_empty(self, node):
        if node is not self.head and not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        cur = self.where.get(key, self.head)
        nxt = cur.next
        if nxt is self.tail or nxt.cnt != cur.cnt + 1:
            nxt = self._insert_after(cur, cur.cnt + 1)
        nxt.keys.add(key)
        self.where[key] = nxt
        if cur is not self.head:
            cur.keys.discard(key)
            self._remove_if_empty(cur)

    def dec(self, key: str) -> None:
        cur = self.where[key]
        cur.keys.discard(key)
        if cur.cnt == 1:
            del self.where[key]
        else:
            prv = cur.prev
            if prv is self.head or prv.cnt != cur.cnt - 1:
                prv = self._insert_after(cur.prev, cur.cnt - 1)
            prv.keys.add(key)
            self.where[key] = prv
        self._remove_if_empty(cur)

    def getMaxKey(self) -> str:
        node = self.tail.prev
        if node is self.head:
            return ""
        return next(iter(node.keys))

    def getMinKey(self) -> str:
        node = self.head.next
        if node is self.tail:
            return ""
        return next(iter(node.keys))
