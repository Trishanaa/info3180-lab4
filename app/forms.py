from flask_wtf import FlaskForm
from wtforms import FileField, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileRequired 

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileRequired(), DataRequired()])  

    def validate_file(self, field):
        if not field.data:  
            raise ValidationError("No file selected.")
        
        if not allowed_file(field.data.filename):  
            raise ValidationError("The file must be a JPG or PNG.")
