from flask import render_template, redirect, session, url_for, request, jsonify
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

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/update_cart', methods=['POST'])
def update_cart():
    data = request.get_json()
    book_id = data['book_id']
    is_listed = data['is_listed']

    try:
        # データベースを更新
        book = Book.query.get(book_id)
        if book:
            book.list = is_listed
            db.session.commit()
            return jsonify({'message': 'Cart updated successfully'})
        else:
            return jsonify({'message': 'Book not found'}), 404
    except Exception as e:
        print("Error occurred:", e)
        return jsonify({'message': 'Error updating cart'}), 500