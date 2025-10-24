from flask import Flask, render_template, request

app = Flask(__name__)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = add(num1, num2)
        elif operation == "sub":
            result = sub(num1, num2)
        elif operation == "mul":
            result = mul(num1, num2)
        elif operation == "div":
            result = div(num1, num2)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
