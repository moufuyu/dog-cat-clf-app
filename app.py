import os
import io
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

model = load_model('./dog_cat_clf.h5') # モデルの読み込み
category = np.array(['犬', '猫'])
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'PNG', 'JPG'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        img_file = request.files['img_file']

        # 不適切なファイルを弾く
        if img_file and allowed_file(img_file.filename):
            filename = secure_filename(img_file.filename)
        else:
            return ''' <p>許可されていない拡張子です</p> '''

        # BytesIOで読み込んでOpenCVで扱える型にする
        f = img_file.stream.read()
        bin_data = io.BytesIO(f)
        file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        # サイズを調整
        raw_img = cv2.resize(img, (150, 150))

        # サイズだけ変えたものを保存する
        raw_img_url = os.path.join(app.config['UPLOAD_FOLDER'], 'raw_'+filename)
        cv2.imwrite(raw_img_url, raw_img)

        # 3次元を4次元に変換、入力画像は1枚なのでsamples=1
        img_dims = np.expand_dims(raw_img, axis=0)
        preds = model.predict(img_dims)
        judge = category[np.argmax(preds)] # モデルが予想したカテゴリ
        p = np.max(preds) * 100 # モデルが出力した確率

        return render_template('index.html', raw_img_url=raw_img_url, judge = judge, p = p)

    else:
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.debug = True
    app.run()