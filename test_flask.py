from flask import Flask, render_template, flash, request, abort, redirect
from wtforms import Form,TextField,PasswordField,validators
from models import User
from db import *

app = Flask(__name__)
app.secret_key = '123'

class LoginForm(Form):
    ur = TextField("username",[validators.Required()])
    pw = PasswordField("password",[validators.Required()])

@app.route('/')
def hello_world():
    flash('welcome')
    return render_template("one_base.html")

@app.route('/user', methods=['GET','POST'])
def user_index():
    user = User(1, "fengnan")
    myForm = LoginForm(request.form)
    if request.method == 'POST':
        if myForm.ur.data == 'fengnan' and myForm.pw.data == '123456' and myForm.validate():
            return redirect("https://www.baidu.com")
        else:
            message = "username or password wrong"
            return render_template("user.html", user=user, message=message, form=myForm)
    return render_template("user.html", user=user, form=myForm)

@app.route('/register', methods=['GET', 'POST'])
def register():
    myform = LoginForm(request.form)
    message = "please register"
    user = User(1, "fengnan")
    if request.method == "POST":
        addUser(myform.ur.data, myform.pw.data)
        message = "register sucess"
    return render_template("user.html", user=user, message=message, form=myform)


@app.route('/query/<user_id>')
def query(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, "fengnan")
        return render_template("query.html", user=user)
    else:
        abort(404)


@app.route('/users')
def user_list():
    users = []
    for i in range(1,11):
        user = User(i, 'fengnan'+str(i))
        users.append(user)
    return render_template("user_list.html",users=users)

@app.route('/login', methods=['GET','POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if request.method == 'POST':
        if not username:
            flash("please input the username")
            return render_template("one_base.html")
        if not password:
            flash("please input the password")
            return render_template("one_base.html")
        if username == 'fengnan' and password == '123456':
            flash('login sucess')
            return render_template("one_base.html")
        else:
            flash('login failed')
            return render_template("one_base.html")
    return render_template("one_base.html")

@app.route('/Cal')
def calculate():
    return render_template("Cal.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000)
