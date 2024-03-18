
class Node:
    def __init__(self, val=None):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.temp = self.head

    def insertAtTail(self, n):
        if self.head.data == None:
            self.head = n
            self.temp = n
        else:
            self.temp.next = n
            self.temp = n

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data,end=" ")
            temp = temp.next


class Merge:
    def mergedHead(self, head1, head2):
        if (head1 ==None and head2==None):
            return None

        if head1 == None:
            return head2

        if head2 == None:
            return head1

        merged_head = None
        temp = None

        while head1 is not None and head2 is not None:
            if head1.data < head2.data:
                if merged_head is None:
                    merged_head = head1
                    temp = head1
                else:
                    temp.next = head1
                    temp = temp.next
                head1 = head1.next
            else:
                if merged_head is None:
                    merged_head = head2
                    temp = head2
                else:
                    temp.next = head2
                    temp = temp.next
                head2 = head2.next

        if head1 is not None:
            temp.next = head1
        elif head2 is not None:
            temp.next = head2

        return merged_head


n1 = Node(1)
n2 = Node(15)
n3 = Node(55)
l = LinkedList()
l.insertAtTail(n1)
l.insertAtTail(n2)
l.insertAtTail(n3)
print("\nlist 1")
l.printList()

l2 = LinkedList()
l2.insertAtTail(Node(10))
l2.insertAtTail(Node(50))
l2.insertAtTail(Node(60))
l2.insertAtTail(Node(6))
print("\nlist 2")
l2.printList()

m = Merge()
merged_head = m.mergedHead(l.head, l2.head)

print("\nMerged List")
while merged_head is not None:
    print(merged_head.data,end=" ")
    merged_head = merged_head.next
