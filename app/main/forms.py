#coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class CommentForm(FlaskForm):
    name = StringField(u'昵称', validators=[DataRequired()])
    email = StringField(u'邮箱', validators=[DataRequired(), Length(1, 64)])
    content = TextAreaField(u'内容', validators=[DataRequired(), Length(1, 1024)])
    follow = StringField(validators=[DataRequired()])
