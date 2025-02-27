from flask import Flask
from flask_migrate import Migrate
from models import db

### インスタンス生成
app = Flask(__name__)

# 設定ファイル読み込み
app.config.from_object("config.Config")
# dbとFlaskとの紐づけ
db.init_app(app)
# マイグレーションとの紐づけ(Flaskとdb)
migrate = Migrate(app, db)
# viewsのインポート
from views import *

### 実行
if __name__ == '__main__':
    app.run(debug=True)