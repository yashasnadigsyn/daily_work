class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def insertathead(head, new_data):
    new_node = Node(new_data, head)
    return new_node

def printList(head):
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == '__main__':
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    print("Original list: ")
    printList(head)
    
    head = insertathead(head, 1)
    printList(head)