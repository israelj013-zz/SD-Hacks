from flask import Flask, render_template, request, url_for, flash, redirect
from detect_text import create_schedule
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "C:/Users/mjnav/github/SD-Hacks"
app = Flask(__name__)
app.secret_key = "sd-hacks"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("main.html")

# @app.route("/main", methods=["GET", "POST"])
# def file_input():
#     error = None
#     try:
#         if request.method == "POST":
#             attemptedFile = request.form["fileToUpload"]
#             with open(attemptedFile, 'rb') as source_image:
#                  source_bytes = source_image.read()
#             schedule = create_schedule(source_bytes)
#             return redirect(url_for('modifySchedule'), schedule)
#     except Exception as e:
#         flash(e)
#     return redirect(url_for('modifySchedule'))
#     #return render_template("main.html")

@app.route("/modifySchedule", methods = ["GET", "POST"] )
def get_file():
    error = None
    # try:
    if request.method == "POST":
        print(request.files)
        attemptedFile = request.files["fileToUpload"]
        print('here', attemptedFile)
        filename = secure_filename(attemptedFile.filename)
        # print(attemptedFile)
        attemptedFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        with open(filename, 'rb') as source_image:
              source_bytes = source_image.read()
        schedule = create_schedule(source_bytes)
        return render_template("modifySchedule", schedule = schedule)
        #commet
        #return("Hello World")
    # except Exception as e:
    #     flash(e)
    #
    #
    #     return render_template("modifySchedule.html", error = error)


if __name__ == "__main__":
    app.run(debug=True)
