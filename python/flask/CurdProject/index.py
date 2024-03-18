from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='flaskcurd'
mysql=MySQL(app)


@app.route('/test')
def test():
    return "home"

@app.route('/')
def home():
    cursor=mysql.connection.cursor()
    cursor.execute("select *from user")
    data=cursor.fetchall()
    return render_template("index.html",page="home Page",users=data)

@app.route('/formData', methods=["POST"])
def formData():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    # cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
   # Construct the query dynamically
    data = (name, email, password)  
    cursor=mysql.connection.cursor()
    cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)", data)
    mysql.connection.commit()
    cursor.close()
    print(name, email, password)
    return redirect("/")


@app.route('/delete/<int:user_id>', methods=['GET', 'POST'])
def deleteUser(user_id):
    # print("this is user Id",user_id)
    cursor=mysql.connection.cursor()
    cursor.execute("DELETE FROM user WHERE id=%s", (user_id,))
    mysql.connection.commit()
    cursor.close()
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET','POST'])
def updateUser(user_id):
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE id=%s", ([user_id]))
    # cursor.execute("select *from user where id=%s", (user_id,))
    userData=cursor.fetchone()
    cursor.close()
    return render_template("updateUser.html",page="update User",user=userData)


@app.route('/updateuser/<int:user_id>', methods=['GET','POST'])
def updateUserData(user_id):
    
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    print(user_id ,name, email, password)
    cursor=mysql.connection.cursor()
    cursor.execute("UPDATE user SET name=%s, email=%s, password=%s WHERE id=%s", (name, email, password, user_id))
    mysql.connection.commit()
    cursor.close()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True,port=8080)
