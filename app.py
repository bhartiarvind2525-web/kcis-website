from flask import Flask, render_template, request  # Added 'request' here

app = Flask(__name__)

# 1. Home Page
@app.route("/")
def home():
    return render_template("home.html")

# 2. About Us Page
@app.route("/about")
def about():
    return render_template("about.html")

# 3. Infrastructure Page
@app.route("/infrastructure")
def infrastructure():
    return render_template("infrastructure.html")

# 4. Career Page
@app.route("/career")
def career():
    return render_template("career.html")

# 5. Admission Page
@app.route('/admission', methods=['GET', 'POST'])
def admission():
    if request.method == 'POST':
        parent_name = request.form.get('parent_name')
        mobile = request.form.get('mobile_number')
        target_class = request.form.get('admission_class')
        
        print(f"NEW ENQUIRY: {parent_name}, Phone: {mobile}, Class: {target_class}")
        
        return "<h1>Thank You! We have received your enquiry.</h1><a href='/admission'>Go Back</a>"
    
    return render_template('admission.html')

if __name__ == "__main__":
    app.run(debug=True)
