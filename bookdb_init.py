import csv
from models import db, Book
from app import app

# flask db init, flask db migrate, flask db upgradeコマンド後にこのファイルを実行するとcsvファイルが読み込まれる
def add_data_to_db():
    with app.app_context():
        with open('BookList.csv', 'r', encoding="utf-8") as file:
            reader = csv.reader(file)
            for line in reader:
                book = Book(id=line[0], author=line[1], title=line[2], publisher=line[3], price=line[4], isbn=line[5], list = False)
                db.session.add(book)
            db.session.commit()
    # データベースへの変更をコミット
    db.session.commit()

if __name__ == '__main__':
    add_data_to_db()