import datetime
from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField,PasswordField, BooleanField, IntegerField, FloatField, RadioField, SelectMultipleField, widgets, FieldList, FormField, DecimalField, TimeField, DateTimeField, DateField, EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from .requete import get_cnx , Spectateur

cnx = get_cnx()

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    next = HiddenField()
    
    def get_authenticated_user(self):
        user = Spectateur.Get.get_all_spectateur_avec_email(cnx, self.email.data)
        mdp = Spectateur.Get.get_password_with_email(cnx, self.email.data)
        if user is None:
            return None
        passwd = self.password.data
        print(str(mdp)+" == "+str(passwd))
        return user if passwd == mdp else None
    
class RegisterForm(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    numerotelephone = StringField('numerotelephone', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Password again', validators=[DataRequired()])
    next = HiddenField()

class ModifierMdpForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    ancienPassword = PasswordField('Ancien mot de passe', validators=[DataRequired()])
    password = PasswordField('Nouveau mot de passe', validators=[DataRequired()])
    confirm = PasswordField('Confirmer le nouveau mots de passe', validators=[DataRequired()])
    next = HiddenField()

    def change_password(self):
        if self.password.data != self.confirm.data:
            return False
        Spectateur.Update.update_mdp(cnx, self.email.data, self.password.data)
        return True

class ModifierEmailForm(FlaskForm):
    ancienEmail = EmailField('email', validators=[DataRequired()])
    passwordActuel = PasswordField('Mot de passe actuel', validators=[DataRequired()])
    nouveauEmail = EmailField('Nouveau email', validators=[DataRequired()])
    next = HiddenField()

    def change_email(self):
        Spectateur.Update.update_email(cnx, self.ancienEmail.data, self.nouveauEmail.data)

class CalendarForm(FlaskForm):
    date = DateField('Choisir une date', validators=[DataRequired()], format='%Y-%m-%d', default=datetime.date.today)
    next = HiddenField()
    
class ModifierNomForm(FlaskForm):
    identifiant = StringField('Identifiant', validators=[DataRequired()])
    ancienNom = StringField('Nom actuel', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])

    def change_nom(self):
        Spectateur.Update.update_nom(cnx, self.identifiant.data, self.nom.data)
    
class ModifierNumeroTelephoneForm(FlaskForm):
    identifiant = StringField('Identifiant', validators=[DataRequired()])
    ancienNumeroTelephone = StringField('Numéro de téléphone actuel', validators=[DataRequired()])
    numeroTelephone = StringField('Numéro de téléphone', validators=[DataRequired()])

    def change_numeroTelephone(self):
        Spectateur.Update.update_numeroTelephone(cnx, self.identifiant.data, self.numeroTelephone.data)