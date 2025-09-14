class LRUCache:

    def __init__(self, capacity: int):
        self.cacheMap = dict()
        self.cap = capacity
        self.linked_list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            node = self.cacheMap[key]
            self.linked_list.moveToTail(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            node = self.cacheMap[key]
            node.value = value
            self.linked_list.moveToTail(node)
        elif len(self.cacheMap.keys()) == self.cap:
            node = Node(value, key)
            removed = self.linked_list.removeLRU()
            self.linked_list.append(node)
            self.cacheMap[key] = node
            self.cacheMap.pop(removed.key)
        else:
            node = Node(value, key)
            self.cacheMap[key] = node
            self.linked_list.append(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, node):
        if self.tail == None:
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
    
    def moveToTail(self, node):        
        if node == self.tail:
            return

        if self.head == None or self.head == self.tail:
            return

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
            
        if node.next:
            node.next.prev = node.prev
        
        self.tail.next = node 
        node.prev = self.tail
        node.next = None
        self.tail = node

    def removeLRU(self):
        if self.head == None:
            return None
            
        removed_node = self.head
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        removed_node.next = None
        removed_node.prev = None
        
        return removed_node

class Node:
    def __init__(self, value, key):
        self.prev = None
        self.next = None
        self.value = value
        self.key = key

