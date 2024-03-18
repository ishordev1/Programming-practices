class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printlist(h1):
    while h1:
        print(h1.data,end=" ")
        h1=h1.next

def sizeOfList(h1):
    count=0
    while h1:
        count=count+1
        h1=h1.next
    return count
def findmidPoint(h1,h2):
    if h1 is None and h2 is None:
        print("empty list")
        return
    h1Size=sizeOfList(h1)
    h2Size=sizeOfList(h2)
    h1Temp=h1
    h2Temp=h2
    if h1Size <h2Size:
        for i in range(0,h2Size-h1Size):
            h2Temp=h2Temp.next
    else:
        for i in range(0,h1Size-h2Size):
            h1Temp=h1Temp.next

    while h1Temp  and h2Temp is not None:
        if h1Temp==h2Temp:
            print(h1Temp.data)
            return
        else:
            h1Temp=h1Temp.next
            h2Temp=h2Temp.next

fn1=Node(5)
fn2=Node(15)
fn3=Node(25)
fn4=Node(35)
fn5=Node(45)
fn1.next=fn2
fn2.next=fn3
fn3.next=fn4
fn4.next=fn5

sn1=Node(10)
sn2=Node(20)
sn3=Node(20)
sn1.next=sn2
sn2.next=sn3
sn3.next=fn3

printlist(fn1)
print("\n")
printlist(sn1)
print("\n")
findmidPoint(fn1,sn1)