#Linked list code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

        print(type(self.head))

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the current head
        self.head = new_node  # Head now points to the new node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If the list is empty, make the new node the head
            return
        last = self.head 
        while last.next:  # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node  # Make the new node the next node of the last node
    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line   

    def search(self, value):
        current = self.head  # Start with the head of the list
        position = 0  # Counter to keep track of the position
        while current: # Traverse the list
            if current.data == value: # Compare the list's data to the search value
                return f"Value '{value}' found at position {position}" # Print the value if a match is found
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list" 

if __name__ == '__main__':
    llist = LinkedList()

    # Insert words at the beginning
    llist.insertAtBeginning('1')
    llist.insertAtBeginning('2')
    llist.insertAtBeginning('3')
    llist.insertAtBeginning('4')

    # Insert a word at the end
    llist.insertAtEnd('5')

    # Print the list
    llist.printList()
    print(llist.search('5'))  