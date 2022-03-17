from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL
from user import User
app = Flask(__name__)  

# home page- display of new page
@app.route('/') 
def index():
    mysql = connectToMySQL("users_schema")
    users = mysql.query_db("SELECT * FROM users;")
    print(users)
    return render_template("read.html", all_users = users)      

# new page for the data- just the display of new user
@app.route ('/user/new')
def new_user():
    return render_template("create.html")


# what we are doing on the templates (new user)
@app.route ('/user/create', methods=["POST"])
def create_user():
    User.make_user(request.form)
    return redirect('/')


if __name__=="__main__":  
    app.run(debug=True) 