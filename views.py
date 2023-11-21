from flask import render_template, redirect, session, url_for, request
from app import app
from models import db, Book, dbrows
from forms import InputForm

### ルーティング

# 入力
@app.route('/', methods=["GET", "POST"])
def input():
    form = InputForm()
    results = []
    # POST
    if form.validate_on_submit():
        param_str = request.form['name']
        results = dbrows(param_str)
        if not results:
            return render_template('input.html', form=form, message="その検索結果に当てはまるものはありません。")
        return render_template('output.html', results=results, param_str=param_str)

    # GET
    return render_template('input.html', form=form)

# 出力
@app.route('/output', methods = ["POST"])
def output():
    return render_template('output.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')