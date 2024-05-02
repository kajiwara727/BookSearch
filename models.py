from flask_sqlalchemy import SQLAlchemy

# Flask-SQLAlchemyの生成
db = SQLAlchemy()

### モデル

# 本
class Book(db.Model):
    # テーブル名
    __tablename__ = 'books'
    # ID(PK)   
    id = db.Column(db.Integer, primary_key=True)
    # 著者
    author = db.Column(db.String(256))
    # タイトル
    title = db.Column(db.String(512))
    # 出版社
    publisher = db.Column(db.String(256))
    # 値段
    price = db.Column(db.Integer)
    # ISBN
    isbn = db.Column(db.String(10))
    # カートリスト
    list = db.Column(db.Boolean, default = False)

# 検索結果を取得
def dbrows(param_str):
    try:
        results = Book.query.filter(
            (Book.title.like('%' + param_str + '%')) |
            (Book.author.like('%' + param_str + '%'))
        ).all()
    except Exception as e:
        print("Error occurred:", e)
        results = []
    return results

# すべての本を取得
def get_all_books():
    try:
        all_books = Book.query.all()
    except Exception as e:
        print("Error occurred:", e)
        all_books = []
    return all_books