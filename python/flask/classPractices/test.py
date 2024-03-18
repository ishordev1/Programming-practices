from flask import Flask,jsonify,render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='python'
mysql=MySQL(app)

# @app.route('/')
# def hello_world():
#     data={
#         "message":"this is return"
#     }
#     return jsonify(data)

@app.route('/')
def hello_world():
   cur=mysql.connect.cursor()
   cur.execute('select *from user')
   data=cur.fetchall()
   return str(data)
#    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)