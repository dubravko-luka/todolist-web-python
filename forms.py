from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired(), Length(min=1, max=100)])
    description = TextAreaField('Mô tả', validators=[DataRequired()])
    priority = SelectField('Ưu tiên', choices=[('low', 'Thấp'), ('medium', 'Trung bình'), ('high', 'Cao')], validators=[DataRequired()])
    assigned_to = SelectField('Người thực hiện', validators=[DataRequired()], choices=[])
