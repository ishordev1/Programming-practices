#--------------------------------------Question No:1----------------------------
# class st:
#     def __init__(self):
#         self.stack=[]
#         self.minStack=[]
     
#     def push(self,data):
#         self.stack.append(data)
#         if not self.minStack:
#             self.minStack.append(data)
#         else:
#             m=min(self.stack[-1],self.minStack[-1])
#             self.minStack.append(m)

#     def pop(self):
#         if self.stack:
#             self.stack.pop()
#             self.minStack.pop()
#         else:
#             print("stack is empty.")

    
#     def peek(self):
#         print("total stack:",self.stack)
#         print("total minStack:",self.minStack)
#         if self.stack:
#             print(self.stack[-1])
#         else:
#             print("stack is empty")
    

#     def stackMinValue(self):
#         if self.minStack:
#             print(self.minStack[-1])
#         else:
#             print("stack is empty.")
        

# obj=st()
# obj.push(5)
# obj.push(8)
# obj.push(1)
# obj.push(3)
# obj.peek()
# obj.pop()
# obj.pop()
# obj.stackMinValue()

#---------------------------------Question No:2-------------------------------

# 2.Write a program to deal with real-world situations where Stack data structure is widely used
# Evaluation of expression:
# Stacks are used to evaluate expressions, especially in languages that use postfix or prefix notation. Operators and operands are pushed onto the stack, and operations are performed based on the LIFO principle.

# #Post Fix
# def evaluateExpression(exp):
#     stack=[]
#     for char in exp.split(" "):
#         if char.isdigit():
#             stack.append(int(char))
#         else:
#             n1=stack.pop()
#             n2=stack.pop()
#             if char=='+':
#                 stack.append(n1+n2)
#             elif char=='-':
#                 stack.append(n2-n1)
#             elif char=='*':
#                 stack.append(n1*n2)
#             elif char=='/':
#                 stack.append(n2/n1)
#     return stack.pop()
# exp="2 4 + 2 *"
# result=evaluateExpression(exp)
# print(result)

##Prefix ex
# def evaluateExpression(exp):
#     stack = []
#     for char in exp.split()[::-1]:
#         if char.isdigit():
#             stack.append(int(char))
#         else:
#             n1 = stack.pop()
#             n2 = stack.pop()
#             if char == '+':
#                 stack.append(n1 + n2)
#             elif char == '-':
#                 stack.append(n1 - n2)  
#             elif char == '*':
#                 stack.append(n1 * n2)
#             elif char == '/':
#                 stack.append(n1 / n2)  
#     return stack.pop()

# exp = "* + 4 2 2"
# result = evaluateExpression(exp)
# print(result)

#---------------------------------Question No:7-------------------------------

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class linkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
    
#     def insert(self,data):
#         temp=Node(data)
#         if self.head is None:
#             self.head=temp
#             self.tail=temp
#         else:
#             self.tail.next=temp
#             self.tail=self.tail.next
    
#     def traversal(self):
#         temp=self.head
#         if temp is None:
#             print("linked list is empty")
        
#         while temp:
#             print(temp.data, end=" ")
#             temp=temp.next
#         print("\n")


#     def mearge2LinkedList(self,h1,h2):
#         if h1 is None and h2 is None:
#             return None
#         if h1 is None:
#             return h2
#         if h2 is None:
#             return h1
        
#         mg=None
#         temp=None
#         while h1 is not None and h2 is not None:
#             if h1.data<h2.data:
#                 if mg is None:
#                     mg=h1
#                     temp=h1
#                 else:
#                     temp.next=h1
#                     temp=temp.next
#                 h1=h1.next
#             else:
#                 if mg is None:
#                     mg=h2
#                     temp=h2
#                 else:
#                     temp.next=h2
#                     temp=temp.next
#                 h2=h2.next
            
#             if h1 is not None:
#                 temp.next=h1
#             if h2 is not None:
#                 temp.next=h2
#         return mg

# obj=linkedList()
# obj.insert(5)
# obj.insert(15)
# obj.insert(25)
# obj.insert(35)
# obj.traversal()

# obj2=linkedList()
# obj2.insert(10)
# obj2.insert(20)
# obj2.insert(30)
# obj2.insert(40)
# obj2.traversal()

# obj3=linkedList()
# mglist=obj3.mearge2LinkedList(obj.head,obj2.head)
# while mglist is not None:
#     print(mglist.data,end=" ")
#     mglist=mglist.next


#---------------------------------Question No:8-------------------------------
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def printlist(h1):
#     while h1:
#         print(h1.data,end=" ")
#         h1=h1.next

# def sizeOfList(h1):
#     count=0
#     while h1:
#         count=count+1
#         h1=h1.next
#     return count
# def findmidPoint(h1,h2):
#     if h1 is None and h2 is None:
#         print("empty list")
#         return
#     h1Size=sizeOfList(h1)
#     h2Size=sizeOfList(h2)
#     h1Temp=h1
#     h2Temp=h2
#     if h1Size <h2Size:
#         for i in range(0,h2Size-h1Size):
#             h2Temp=h2Temp.next
#     else:
#         for i in range(0,h1Size-h2Size):
#             h1Temp=h1Temp.next

#     while h1Temp  and h2Temp is not None:
#         if h1Temp==h2Temp:
#             print(h1Temp.data)
#             return
#         else:
#             h1Temp=h1Temp.next
#             h2Temp=h2Temp.next

# fn1=Node(5)
# fn2=Node(15)
# fn3=Node(25)
# fn4=Node(35)
# fn5=Node(45)
# fn1.next=fn2
# fn2.next=fn3
# fn3.next=fn4
# fn4.next=fn5



# sn1=Node(10)
# sn2=Node(20)
# sn3=Node(20)
# sn1.next=sn2
# sn2.next=sn3
# sn3.next=fn3

# printlist(fn1)
# print("\n")
# printlist(sn1)
# print("\n")
# findmidPoint(fn1,sn1)


# Python program to swap the elements of linked list pairwise

class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to pairwise swap elements of a linked list
    def pairwiseSwap(self):
        temp = self.head
 
        # There are no nodes in linked list
        if temp is None:
            return
 
        # Traverse furthethr only if there are at least two
        # left
        while(temp and temp.next):
 
            # If both nodes are same,
            # no need to swap data
            if(temp.data != temp.next.data):
 
                # Swap data of node with its next node's data
                temp.data, temp.next.data = temp.next.data, temp.data
 
            # Move temp by 2 to the next pair
            temp = temp.next.next
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next
 
 
# Driver program
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
 
print ("Linked list before calling pairWiseSwap() ")
llist.printList()
 
llist.pairwiseSwap()
 
print ("\nLinked list after calling pairWiseSwap()")
llist.printList()








