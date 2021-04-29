class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Add():
    def __init__(self):
        print('Add class initialized')

    # Append a node
    def append(self, data):
        if data is None:
            print('No data received')
            return
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = node

    # Add a node in beginning
    def push(self, data):
        if data is None:
            print('No data received')
            return
        node = Node(data)
        node.next = self.head
        self.head = node

    # Insert after a given node value
    def insert_after(self, insert_after_value=None, data=None):
        if insert_after_value is None or data is None:
            print('Missing arguments')
            return
        if self.head is None:
            print('List is empty')
            return 
        # Get the reference to the node after which the new node will be inserted
        start = self.head
        prev_node = None
        while start:
            if start.data == insert_after_value:
                prev_node = start
                break
            start = start.next
        # Check if the searched node exists or not
        if prev_node is None:
            print('Given node does not exist')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
      
class Misc():
    def __init__(self):
        print('Misc constructor called')

    # Display the list
    def display_list(self):
        start = self.head
        if start is None:
            print('No items in linked list')
            return
        print('Linked list is as follows: ')
        while (start):
            print(start.data, '-> ')
            start = start.next
        print()

    # Search for value
    def search(self, search_value=None):
        if search_value is None:
            print('Enter a search value and try again')
            return
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        while temp:
            if temp.data is search_value:
                print('Search successful:', search_value, ' found')
                return temp
            temp = temp.next

        print(search_value,' does not exist')
        return None
        
class Delete():
    def __init__(self):
        print('Delete class constructor')

    # Pretty easy, simply shift the head to the reference the next node
    def del_first_node(self):
        if self.head is None:
            print('Linked list is empty')
            return
        self.head = self.head.next

    # This piece of code run through the list and removes the reference to the last node from the node just before the last node
    def del_last_node(self):
        if self.head is None:
            print('List is empty')
            return
        temp = node_before_deleted_node = self.head
        while temp:
            node_before_deleted_node = temp
            temp = temp.next
        node_before_deleted_node.next = None

    def del_node_after(self, node=None):
        if self.head is None:
            print('List is empty')
            return
        if node is None:
            print('Enter a node value')
        temp = self.head
        while temp:
            if temp.data is node:
                temp.next = temp.next.next
                return
            temp = temp.next
        return 'Node not found'
        
# Singly linked list
class Singly(Add, Delete, Misc):
    def __init__(self):
        # Just for testing purposes, calling the base class constructors
        Add.__init__(self)
        Delete.__init__(self)
        Misc.__init__(self)
        # Initialize the head
        self.head = None
        
# Perform your operations here
singly = Singly()

# Empty list check
singly.display_list()
singly.search()
singly.insert_after()
singly.del_first_node()
singly.del_last_node()
singly.del_node_after()

# Adding data to list
for i in range(10):
    singly.append(i)

singly.display_list()

# Add operations
singly.push(550)
singly.insert_after(3, 44)
singly.append(69)
singly.display_list()

# Search
singly.search(50)
singly.search(5)
singly.search(9)

# Delete
singly.del_first_node()
singly.display_list()
singly.del_first_node()
singly.display_list()
singly.del_first_node()
singly.display_list()
singly.del_first_node()
singly.display_list()
singly.del_node_after(3)
singly.display_list()
singly.del_node_after(9)
singly.display_list()