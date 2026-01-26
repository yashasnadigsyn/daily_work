class Node:
    def __init__(self, data1):
        self.data = data1
        self.next = None
        
def length_of_ll(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
        
    return count

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
print("Length of Linked List:", length_of_ll(head))