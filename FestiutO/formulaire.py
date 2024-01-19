import datetime
from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField,PasswordField, BooleanField, IntegerField, FloatField, RadioField, SelectMultipleField, widgets, FieldList, FormField, DecimalField, TimeField, DateTimeField, DateField, EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from .requete import Groupe, Musicien, Scene, get_cnx , Spectateur

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
    

# foorm Organisateur 
class ModifierNomFormORG(FlaskForm):
    email = EmailField('Email actuel', validators=[DataRequired()])
    nom = StringField('Nouveau nom', validators=[DataRequired()])
    nomVerif = StringField('Confirmer le nouveau nom', validators=[DataRequired()])
    def change_nom(self):
        if self.nom.data != self.nomVerif.data:
            return False
        Spectateur.Update.update_nom(cnx, self.email.data, self.nom.data)
        return True
    
    def change_nom_musicien(self):
        if self.nom.data!= self.nomVerif.data:
            return False
        Musicien.Update.update_nom_musicien(cnx, self.email.data, self.nom.data)
        return True
    
class ModifierNumeroTelephoneFormORG(FlaskForm):
    emailField = EmailField('Email actuel', validators=[DataRequired()])
    numeroTelephone = StringField('Numéro de téléphone', validators=[DataRequired()])
    numeroTelephoneVerif = StringField('Confirmer le numéro de téléphone', validators=[DataRequired()])
    def change_numeroTelephone(self):
        if self.numeroTelephone.data != self.numeroTelephoneVerif.data:
            return False
        Spectateur.Update.update_numeroTelephone(cnx, self.emailField.data, self.numeroTelephone.data)
        return True
    
    def change_numeroTelephone_musicien(self):
        if self.numeroTelephone.data!= self.numeroTelephoneVerif.data:
            return False
        Musicien.Update.update_numeroTelephone_musicien(cnx, self.emailField.data, self.numeroTelephone.data)
        return True
        
class ModifierEmailFormORG(FlaskForm):
    ancienEmail = EmailField('Email actuel', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    emailVerif = EmailField('Confirmer l\'email', validators=[DataRequired()])
    
    def change_email(self):
        if self.email.data != self.emailVerif.data:
            return False
        Spectateur.Update.update_email(cnx, self.ancienEmail.data, self.email.data)
        return True
    
    def change_email_musicien(self):
        if self.email.data!= self.emailVerif.data:
            return False
        Musicien.Update.update_email_musicien(cnx, self.ancienEmail.data, self.email.data)
        return True
    
class ModifierPasswordFormORG(FlaskForm):
    email = StringField('Email actuel', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm = PasswordField('Confirmer le mot de passe', validators=[DataRequired()])
    
    def change_password(self):
        if self.password.data != self.confirm.data:
            return False
        Spectateur.Update.update_mdp(cnx, self.identifiant.data, self.password.data)
        return True
class AjouterCompteOrganisateurForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    numeroTelephone = StringField('Numéro de téléphone', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm = PasswordField('Confirmer le mot de passe', validators=[DataRequired()])
    
    def ajouter_compte(self):
        if self.password.data != self.confirm.data:
            return False
        Spectateur.Insert.insert_spectateur(cnx, self.nom.data, self.numeroTelephone.data, self.email.data, self.password.data, 1)
        return True
    
    
class AjouterArtisteForm(FlaskForm):
    nom = StringField('Nom', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    numeroTelephone = StringField('Numéro de téléphone', validators=[DataRequired()])
    photo = FileField('Photo')
    
    def ajouter_artiste(self):
        try:
            Musicien.Insert.insert_musicien(cnx, self.nom.data,self.email.data, self.numeroTelephone.data, "imaginedragons.jpeg",0)
            return True
        except: 
            return False

class AjouterSceneForm(FlaskForm):
    nomScene = StringField('Nom de la scene', validators=[DataRequired()])
    lieu = StringField('Nom du lieux', validators=[DataRequired()])
    
    def ajouter_scene(self):
        try:
            Scene.Insert.insert_scene(cnx, self.nomScene.data, self.lieu.data)
            return True
        except:
            return False
        
class ModifierNomSceneForm(FlaskForm):
    nomScene = StringField('Nom de la scene', validators=[DataRequired()])
    nouveauNomScene = StringField('Nouveau nom de la scene', validators=[DataRequired()])
    nouveauNomSceneVerif = StringField('Confirmer le nouveau nom de la scene', validators=[DataRequired()])
    
    def change_nom_scene(self, idScene):
        try:
            if self.nouveauNomScene.data != self.nouveauNomSceneVerif.data:
                return False
            Scene.Update.update_scene(cnx, idScene, self.nouveauNomScene.data)
            return True
        except:
            return False
        
class ModifierNomLieuForm(FlaskForm):
    nomLieu = StringField('Nom du lieu', validators=[DataRequired()])
    nouveauNomLieu = StringField('Nouveau nom du lieu', validators=[DataRequired()])
    nouveauNomLieuVerif = StringField('Confirmer le nouveau nom du lieu', validators=[DataRequired()])
    
    def change_nom_lieu(self, idScene):
        try:
            if self.nouveauNomLieu.data != self.nouveauNomLieuVerif.data:
                return False
            Scene.Update.update_lieu(cnx, idScene, self.nouveauNomLieu.data)
            return True
        except:
            return False
        
    
class AjouterGroupeForm(FlaskForm):
    nomGroupe = StringField('Nom du groupe', validators=[DataRequired()])
    description = StringField('Email', validators=[DataRequired()])
    reseau = StringField('Numéro de téléphone', validators=[DataRequired()])
    photo = FileField('Photo')

    def ajouter_groupe(self):
        try:
            Groupe.Insert.insert_groupe(cnx, self.nomGroupe.data,self.description.data, self.reseau.data, "NULL",0)
            return True
        except: 
            return False