from wtforms import Form, TextAreaField, StringField, DateTimeLocalField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')

