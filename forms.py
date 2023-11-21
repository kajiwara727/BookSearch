from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from models import Book

### Formクラス

# 入力クラス
class InputForm(FlaskForm):
    name = StringField('タイトルか著者を入力してください', validators = [DataRequired('必須入力です')])
    submit = SubmitField('送信')