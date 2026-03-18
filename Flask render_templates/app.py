from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    # if username == "admin" and password == "pass":
    #     return render_template("welcome.html", name=username) #{{name}}
    valid_users = {
        "admin": "pass", 
        "user1": "password1", 
        "user2": "password2"
    }
    if username in valid_users and valid_users[username] == password:
        return render_template("welcome.html", name=username) #{{name}}
    else:
        return "<h1>Invalid credentials</h1>"

if __name__ == "__main__":
    app.run(debug=True)