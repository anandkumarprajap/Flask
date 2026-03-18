from flask import Flask, render_template, request, url_for, redirect, flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        flash(f"Welcome , {name}! You have been registered successfully.", "success")
        return redirect(url_for('Success'))
    return render_template("Register.html", form=form)

@app.route("/success")
def Success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)


    