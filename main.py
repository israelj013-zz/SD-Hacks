from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("main.html")

@app.route("/main", methods=["GET", "POST"])
def file_input():
    error = None
    try:
        if request.method == "POST":
            attemptedFile = request.form["fileToUpload"]
            return redirect(url_for('modifySchedule'))
    except Exception as e:
        flash(e)
        return render_template("main.html")

@app.route("/modifySchedule")
def print(attemptedFile):
    flash(attemptedFile)


if __name__ == "__main__":
    app.run(debug=True)