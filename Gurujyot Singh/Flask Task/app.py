from flask import Flask, request, render_template

# Initializing flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Interns!</p>"

@app.route("/calculate", methods=["GET"])
def calculate():
    # Initializing variables
    val1 = None
    val2 = None
    op = None
    a = None

    if request.method == "GET":
        # Getting values from the request and converting it to integer
        val1 = request.args.get("val1", type=int)
        val2 = request.args.get("val2", type=int)
        print(val1, val2)
        op = request.args.get("op")  # Getting the operation

        # Performing operations based on the value of 'op'
        if op == "add":
            a = val1 + val2  # Addition
        elif op == "sub":
            a = val1 - val2  # Subtraction
        elif op == "mul":
            a = val1 * val2  # Multiplication
        elif op == "div":
            # Fixing incorrect condition check for division by zero
            if val2 == 0:
                a = "Cannot be divisible by 0"
            else:
                a = val1 / val2  # Division
        elif op == "power":
            a = val1 ** val2  # Power

    # Returing data to index.html to print output
    return render_template('index.html', val1=val1, val2=val2, op=op, a=a)



if __name__=="__main__":
    app.run(debug=True)
