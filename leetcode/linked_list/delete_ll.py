class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
def delete_tail(head):
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    
    curr.next = None
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

head = delete_tail(head)
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next