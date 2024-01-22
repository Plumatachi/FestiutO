import datetime
from wtforms import StringField, HiddenField, FileField, SubmitField, SelectField, TextAreaField, DateField,PasswordField, BooleanField, IntegerField, FloatField, RadioField, SelectMultipleField, widgets, FieldList, FormField, DecimalField, TimeField, DateTimeField, DateField, EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from .requete import Appartient, Groupe, Hebergement, Musicien, Scene, get_cnx , Spectateur, Evenement,Reserver

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
            Musicien.Insert.insert_musicien(cnx, self.nom.data,self.email.data, self.numeroTelephone.data, "NULL")
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
        
class ModifierNomGroupeForm(FlaskForm):
    nomGroupe = StringField('Nom du groupe', validators=[DataRequired()])
    nouveauNomGroupe = StringField('Nouveau nom du groupe', validators=[DataRequired()])
    nouveauNomGroupeVerif = StringField('Confirmer le nouveau nom du groupe', validators=[DataRequired()])
    
    def change_nom_groupe(self, idGroupe):
        try:
            if self.nouveauNomGroupe.data != self.nouveauNomGroupeVerif.data:
                return False
            Groupe.Update.update_nom_groupe(cnx, idGroupe, self.nouveauNomGroupe.data)
            return True
        except:
            return False
        

class ModifierDescriptionGroupeForm(FlaskForm):
    nomGroupe = StringField('Nom du groupe', validators=[DataRequired()])
    nouvelleDescriptionGroupe = StringField('Nouvelle description du groupe', validators=[DataRequired()])
    nouvelleDescriptionGroupeVerif = StringField('Confirmer la nouvelle description du groupe', validators=[DataRequired()])
    
    def change_description_groupe(self, idGroupe):
        try:
            if self.nouvelleDescriptionGroupe.data != self.nouvelleDescriptionGroupeVerif.data:
                return False
            Groupe.Update.update_description(cnx, idGroupe, self.nouvelleDescriptionGroupe.data)
            return True
        except:
            return False
        
class AjouterMembreGroupeForm(FlaskForm):
    nomGroupe = StringField('Nom du groupe', validators=[DataRequired()])
    nomMembre = StringField('Nom du membre', validators=[DataRequired()])

    def ajouter_membre_groupe(self):
        try:
            groupe = Groupe.Get.get_groupe_with_nom(cnx, self.nomGroupe.data)
            print(groupe)
            idMusicien = Musicien.Get.get_id_musicien_with_nom(cnx, self.nomMembre.data)
            print(idMusicien)
            Appartient.Insert.insert_membre(cnx, idMusicien ,groupe[0])
            return True
        except: 
            return False

class AjouterHebergementForm(FlaskForm):
    nomHebergement = StringField('Nom de l\'hebergement', validators=[DataRequired()])
    nombreDePlace = IntegerField('Nombre de place', validators=[DataRequired()])
    
    def ajouter_hebergement(self):
        try:
            Hebergement.Insert.insert_hebergement(cnx,  self.nombreDePlace.data, self.nomHebergement.data)
            return True
        except: 
            return False
        
class ModifierPlaceHebergementForm(FlaskForm):
    nomHebergement = StringField('Nom de l\'hebergement', validators=[DataRequired()])
    nombreDePlace = IntegerField('Nombre de place', validators=[DataRequired()])
    nombreDePlaceVerif = IntegerField('Confirmer le nombre de place', validators=[DataRequired()])
    
    def change_place_hebergement(self, idHebergement):
        try:
            if self.nombreDePlace.data != self.nombreDePlaceVerif.data:
                return False
            Hebergement.Update.update_place_hebergement(cnx, idHebergement, self.nombreDePlace.data)
            return True
        except: 
            return False
        
class ModifierNomHebergementForm(FlaskForm):
    nomHebergement = StringField('Nom de l\'hebergement', validators=[DataRequired()])
    nouveauNomHebergement = StringField('Nouveau nom de l\'hebergement', validators=[DataRequired()])
    nouveauNomHebergementVerif = StringField('Confirmer le nouveau nom de l\'hebergement', validators=[DataRequired()])
    
    def change_nom_hebergement(self, idHebergement):
        try:
            if self.nouveauNomHebergement.data != self.nouveauNomHebergementVerif.data:
                return False
            Hebergement.Update.update_nom_hebergement(cnx, idHebergement, self.nouveauNomHebergement.data)
            return True
        except:
            return False
        


class AjouterConcertForm(FlaskForm):
    nomJournee = StringField('Nom de la journée', validators=[DataRequired()])
    nomGroupe = StringField('Nom du groupe', validators=[DataRequired()])
    montage = StringField('Montage', validators=[DataRequired()])
    demontage = StringField('Démontage', validators=[DataRequired()])
    scene = StringField('Scene', validators=[DataRequired()])
    dateDebut = DateTimeField('Date de début', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S', default=datetime.datetime.now)
    dateFin = DateTimeField('Date de Fin', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S', default=datetime.datetime.now)

    def ajouter_concert(self):
            try:
                Evenement.Insert.insert_concert(cnx, self.nomGroupe.data ,self.montage.data, self.demontage.data, self.dateDebut.data, self.dateFin.data, self.scene.data, self.nomJournee.data)
                return True
            except:
                return False
            
class ModifierNomGroupePourConcertForm(FlaskForm):
    ancienNomDuGroupe = StringField('Nom de l\'hebergement', validators=[DataRequired()])
    nouveauNomGroupe = StringField('Nom de l\'hebergement', validators=[DataRequired()])

    def change_nom_groupe(self, idEvenement):
        try:
            Evenement.Update.update_evenement_groupe(cnx, idEvenement, self.nouveauNomGroupe.data)
            return True
        except:
            return False
        


class ModifierScenePourConcertForm(FlaskForm):
    ancienScene = StringField('ancien scene', validators=[DataRequired()])
    nouveauScene = StringField('nouveau scene', validators=[DataRequired()])

    def change_scene(self, idEvenement):
        try:
            Evenement.Update.update_evenement_scene(cnx, idEvenement, self.nouveauScene.data)
            return True
        except:
            
            return False
            
class ModifierMontagePourConcertForm(FlaskForm):
    tempsMontage = StringField('temps montage', validators=[DataRequired()])

    def change_Montage(self, idEvenement):
        try:
            Evenement.Update.update_evenement_montage(cnx, idEvenement, self.tempsMontage.data)
            return True
        except:
            return False
        

class ModifierDemontagePourConcertForm(FlaskForm):
    tempsDemontage = StringField('temps montage', validators=[DataRequired()])

    def change_demontage(self, idEvenement):
        try:
            Evenement.Update.update_evenement_demontage(cnx, idEvenement, self.tempsDemontage.data)
            return True
        except:
            return False
        

class ModifierDateDebutPourConcertForm(FlaskForm):
    dateDebut = DateTimeField('Date de début', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S', default=datetime.datetime.now)

    def change_dateDebut(self, idEvenement):
        try:
            Evenement.Update.update_evenement_dateDebut(cnx, idEvenement, self.dateDebut.data)
            return True
        except:
            return False
        

class ModifierDateFinPourConcertForm(FlaskForm):
    dateFin = DateTimeField('Date de début', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S', default=datetime.datetime.now)

    def change_dateFin(self, idEvenement):
        try:
            Evenement.Update.update_evenement_dateFin(cnx, idEvenement, self.dateFin.data)
            return True
        except:
            return False
        
class ModifierNomActivitePourActiviteForm(FlaskForm):
    nouveauNomActivite = StringField('nouveau nom activite', validators=[DataRequired()])

    def change_nom_activite(self, idEvenement):
        try:
            Evenement.Update.update_evenement_nomActivite(cnx, idEvenement, self.nouveauNomActivite.data)
            return True
        except:
            return False
        

class ModifierPrivatisationPourActiviteForm(FlaskForm):
    nouveauPrivatisation = StringField('public ou priver', validators=[DataRequired()])

    def change_privatisation(self, idEvenement):
        try:
            Evenement.Update.update_evenement_privatisation(cnx, idEvenement, self.nouveauPrivatisation.data)
            return True
        except:
            return False
        

class AjouterActivteForm(FlaskForm):
    nomJournee = StringField('Nom de la journée', validators=[DataRequired()])
    nomGroupe = StringField('Nom du groupe', validators=[DataRequired()])
    nomActivite = StringField('nomActivte', validators=[DataRequired()])
    privatisation = StringField('privatisation', validators=[DataRequired()])
    scene = StringField('Scene', validators=[DataRequired()])
    dateDebut = DateTimeField('Date de début', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S', default=datetime.datetime.now)
    dateFin = DateTimeField('Date de Fin', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S', default=datetime.datetime.now)

    def ajouter_activite(self):
            try:
                Evenement.Insert.insert_activite(cnx, self.nomGroupe.data ,self.nomActivite.data, self.privatisation.data, self.dateDebut.data, self.dateFin.data, self.scene.data, self.nomJournee.data)
                return True
            except:
                return False


class ModifierJourneeBilletForm(FlaskForm):
    nomJournee = StringField('Nom de la journée', validators=[DataRequired()])
    
    def change_journee(self, idJournee,idSpectateur):

            Reserver.Update.update_journee(cnx, idJournee,idSpectateur, self.nomJournee.data)
   