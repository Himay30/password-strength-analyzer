from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    remarks = []

    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("At least 8 characters required")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Include numbers")

    if re.search(r"[!@#$%^&*]", password):
        strength += 1
    else:
        remarks.append("Use special characters")

    if strength == 5:
        return "Strong 💪", remarks
    elif strength >= 3:
        return "Medium ⚠️", remarks
    else:
        return "Weak ❌", remarks


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    tips = []

    if request.method == "POST":
        password = request.form["password"]
        result, tips = check_password_strength(password)

    return render_template("index.html", result=result, tips=tips)


if __name__ == "__main__":
    app.run(debug=True)