"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?

#     def __len__(self):
#         pass

#     def push(self, value):
#         pass

#     def pop(self):
#         pass

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next  # The next node in the list
class LinkedList:
    def __init__(self):
        self.head: Node = None  # points to the first node in the list
        self.tail: Node = None  # Points to the last node in the list
        self.length = 0
    def __str__(self):
        pass
    def __len__(self):
        return self.length
    def add_to_tail(self, value):
        # Check if there's a tail
        # If there is no tail (empty list)
        if self.tail is None:
            # Create a new node
            new_tail = Node(value, None)
        #    Set self.head and self.tail to the new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail (general case):
        else:
            # Create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
            # Set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # Set self.tail to the new node
            self.tail = new_tail
        self.length += 1
    def remove_head(self):
        # If not head (empty list)
        if self.head is None:  # if self.head is None
            return None
        # List with one element:
        if self.head == self.tail:
            # Set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            # Set self.tail to None
            self.tail = None
            # Decrement length by 1
            self.length = self.length - 1
            return current_head.value
        # If head (General case):
        else:
            # 	Set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            #  Return current_head.value
            self.length = self.length - 1
            return current_head.value
    def remove_tail(self):
        # Remove Tail:
        if self.tail is None:
            return None
        # List of 1 element:
        if self.head == self.tail:
        # Save the current_tail.value
            current_tail = self.tail
        # Set self.tail to None
            self.tail = None
        # Set self.head to None
            self.head = None
            self.length = self.length - 1
            return current_tail.value
        # Check if it's there
        # General case:
        else:
        # Start at head and iterate to the next-to-last node
            current_node = self.head
        # Stop when current_node.next == self.tail
            while current_node.next != self.tail:
                current_node = current_node.next
            # Once we exit the while loop, current_node is pointing to the node right before self.tail
        # Save the current_tail value
            current_tail = self.tail
        # Set self.tail to current_node
            self.tail = current_node
        # Set current_node.next to None
            current_node.next = None
            self.length = self.length - 1
            return current_tail.value
    def add_to_head(self, value):
        # If no head / empty list:
        if self.head is None:
        # Create the new node with next = None
            new_node = Node(value, None)
        #  Set self.head = new node
            self.head = new_node
        # Set self.tail = new node
            self.tail = new_node
        # increment self.length
            self.length += 1
        else:
        # If head:
        # Create the new node
            new_node = Node(value, self.head)
        # New_node.next = self.head
        # Set self.head = new_node
            self.head = new_node
        # increment self.length
            self.length += 1
    def remove_at_index(self, index):
        # Remove at index i:
        # 0) Check that length > i. If not, return None
        if index >= self.length:
            return None
        if self.length == 1 and index == 0:
            target = self.head
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return target.value
        # Iterate through the loop i-1 times:
        prev_node = self.head
        for i in range(index - 1):
        # This will get us to prev_node points to the node before the target node
            prev_node = prev_node.next
        target = prev_node.next
        prev_node.next = target.next
        target.next = None
        self.length = self.length - 1
        return target.value


import time
# from singly_linked_list.singly_linked_list import LinkedList
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    def __len__(self):
        return len(self.storage)
    def push(self, value):
        self.storage.add_to_head(value)
    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.remove_head()
n = 100000
stack = Stack()
start = time.time()
for i in range(n):
    stack.push(i)
print("Pushing (to front): ", time.time() - start)
start = time.time()
for i in range(n):
    stack.pop()
print("Popping (from front): ", time.time() - start)





        # Remove Tail:
        # Check if it's there
        # General case:
        # Start at head and iterate to the next-to-last node
        # Stop when current_node.next == self.tail
        # Save the current_tail value
        # Set self.tail to current_node
        # Set current_node.next to None
        #
        # List of 1 element:
        # Save the current_tail.value
        # Set self.tail to None
        # Set self.head to None