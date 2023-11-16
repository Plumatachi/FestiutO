from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField,PasswordField, BooleanField, IntegerField, FloatField, RadioField, SelectMultipleField, widgets, FieldList, FormField, DecimalField, TimeField, DateTimeField, DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from .requete import get_cnx , Spectateur

cnx = get_cnx()

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    next = HiddenField()
    
    def get_authenticated_user(self):
        user = Spectateur.Get.get_nom_spectateur_avec_email(cnx, self.email.data)
        print(user)
        mdp = Spectateur.Get.get_password_with_email(cnx, self.email.data)
        if user is None:
            return None
        passwd = self.password.data
        print(str(mdp)+" == "+str(passwd))
        return user if passwd == mdp else None
    
class RegisterForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    numerotelephone = StringField('numerotelephone', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Password again', validators=[DataRequired()])
    next = HiddenField()
    