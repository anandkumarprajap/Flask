from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")

        if not name:
            flash("Name cannot be empty")
            return redirect(url_for("home"))

        flash(f"Thanks {name}, your feedback was saved")
        return redirect(url_for("feedback"))   # FIXED

    return render_template("form.html")


@app.route("/thankyou")
def feedback():
    return render_template("thankyou.html")


if __name__ == "__main__":
    app.run(debug=True)