import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.getcwd(),'static') # EXTRAA
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

app = Flask(__name__, static_folder='static') # EXTRAA
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # EXTRAA

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'test.jpg')) # EXTRAA
            # return ("200 OK")
            return redirect(url_for('uploaded_file'))
    return render_template("index.html")

@app.route('/uploads')
def uploaded_file():
    return render_template("img.html");

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
