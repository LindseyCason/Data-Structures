from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        #DLL to keep order, Dictonary to keep KV pair, Current Size and Limit
        self.order = DoublyLinkedList()
        self.storage = {} #ORDERED
        self.size=0
        self.limit=limit
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage: #self.storage IS the DICT
            node=self.storage[key]
            self.order.move_to_end(node)#MOST RECENTLY USED
            return node.value[1]#0 is they key 1 is the value, make sure you're returning value.
        else:
            return None


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        #lecture notes
        #Create node if key not found and move to front, increase size
        #Move node to front if key IS found because recently used
        #If full, remove last node from BOTH linked list AND dictionary
        if key in self.storage:
            node=self.storage[key] #This is a pointer to the key
            node.value=(key,value) #the value is the tuple for that key/-->updating
            self.order.add_to_tail(node) #makes it most recent
            return

        if self.size == self.limit:
            del self.storage[self.order.head.value[0]] #REMOVED FROM DICT
            self.order.remove_from_head() #REMOVE IT FROM DLL
            self.size -= 1

        self.order.add_to_tail((key,value)) #If size = 0 then add key,value TUPLE
        self.storage[key] =self.order.tail
        self.size += 1
