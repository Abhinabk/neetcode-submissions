class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:

    def __init__(self):
        self.arr  = [Node(-1,-1) for i in range (10**4)]       

    def put(self, key: int, value: int) -> None:
        idx = key%10**4
        head = self.arr[idx]
        curr = head.next
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        new_node = Node(key,value)
        new_node.next = head.next
        head.next = new_node
        return

    def get(self, key: int) -> int:
        idx = key%10**4
        head = self.arr[idx]
        curr = head.next
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return -1


    def remove(self, key: int) -> None:
        idx = key%10**4
        prev= self.arr[idx]
        curr = prev.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)