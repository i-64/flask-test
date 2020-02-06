import os
from flask import Flask, render_template
from werkzeug.utils import secure_filename
from flask import flash, request, redirect, url_for, send_from_directory

UPLOAD_FOLDER = os.path.join(os.getcwd(),'static')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route("/")
# def index():
#     return render_template("index.html", message="Hello Flask!");

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return ("200 OK")
            # return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads')
def uploaded_file():
    return render_template("index.html", message="Hello Flask!");
    # return render_template("img.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
