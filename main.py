from flask import Flask, render_template, request
import encryption

app = Flask(__name__, static_url_path='/static')

def check_auth(password:str=None):
    print(password)
    if password is None or password.strip() is "":
        return "Password not supplied."
    with open("auth_key.txt", "r", encoding="utf-8") as auth_key:
        auth_key = auth_key.read()
        with open("password_encrypted.txt", "r", encoding="utf-8") as passe:
            passe = passe.read()
            if password != encryption.decrypt(passe, int(auth_key)):
                return "Incorrect password"
            return True

@app.route("/")
def home():
    return render_template("auth.html", additional="")

@app.route('/', methods=['POST'])
def index_post():
    text = request.form['text']
    result = check_auth(text)
    if result is not True:
        return render_template("auth.html", additional=result)
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
