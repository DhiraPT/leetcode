class ListNode:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node = {}

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node, prev_node):
        node.prev = prev_node
        node.next = prev_node.next
        prev_node.next.prev = node
        prev_node.next = node

    def inc(self, key: str) -> None:
        if key not in self.key_node:
            if self.head.next.count != 1:
                self._append(ListNode(1), self.head)
            self.head.next.keys.add(key)
            self.key_node[key] = self.head.next
        else:
            curr_node = self.key_node[key]
            next_node = curr_node.next
            if next_node.count != curr_node.count + 1:
                next_node = ListNode(curr_node.count + 1)
                self._append(next_node, curr_node)
            next_node.keys.add(key)
            curr_node.keys.remove(key)
            self.key_node[key] = next_node

            if not curr_node.keys and curr_node.count != 0:
                self._remove(curr_node)

    def dec(self, key: str) -> None:
        curr_node = self.key_node[key]
        if curr_node.count == 1:
            curr_node.keys.remove(key)
            del self.key_node[key]
        else:
            prev_node = curr_node.prev
            if prev_node.count != curr_node.count - 1:
                prev_node = ListNode(curr_node.count - 1)
                self._append(prev_node, curr_node.prev)
            prev_node.keys.add(key)
            curr_node.keys.remove(key)
            self.key_node[key] = prev_node

        if not curr_node.keys and curr_node.count != 0:
            self._remove(curr_node)

    def getMaxKey(self) -> str:
        if self.tail.prev.count == 0:
            return ''
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next.count == 0:
            return ''
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()