# ⦁	Write a program for implementing a  MINSTACK  which should support operations like push, pop, overflow, underflow, display
# a.	Construct a stack of N-capacity
# b.	Push elements 
# c.	Pop elements
# d.	Top element 
# e.	Retrieve the min element from the stack


# class stack:
#   def __init__(self):
#     self.ele_stack=[]
    
    
#   def push(self,element):
#     self.ele_stack.append(element)
  
#   def pop(self):
#     if self.ele_stack:
#       self.ele_stack.pop()
#     else:
#       print("stack is empty")
      
      
#   def peek(self):
#     if self.ele_stack:
#       print(self.ele_stack[-1])
#     else:
#       print("stack is empty")
      
#   def size(self):
#     if self.ele_stack:
#       print(len(self.ele_stack))
#     else:
#       print("stack is empty")
    
#     def isEmpty(self):
#       if not self.ele_stack:
#         print("true")
#       else:
#         print("false")
        
    
#     # def get_Min(self):
#     #   if not self.ele_stack:
      
# obj=stack()
# obj.push(5)
# obj.push(10)
# obj.peek()
# print(obj.ele_stack)


# obj.pop()
# obj.pop()
# obj.pop()
# obj.pop() 


# Write a program for implementing a  MINSTACK  which should support operations like push, pop, overflow, underflow, display
class stack:
  def __init__(self):
    self.ele_stack=[]
    self.minStack=[]
    
    
  def push(self,element):
      self.ele_stack.append(element)
      if self.minStack:
        min_value=min(element,self.minStack[-1])
        self.minStack.append(min_value)
      else:
        self.minStack.append(element)
  
  
  def pop(self):
    if self.ele_stack:
      self.ele_stack.pop()
      self.minStack.pop()
    else:
      print("stack is empty")
      
      
  def peek(self):
    if self.ele_stack:
      print(self.ele_stack[-1])
    else:
      print("stack is empty")
      
  def size(self):
    if self.ele_stack:
      print(len(self.ele_stack))
    else:
      print("stack is empty")
    
    def isEmpty(self):
      if not self.ele_stack:
        print("true")
      else:
        print("false")
        
    
  def get_Min(self):
    if self.minStack:
       return self.minStack[-1]
    else:
        return 0
        
      
obj=stack()
obj.push(5)
obj.push(-2)
obj.push(10)
obj.push(5)
obj.peek()
print(obj.ele_stack)

obj.push(-1)
 

print("this is min value",obj.get_Min())

      
      
      
      
      