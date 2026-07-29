class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyHashSet:

    def __init__(self):
        self.arr = [Node(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        idx = key % 10**4
        head = self.arr[idx]
        curr = head.next

        while curr:
            if curr.value == key:
                return
            curr = curr.next

        new_node = Node(key)
        new_node.next = head.next
        head.next  = new_node

    def remove(self, key: int) -> None:
        idx = key % 10**4
        prev = self.arr[idx]
        curr = prev.next
        while curr:
            if curr.value == key:
                prev.next = curr.next
                return
            curr = curr.next
        return

    def contains(self, key: int) -> bool:
        idx = key % 10**4
        head = self.arr[idx]
        curr = head.next

        while curr:
            if curr.value == key:
                return True
            curr = curr.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)