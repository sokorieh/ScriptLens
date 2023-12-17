from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        image = Image.open(io.BytesIO(image_file.read()))
        ocr_result = pytesseract.image_to_string(image)
        return render_template('result.html', text=ocr_result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
