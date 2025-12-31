from flask import Flask, render_template

app = Flask(__name__)

# 1. Home Page
@app.route("/")
def home():
    return render_template("home.html")

# 2. About Us Page
@app.route("/about")
def about():
    return render_template("about.html")

# 3. Infrastructure Page (Labs, Playground, Transport)
@app.route("/infrastructure")
def infrastructure():
    return render_template("infrastructure.html")

# 4. Career Page (Computer Science Teacher Job)
@app.route("/career")
def career():
    return render_template("career.html")

# 5. Admission Page (Fees & Enquiry Form)
@app.route("/admission")
def admission():
    return render_template("admission.html")

if __name__ == "__main__":
    # The 'debug=True' allows you to see changes without restarting the script manually
    app.run(debug=True)