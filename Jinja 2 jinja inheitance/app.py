from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("feedback.html")  # home page

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        message = request.form.get("message")
        # Here you can process the feedback, e.g., save it to a database or send an email
        return render_template("thankyou.html", user=name , message=message)
    return render_template("feedback.html") 

@app.route("/about")
def about(): 
    
    return render_template("about.html")


if __name__ == "__main__":    
    app.run(debug=True)