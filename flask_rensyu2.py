# s24011
# flask_rensyu2.py
# 「こんにちは世界」と書かれたHTML文章を表示するプログラム

# render_templateはhtmlファイルを扱う際必要
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

if __name__== '__main__':
    app.run(host='0.0.0.0',port=6423)
