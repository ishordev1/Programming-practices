import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='root',
    database='mydatabase'                         
     )
myc=mydb.cursor()

def insertData():
    print("Enter you name:")
    name=input()
    print("Enter you address:")
    address=input()
    myc.execute(f"insert into customer values('{name}','{address}')")
    mydb.commit()
    print("data added successfully.\n")

def update():
    print("Enter you name which you want to update:")
    name=input()
    # myc.execute(f"select from customer where name='{name}'")
    # my=myc.fetchone()
    # if my:
        # print('please enter correct details:')
    # else:
        # print(f"sorry {name} not found.")

    print("Enter your New name:")
    newName=input()

    print("Enter your New address:")
    newAddress=input()
    myc.execute(f"update customer set name='{newName}',address='{newAddress}' where name='{name}'")
    mydb.commit()
    print("data updated successfully.\n")


def delete():
    print("Enter you name which you wanat to delete:")
    name=input()

    myc.execute(f"delete from customer where name={name}")
    mydb.commit()
    print("delete successfully.\n")

def showAll():
    myc.execute("select *from customer")
    my=myc.fetchall()
    for x in my:
        print(x)

while True:
    print("-----------------------****************----------------------")
    print("Enter operation no:")
    print("1 for insert:")
    print('2 for update:')
    print("3 for delete:")
    print('4 for show all data:')
    print('5 to exit:')
    print("-----------------------****************----------------------")
    ch=int(input('Enter the you choice:\n'))
    match ch:
        case 1:
            insertData()
        case 2:
            update()
        case 3:
            delete()
        case 4:
            print("-------------**********All Data From Table***********-------------")
            showAll()
            print("-----------------------******END******----------------------")
        case 5:
            break
        case _:
            print("you are enter wrong choice:\n")

