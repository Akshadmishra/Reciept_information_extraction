from flask import Flask, render_template, request, url_for, session
import os, pytesseract
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image
import pickle
project_dir= 'C:\projects\capstone'
app = Flask(__name__,static_url_path='',
            static_folder='static',
             template_folder='templates' )

photos = UploadSet('photos', IMAGES)
app.config['UPLOAD_FOLDER'] = 'images'

# if __name__ == '__main__':
#     # Setup Tesseract executable path
#     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'
#     app.run(debug=True)

class gettext(object):
    if __name__ == '__main__':
    # Setup Tesseract executable path
     pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    app.run(debug=True)
    def __init__(self, file):
     self.file = pytesseract.image_to_string(Image.open(project_dir + '\images\\' + file))

@app.route("/")
def home():
    return render_template('index.html')

# if __name__ == '__main__':
#     # Setup Tesseract executable path
#     pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR'
#     app.run(debug=True)

@app.route('/form', methods=['GET', 'POST'])
def scan_file():
    if request.method == 'POST':
       name = request.form['img-name'] + '.jpg'
       file = request.files['file']
       path = os.path.join(app.config['UPLOAD_FOLDER'], name)
       file.save(path)
       model_name= request.form['modal']
       

        # print("Found data:", scanned_text)

        # session['data'] = {
        #     "text": scanned_text
        # }


