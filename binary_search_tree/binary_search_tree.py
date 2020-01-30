import sys
from dll_queue import Queue
from dll_stack import Stack

# ### Binary Search Trees
# * Should have the methods `insert`, `contains`, `get_max`.
#   * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
#   * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
#   * `get_max` returns the maximum value in the binary search tree.
#   * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 

# ![Image of Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)

class BinarySearchTree:
    def __init__(self, value):
        self.value = value #because we are looking at an instance of a binary search tree, self.value will be the root.
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #If the value is less than the root....
        if value < self.value:
            if not self.left: #and there is no left assigned...
                self.left=BinarySearchTree(value) #assign a new node with the value to the left of the root.
            else:
                self.left.insert(value) #This moves us down to the left node and calls insert again and will create a node of the value once it gets to a point where there is no left child
        else:
            if not self.right:
                self.right=BinarySearchTree(value)
            else:
                self.right.insert(value)

        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:#move left and run code until you return something
            if target == self.left.value: #return true
                return True
            elif self.left.left == None: #if no left and no match, return False
                return False
        if target > self.value:#move right and return code until you return something
            if target == self.right.value:#move right
                return True
            elif self.right.right == None: #if no more rights and no match, return false
                return False
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right: #if there is no self.right just return where your current value (this could be 3 loops down the line), greater numbers will be to the right. When the rights run out, you've found your largest number
            return self.value
        elif self.right: #otherwise, if there is a right, call the function with the new value and repeat until there are no more rights.
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)#initial call

        if self.left:
            self.left.for_each(cb)#if we can go left go left and run for each passing in cb
        if self.right:
            self.right.for_each(cb)#if we can go right go right and run for each passing in cb

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        curr=node# set current to current node
        if curr.left: #if current node has a left child
            self.in_order_print(curr.left) #recall func using left child.
        print(curr.value)#this is proper placement
        if curr.right:
            self.in_order_print(curr.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q=Queue()
        q.enqueue(node)#adding initial node to Queue
        while q.len() > 0: #Until the Que is empty
            pop=q.dequeue() #To remove from Queue and proceed to add it's children in code below
            print(pop.value) #print the value that we popped off/out of the queue
            if pop.left: #If the popped value has a left node(A CHILD, ADD THE CHILDREN TO THE QUEUE)
                q.enqueue(pop.left)
            if pop.right: #If the popped value has a right node(A CHILD, ADD THE CHILDREN TO THE QUEUE)
                q.enqueue(pop.right)
                #Since children have been added the process will repeat in the while loop until no children can be added

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        curr=node
        s=Stack()
        s.push(curr) #pushes node to stack
        while s.len() > 0: #Until the stack is empty
            pop=s.pop()
            print(pop.value) #print the value of the popped item
            if pop.right: #if popped item has children, add them to the stack
                s.push(pop.right)
            if pop.left:
                s.push(pop.left)
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
