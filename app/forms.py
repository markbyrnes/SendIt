from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError,  Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired, FileField
from app.models import User


#login form, validators stop submitting empty field
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

#registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() #checks if username already in db
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() #checks if email already in db
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm): #edit profile 'bio'
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    profile_pic = FileField('Profile Picture', validators=[FileRequired()])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

#follow/unfollow form
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

#Delete Post
class EmptyForm(FlaskForm):
    submit = SubmitField('Delete Post')

#post on your account
class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

#upload avatar
class UploadAvatarForm(FlaskForm):
    image = FileField('Upload (<=3M)', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'The file format should be .jpg or .png.')
    ])
    submit = SubmitField()

#search
class SearchForm(FlaskForm):
    searched = StringField("Search",  validators=[
        DataRequired()])
    submit = SubmitField("Submit")

#send message
class MessageForm(FlaskForm):
    message = TextAreaField(('Message'), validators=[
        DataRequired(), Length(min=0, max=140)])
    submit = SubmitField(('Submit'))