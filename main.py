from flask import Flask, render_template, request

app = Flask(__name__)

# Global dictionary to store names and their results
names = []
results = {}

@app.route("/", methods=["GET", "POST"])
def home():
    global names, results

    # Handle form submissions
    if request.method == "POST":
        if "add_name" in request.form:
            # Add a new name
            new_name = request.form.get("name")
            if new_name:
                names.append(new_name)
                results[new_name] = None  # Initialize result for this name
        elif "add_numbers" in request.form:
            # Add numbers for a specific name
            try:
                name = request.form.get("current_name")
                num1 = float(request.form.get("num1"))
                num2 = float(request.form.get("num2"))
                results[name] = num1 + num2
            except (TypeError, ValueError):
                results[name] = "Invalid input"

    return render_template("index.html", names=names, results=results)


if __name__ == "__main__":
    app.run(debug=True)
