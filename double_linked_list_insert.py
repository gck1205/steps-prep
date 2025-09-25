#Code for double linked list implementation in Python
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLinkedList:
      def __init__(self):
           self.head=None
           self.prev=None
           self.next=None

def insertBegin(head, data):
    #Create a new node
    new_node = Node(data)
    new_node.next=head
    head.prev= new_node
    
    return new_node

def insert_end(head, data):
    #Create a new node
    new_node = Node(data)
    #If the list is empty, set the new node as the head
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        # Set the next of the last node to the new node
        curr.next = new_node
        # Set the prev of the new node to the last node
        new_node.prev = curr
    return head

def insert_at_position(head, pos, data):
    #Create a new node
    new_node = Node(data)
    if pos ==1:#Insert at the beginning
        new_node.next = head
        if head is not None:    #If the list is not empty set the prev of head to new node
            head.prev = new_node
        return new_node #Return the new node as the head of the linked list
    
    #Traverse the list to find the position
    curr = head
    for _ in range(1, pos-1):
        if curr is None:
            print("Position is out of bounds.")
            return head
        curr = curr.next
    #If the current position is out of bound
    if curr is None:
        print("Position is out of bounds.")
        return head
    #Else:
    new_node.prev = curr    # Set the prev of new node to curr
    new_node.next = curr.next   # Set the next of new node to next of curr
    curr.next = new_node# Update the next of current node to new node
    # If the new node is not the last node, update prev of next node to new node
    if new_node.next is not None:
        new_node.next.prev = new_node
    
    return head

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    head = Node(2)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List:", end=' ')
    printList(head)

    # Insert a new node at the front of the list
    head = insertBegin(head, 1)
    # Print the updated list
    print("After inserting Node 1 at the front:", end=' ')
    printList(head)

    # Insert a new node with data 6 at the end
    print("After inserting Node 6 at the end: ", end="")
    data = 6
    head = insert_end(head, data)
    # Print the updated list
    printList(head)

    # Insert a new node with data 5 at the position 5
    print("After inserting Node 5 at the position 5: ", end="")
    data = 5
    pos = 5
    head = insert_at_position(head, pos, data)
    # Print the updated list
    printList(head)