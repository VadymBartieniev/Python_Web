from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, AnyOf, Regexp, EqualTo, Email, ValidationError
from .models import User


LENGTH_BETWEEN = 'length must be between {} and {} characters'
LENGTH_MIN = 'length must be at least {} characters'
REGEXP = 'input must be for regex ({})'
PASSWORD = 'passwords must match'
ONLY_USERNAME_SYMBOLS = 'username must have only letters, numbers, . or _'
EMAIL = 'Email must be in pattern for email'
EMAIL_EXIST = 'This email already exist!'
USERNAME_EXIST = 'This username already exist!'



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(REQUIRED.format('username')),
                                       Length(min=4, max=14, message=LENGTH_BETWEEN.format(4, 14)),
                                       Regexp('^[A-Za-z][A-Za-z0-9_.]+$', message=ONLY_USERNAME_SYMBOLS)])
    email = StringField('Email',
                        validators=[InputRequired(REQUIRED.format('email')),
                                    Email(message=EMAIL)])
    password = PasswordField('Password',
                             validators=[InputRequired(REQUIRED.format('password')),
                                         Length(min=6, message=LENGTH_MIN.format(6))])

    password_repeat = PasswordField('Confirm password',
                                    validators=[InputRequired(REQUIRED.format('password')),
                                                Length(min=6, message=LENGTH_MIN.format(6)),
                                                EqualTo('password')])

    submit = SubmitField(label=(''))

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(EMAIL_EXIST)

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(USERNAME_EXIST)


class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(),
                                           Length(min=4, max=10,
                                                  message='Name length must be between %(min)d and %(max)d')])
    email = StringField("Email", validators=[DataRequired(), Email(message='Email is invalid')])
    phone = StringField("Phone", validators=[DataRequired(),
                                             Regexp(regex='^\+380[0-9]{9}', message='Phone is invalid')])
    subject = SelectField("Subject", choices=[('1', 'Bug report'), ('2', 'Cooperation'), ('3', 'Suggestions')])
    message = TextAreaField("Message", validators=[DataRequired(), Length(max=500, message='Message is too long')])
    submit = SubmitField("Send")
