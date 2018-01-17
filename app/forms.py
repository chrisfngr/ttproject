from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class InputName(Form):
    test_Name = StringField('test_Name', validators = [DataRequired()])
