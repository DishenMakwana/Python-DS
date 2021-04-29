class Node():
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None

class Add():
    def __init__(self):
        print('Add class initialized')

    # Append a node to the linked list
    def append(self, data):
        node = Node(data)
        # Check if head node exists or not
        if self.head is None:
            self.head = self.last = node
            return
        # Set the node's previous to point to last node
        node.prev = self.last
        # Then set the last's next to point to the created node
        self.last.next = node
        # And finally make the created node the last node
        self.last = node

    # Add node to the start
    def add_to_start(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.last = node
            return
        # Set the current head's prev to point to the node
        self.head.prev = node
        # Set the node's next to point to the current head
        node.next = self.head
        # Set the node as the new head
        self.head = node

    # Insert after
    def insert_after(self, node, data):
        start = self.head
        # Loop through the list until the desired node is found
        while start.data is not node:
            start = start.next
        if start is None:
            print('Node with value {node_data} does not exist in the list')
            return False
        # Start now holds the node after which the new node needs to be inserted
        node = Node(data)
        # Link the created node with the start node and the node after the start node
        node.prev = start
        node.next = start.next
        # Link the node after the start node with the created node
        start.next.prev = node
        # Link the created node with the start node
        start.next = node

    # Insert before
    def insert_before(self, node, data):
        start = self.head
        # Loop through the list until the node is found
        while start.data is not node:
            start = start.next
        if start is None:
            print('Node with value {node} does not exist')
            return False
        # The start now holds the node before which the new node will be inserted
        node = Node(data)
        # Link the node to start and the node before the start
        node.next = start
        node.prev = start.prev
        # Link the created node and the node before the start
        start.prev.next = node
        # Link the start node and the created node
        start.prev = node

class Misc():
    def __init__(self):
        print('Misc class initialized')

    # Display list
    def display_list(self):
        if self.head is None:
            print('Cannot display: List is empty')
            return False
        temp = self.head
        print('List is as follows')
        while temp is not None:
            print(temp.data,' -> ')
            temp = temp.next
        print()   # Moves cursor to next line

    # Search for a given node
    def search(self, value):
        if self.head is None:
            print('Cannot search: List is empty')
            return False
        # Search starts here
        temp = self.head
        while temp is not None:
            if temp.data is value:
                print('Search Successful: Value {value} found')
                return True
            temp = temp.next
        # Search unsuccessful
        print('Search unsuccessful: Value {value} not found')
        return False
       
class Delete():
    def __init__(self):
        print('Delete class initialized')

    # Delete the head node
    def delete_head(self):
        if self.head is None:
            print('Cannot delete: List is empty')
            return False
        # Make the node next to the head as the new head
        new_head = self.head.next
        # Set the new_head.prev to None
        new_head.prev = None
        # Set the head as the new head
        self.head = new_head

    # Delete a given node
    def delete_given_node(self, node):
        if self.head is None:
            print('Cannot delete: List is empty')
            return False
        # Search starts here
        temp = self.head
        while temp:
            if temp.data is node:
                break
            temp = temp.next
        if temp is None:
            print('Node with value {node} does not exist')
            return False
        # Connect the node previous to temp and node after temp with each other
        prev_node = temp.prev
        next_node = temp.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
class Doubly(Add, Delete, Misc):
    def __init__(self):
        Delete.__init__(self)
        Add.__init__(self)
        Misc.__init__(self)
        self.head = self.last = None
        
doubly = Doubly()
# Operations on empty list
# doubly.search(5)
# doubly.delete_head()
# doubly.delete_given_node(5)
# doubly.display_list()

# Operations
for i in range(10):
    doubly.append(i)

# Add operations
doubly.display_list()
doubly.insert_after(5, 555)
doubly.insert_before(5, 444)
doubly.display_list()

# Search operations
doubly.search(5)
doubly.search(2)
doubly.search(10)
doubly.search(100)

# Delete Operations
doubly.display_list()
doubly.delete_head()
doubly.display_list()
doubly.delete_given_node(555)
doubly.delete_given_node(444)
doubly.delete_given_node(100)
doubly.display_list()
doubly.delete_head()
doubly.display_list()