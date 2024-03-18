# 2.Write a program to deal with real-world situations where Stack data structure is widely used
# Evaluation of expression:
# Stacks are used to evaluate expressions, especially in languages that use postfix or prefix notation. Operators and operands are pushed onto the stack, and operations are performed based on the LIFO principle.

def evaluateExpression(exp):
    stack=[]
    for char in exp.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            n1=stack.pop()
            n2=stack.pop()
            if char=='+':
                stack.append(n1+n2)
            elif char=='-':
                stack.append(n2-n1)
            elif char=='*':
                stack.append(n1*n2)
            elif char=='/':
                stack.append(n2/n1)


    return stack.pop()

exp="2 4 + 2 *"
result=evaluateExpression(exp)
print(result)

























