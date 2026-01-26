class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
def search_an_element(head, val):
    curr = head
    while curr is not None:
        if curr.data == val:
            return True
        curr = curr.next
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(search_an_element(head, 4))