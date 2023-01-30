from flask import Flask, render_template, request, make_response, redirect
import hashlib

app = Flask(__name__, static_url_path='/static')

def check_auth(password:str=None, attempts:int=0):
    if password is None or password.strip() == "":
        return "Password not provided."
    if attempts is not None and attempts >= 10:
        return "Attempt limit reached."
    with open('password_hash.txt', 'r', encoding='utf-8') as password_hashe:
        password_hash = password_hashe.read()
        result = hashlib.sha512(password.encode())
        if result.hexdigest() not in password_hash:
            return "Invalid password."
        return True

def remove_password(password:str=None):
    if password is None:
        return "Password is not provided."
    with open('password_hash.txt', 'r', encoding="utf-8") as password_hashe:
        password_hash = password_hashe.read()
        with open('password_hash.txt', 'w', encoding='utf-8') as password_hashx:
            result = hashlib.sha512(password.encode())
            password_hashx.write(password_hash.replace(f"{result.hexdigest()}", "")) # There will be blanks where the password hash used to be.
    return "Password removed successfully."

def add_password(password:str=None):
    if password is None:
        return "Password is not provided."
    with open('password_hash.txt', 'a', encoding="utf-8") as password_hash:
        result = hashlib.sha512(password.encode())
        password_hash.write(f"\n{result.hexdigest()}")
    return "Password added successfully."

@app.route("/")
def index():
    cookie = request.cookies.get("password")
    if cookie is None:
        return render_template("auth.html", additional="")
    result = check_auth(cookie)
    if result is not True:
        return render_template("auth.html", additional=result)
    return redirect("/index")

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    attempts = request.cookies.get("attempts")
    if attempts is None:
        attempts = 0
    result = check_auth(text, int(attempts))
    if result is not True:
        resp = make_response(render_template("auth.html", additional=result))
        resp.set_cookie('attempts', str(int(attempts) + 1))
        return resp
    resp = make_response(redirect("/index"))
    resp.set_cookie('password', text)
    return resp

@app.route('/index')
def command_line():
    cookie = request.cookies.get("password")
    result = check_auth(cookie)
    if result is not True:
        return redirect("/")
    resp = make_response(render_template("index.html", additional=result))
    resp.set_cookie('attempts', "0")
    return resp

@app.route('/index', methods=['POST'])
def command_line_post():
    cmd = request.form['cmd']
    cookie = request.cookies.get("password")
    result = check_auth(cookie)
    if result is not True:
        return redirect("/")
    if cmd.strip() == "":
        return render_template('index.html')
    res = eval(cmd)
    return render_template('index.html', result=res)
