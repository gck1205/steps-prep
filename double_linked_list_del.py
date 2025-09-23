#Node structure for the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#Function to Delete at Beginning
def del_head(head): 
    # If empty, return None
    if head is None:
        return None
    # Move head to the next node
    head = head.next
    # Set prev of the new head
    if head is not None:
        head.prev = None
    # Return new head
    return head

#Function to Delete from the End
def del_last(head):
    # If empty or contains single element, return None
    if (head is None) or (head.next is None):
        return None
    #Else travers the list to find the last element
    curr = head
    while curr.next is not None:
        curr = curr.next
    #Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = None
    #Return the head
    return head

#Function to Delete from Specific Position
def del_pos(head, pos):
    # If empty, return None
    if head is None:
        return None
    #Else traverse to the specific node
    curr = head
    for i in range(1, pos):
        if curr is None:
            return head
        curr = curr.next

    # If the position is out of range
    if curr is None:
        return head
    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = curr.next
    # Update the next node's prev pointer
    if curr.next is not None:
        curr.next.prev = curr.prev

    # If the node to be deleted is the head node
    if head == curr:
        head = curr.next
    #Return the head
    return head 

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()
    

if __name__ == "__main__":
    #Initialize
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    #Link the nodes
    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = fourth
    fourth.prev = third
    fourth.next = fifth
    fifth.prev = fourth

    print("Original Linked List: ", end="")
    print_list(head)
    print("After Deletion at the beginning: ", end="")
    head = del_head(head)
    print_list(head)
    print("After Deletion at the end: ", end="")
    head = del_last(head)
    print_list(head)
    print("After Deletion at the position 2: ", end="")
    pos = 2
    head = del_pos(head, pos)
    print_list(head)