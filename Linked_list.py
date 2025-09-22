#Linked list code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)  # Create a new node 
        new_node.next = self.head  # Next for new node becomes the current head
        self.head = new_node  # Head now points to the new node

    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data,end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print()  # Ensures the output is followed by a new line   
    
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.insertAtBeginning(3)
    my_list.insertAtBeginning(7)
    my_list.insertAtBeginning(2)
    my_list.printList()