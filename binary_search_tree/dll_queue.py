import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


#  * Should have the methods: `enqueue`, `dequeue`, and `len`.
#    * `enqueue` should add an item to the back of the queue.
#    * `dequeue` should remove and return an item from the front of the queue.
#    * `len` returns the number of items in the queue.

class Queue:
    def __init__(self):
        self.size=0
        self.storage=DoublyLinkedList()
        #THIS IS BRINGING IN EVERYTHING FROM DOUBLY LINKED LIST THAT WE MADE. WE CAN THEN USE THE METHODS WE WROTE TO ACCOMPLISH WHAT WE WANT WITH THE METHODS BELOW.

    def enqueue(self, value):
        #    * `enqueue` should add an item to the back of the queue.
        self.storage.add_to_tail(value) #CALLING ADD TO HEAD AND PASSING IN THE VALUE. ADD TO HEAD IN DLL WILL RUN AND ACCOMPLISH THIS TASK
        self.size +=1 #increment size

    def dequeue(self):
        #    * `dequeue` should remove and return an item from the front of the queue.
        #value = self.storage.head #WE DON'T NEED THIS HERE BECAUSE IT'S TAKEN CARE OF IN THE REMOVE FROM HEAD FUNCTION IN DLL, THIS CAUSES AN ERROR. JUST RETURN THE CODE AND IT WILL RETURN THE VALUE THAT IS RETURNED FROM THE FUNCTION CALLED FROM DLL.
        self.size -=1 #decrement size

        return self.storage.remove_from_head()

    def len(self):
        #    * `len` returns the number of items in the queue.
        return self.storage.length
