"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    def __len__(self):
        return self.length
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None) #FIRST WE NEED TO MAKE A NODE BY WRAPPING VALUE IN THE LISTNODE CLASS
        self.length += 1 #THEN WE ADD TO THE LENGTH
        if not self.head and not self.tail: #IF THERE IS NO HEAD AND NO TAIL(FALSE), ASSIGN IT TO YOUR NEW NODE
            self.head = new_node
            self.tail = new_node
        else: #OTHERWISE 
            new_node.next = self.head #Assign the NEXT of the new node you added to the current self.head, self.head will NOW be new node and OLD self.head will be in second place(head.next)
            self.head.prev = new_node #This is setting the OLD self.head to have a prev now of new node. Originally it wouldn't have a prev because it was the head but since it's now in second place(in head.next position) the prev position is assigned to new node.
            self.head = new_node #assigning self.head to the new node. NOTICE this is opposite from the first statement in the else.
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value #SETTING VALUE VAR TO THE VALUE IN THE SELF.HEAD POSITION, WE WANT TO DO THIS BEFORE WE DELETE IT SO WE HAVE SOMETHING TO RETURN
        self.delete(self.head)#USING THE DELETE METHOD ABOVE, DELETE THE HEAD AND RETURN THE VALUE OF THE ITEM WE DELETED(WHICH WE CAN DO BECAUSE WE STORED THAT VALUE IN THE VAR VALUE)
        return value
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)#ANYTIME YOU'RE ADDING YOU MUST WRAP IT IN A NODE, THAT'S WHAT THIS IS DOING
        self.length += 1 #ALWAYS ADD TO THE LENGTH
        if not self.head and not self.tail: #IF THERE IS NO HEAD AND NO TAIL, ASSIGN THOSE TO NEW NODE
            self.head = new_node
            self.tail = new_node
        else: #OTHERWISE, IF IT'S NOT THE ONLY NODE IN THE DLL SINCE WE'RE ADDING TO TAIL, SET THE PREVIOUS OF THE NEW NODE TO THE OLD SELF.TAIL
            new_node.prev = self.tail
            self.tail.next = new_node #SET THE NEXT NODE AFTER THE OLD TAIL TO THE NEW NODE.
            self.tail = new_node#SET THE TAIL TO THE NEW NODE. WE'RE NOW REORGANIZED
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value #SET VAR VALUE TO THE VALUE OF THE NODE IN THE TAIL POSITION
        self.delete(self.tail) #DELETE THE NODE IN TAIL POSITION
        return value#RETURN VAR VALUE
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        value = node.value #SET VAR VALUE TO THE VALUE OF THE SINGLE NODE PASSED IN, WHICH IS WHAT WE WANT TO MOVE TO THE FRONT HERE.
        self.delete(node)#FIND THE NODE AND DELETE IT FROM THE LIST
        self.add_to_head(value)#RE-ADD THE NODE TO THE HEAD
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value #SET VALUE TO THE VALUE OF THE NODE THAT WE PASSED IN WHICH IS THE ONE WE WANT TO MOVE TO THE END
        self.delete(node) #FIND AND DELETE THAT NODE
        self.add_to_tail(value)#RE-ADD THIS NODE TO THE TAIL OF THE NODE LIST
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1 #FOR DELETE, REMOVE 1 FROM LENGTH.
        # If LL is empty
        if not self.head and not self.tail: #IF THERE IS NO HEAD AND NO TAIL THE LIST IS EMPTY SO RETURN
            # TODO: Error handling
            return
        # If head and tail
        if self.head == self.tail: #IF THE HEAD AND THE TAIL ARE THE SAME NODE, ASSIGN HEAD AND TAIL TO NONE. EFFECTIVELY DELETING
            self.head = None
            self.tail = None
        # if head
        elif self.head == node:#IF THE NODE PASSED IN IS == TO THE HEAD, REASSIGN THE HEAD POSITION TO HEAD.NEXT(MOVE BACK) AND THEN DELETE THE NODE.
            self.head = self.head.next
            node.delete()
        # if tail
        elif self.tail == node:
            self.tail = self.tail.prev#IF THE NODE PASSED IN IS == TO TAIL, REASSIGN THE TAIL POSITION TO TAIL.PREV AND THEN DELETE THE NODE.
            node.delete()
        # otherwise
        else:
            node.delete() #OTHERWISE DELETE THE NODE
            node.prev=node.next.prev#this closes the gap if removed from the middle.
            node.next=node.prev.next #this closes the gap
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None: #if there is no head, return none (empty list)
            return None
        max_value = self.head.value #SET VAR MAX VALUE TO THE VALUE OF THE NODE AT THE HEAD POSITION
        current = self.head #SET VAR CURRENT TO THE CURRENT SELF.HEAD NODE
        while current:#WHILE CURRENT EXISTS, MOVE DOWN THE LIST ONE AT A TIME....
            if current.value > max_value: #if the current value per loop is greater than the VALUE of the head(static) then assign max_value to the current value we're on in that loop.
                max_value = current.value
            current = current.next #MOVE THE LOOP DOWN THE LINE BY ASSIGNING CURRENT(THE HEAD POSITION) TO THE VALUE OF THE NUMBER AFTER IT FOR COMPARISON
        return max_value #WHEN THERE ARE NO MORE SWITCHES TO BE MADE, RETURN THE MAX VALUE IN THE LIST