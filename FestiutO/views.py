from click import DateTime
from flask import render_template, url_for, redirect, request, session, jsonify, send_file
from .formulaire import CalendarForm, LoginForm, ModifierEmailForm, ModifierMdpForm,RegisterForm
from datetime import datetime
from flask_login import login_user, current_user, logout_user, login_required
from .app import app
from .requete import get_cnx , Spectateur, Journee , Musicien, FAVORIS, FONCTION, Groupe , Evenement


cnx = get_cnx()

@app.route("/")
def home():
    try:
        user = session['utilisateur']
        listeImageId = Groupe.Get.get_images_groupe()
        return render_template(
        "acceuil.html",
        title="Home",
        lireImage= listeImageId,
        user = user
        )
    except:
        listeImageId = Groupe.Get.get_images_groupe()
        return render_template(
        "acceuil.html",
        title="Home",
        lireImage= listeImageId,
        )

@app.route("/Billeterie/")
def billeterie():
    form = CalendarForm()
    listeInfoDate = Journee.Get.get_journee_date()
    print(listeInfoDate)
    return render_template(
    "billeterie.html",
    title="Home",
    listeDate = listeInfoDate
    )
    
    

@app.route("/achat_billet_journee/<idJournee>/<nombrePlace>/<types>/")
def achat_billet_journee(idJournee,nombrePlace,types):
    return render_template('achat_billet.html', id=idJournee ,nombrePlace=nombrePlace,type="'journee'",typeBillet=types)


@app.route("/acheter_Billet_journee", methods=(["GET"]))
def acheter_Billet_journee():
    idJournee = request.args.get('idJournee')
    param3 = request.args.get('nombrePlace')
    param4 = request.args.get('type')
    user = session['utilisateur']
    try:
        Journee.Insert.insert_journee(idJournee,user,param3,param4)
        return "le billet a bien etait acheter"
    except:
        return "le billet a deja etait acheter"


@app.route("/Billeterie/acheterBillet", methods=(["GET"]))
def acheterBillet():
    idJournee = request.args.get('idJournee')
    param3 = request.args.get('nombrePlace')
    param4 = request.args.get('type')

    return redirect(url_for('achat_billet_journee', idJournee=idJournee,nombrePlace=param3,types=param4))
    
    

@app.route("/Programme/")
def programme():
    user = session['utilisateur']
    listeImageId = Groupe.Get.get_images_groupe()
    return render_template(
    "programme.html",
    title="Home",
    lireImage= listeImageId,
    user = user
    )

@app.route("/Login/", methods=("GET","POST",))
def login():
    f = LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user != None:
            session['utilisateur'] = user[0]
            print("login : "+str(user))
            next = f.next.data or url_for("home")
            return redirect(next)
        
    return render_template(
        "login.html",
        title="Profil",
        form=f,
    )
    
@app.route("/Logout/")
def logout():
    session.pop('utilisateur', None)
    return redirect(url_for('home'))


@app.route("/Register/", methods=("GET","POST",))
def register():
    f = RegisterForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        if f.password.data != f.confirm.data:
            return render_template(
                "register.html",
                title="register",
                form=f,
            )
        Spectateur.Insert.insert_spectateur(cnx, f.nom.data, f.numerotelephone.data, f.email.data, f.password.data)
        return render_template("login.html",title="login",form=LoginForm())
    return render_template(
        "register.html",
        title="register",
        form=f,
    )

@app.route("/Profil/")
def profil():
    user = session['utilisateur']
    print("profil : "+str(user))
    return render_template( "profil.html", title="Profil", user=user)

@app.route("/Profil/Modifier/Mots_de_passe/", methods=("GET","POST",))
def modifier_mdp():
    f = ModifierMdpForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        passwordancien = Spectateur.Get.get_password_with_email(cnx, f.email.data)
        if passwordancien != f.ancienPassword.data:
            return render_template(
                "modifier_mdp.html",
                erreur = "Mot de passe incorrect"
            )
        
        if f.password.data != f.confirm.data:
            return render_template(
                "modifier_mdp.html",
                title="Modifier Mots de passe",
                form=f,
            )
        if f.change_password():
            return redirect(url_for("logout"))
    
    return render_template(
        "modifier_mdp.html",
        title="Modifier Mots de passe",
        form=f,
    )

@app.route("/Profil/Modifier/Email/", methods=("GET","POST",))
def modifier_email():
    f = ModifierEmailForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        passwordancien = Spectateur.Get.get_password_with_email(cnx, f.ancienEmail.data)
        if passwordancien != f.passwordActuel.data:
            return render_template(
                "modifier_email.html",
                erreur = "Mot de passe incorrect",
                form = f
            )
        user = Spectateur.Get.get_all_spectateur_avec_email(cnx, f.ancienEmail.data)
        print(user)
        print(f.ancienEmail.data)
        if f.ancienEmail.data != user[3]:
            return render_template(
                "modifier_email.html",
                title="Modifier Mots de passe",
                form=f,
            )
        else:
            f.change_email()
            return redirect(url_for("logout"))
    
    return render_template(
        "modifier_email.html",
        title="Modifier Mots de passe",
        form=f,
    )

# @app.route('/Billeterie/acheter_le_billet/', methods=['GET', 'POST'])
# def index():
#     form = CalendarForm()
#     if form.validate_on_submit():
#         selected_date = form.date.data
#         # Effectuez des actions avec la date sélectionnée
#         # Par exemple, imprimez-la dans la console
#         print(selected_date)
#     return render_template('index.html', form=form)


# @app.route('/Billeterie/acheter_le_billet/confirmation', methods=['GET', 'POST'])
# def confirmation():
#     return render_template('confirmation.html')

@app.route('/get_Info_journee_Groupe', methods=['GET'])
def get_Info_journee_Groupe():
     param1 = request.args.get('idgroupe')
     listeInfo = Groupe.Get.get_consert_groupe(param1)
     listeInfo1 = Groupe.Get.get_activite_groupe(param1)
     return jsonify(listeInfo+listeInfo1)
 
@app.route('/Profil/favoris/<idUser>')
def favoris(idUser):
    userInfo = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    groupFavorisList = FAVORIS.GET.get_favoris_with_idSpectateur(cnx, idUser)

    return render_template('favoris.html', user=userInfo, groupFavorisList=groupFavorisList)

@app.route('/Profil/billet/<idUser>')
def billet(idUser):
    userInfo = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    billetsJournee = Evenement.Get.get_evenement_with_idSpectateur_journee(idUser)
    billetsEvenement = Evenement.Get.get_evenement_with_idSpectateur_Evenement(idUser)
    return render_template('billet_utilisateur.html', user=idUser, billetsJournee=billetsJournee,billetsEvenement=billetsEvenement)

@app.route('/Groupe_page/<idUser>/<idGroupe>')
def groupe(idUser, idGroupe):
    groupInfo = Groupe.Get.get_groupe_with_idgroupe(cnx, idGroupe)
    listeMucisien = Musicien.Get.get_musicien_with_idgroupe(idGroupe)
    isInFavoris = FONCTION.idGroupe_in_like_with_idSpectateur(cnx, idUser, idGroupe)
    
    if isInFavoris:
        isInFavoris = 1
    else:
        isInFavoris = 0

    print(isInFavoris)
    return render_template('groupe.html', groupe=groupInfo, user=idUser, like=isInFavoris, listeMucisien = listeMucisien )

@app.route('/Profil/favoris/<idUser>/<idGroupe>/like')
def like(idUser, idGroupe):
    FAVORIS.Insert.insert_favoris(cnx, idUser, idGroupe)
    return redirect(url_for('groupe', idUser=idUser, idGroupe=idGroupe))

@app.route('/Profil/favoris/<idUser>/<idGroupe>/dislike')
def dislike(idUser, idGroupe):
    FAVORIS.Delete.delete_favoris(cnx, idUser, idGroupe)
    return redirect(url_for('groupe', idUser=idUser, idGroupe=idGroupe))







@app.route("/acheter_billet_evenement", methods=(["GET"]))
def acheter_billet_evenement():
    idEvenement = request.args.get('idEvenement')
    return redirect(url_for('achat_billet_evenement', idEvenement=idEvenement))

@app.route("/acheter_vrai_billet_evenement", methods=(["GET"]))
def acheter_vrai_billet_evenement():
    idEvenement = request.args.get('idEvenement')
    user = session['utilisateur']
    try:
        Evenement.Insert.insert_billet_evenement(user,idEvenement)
        return "billet acheter"
    except:
          return "deja acheter"


@app.route("/achat_billet_evenement/<idEvenement>")
def achat_billet_evenement(idEvenement):
    evenement= Evenement.Get.get_evenement_with_id(idEvenement)

    # Tableau de noms de mois
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

    # Formater la date selon le format souhaité
    resultat_string = "{} {} {} {} H {} minute".format(evenement[0][0].day, mois[evenement[0][0].month - 1], evenement[0][0].year, evenement[0][0].hour, evenement[0][0].minute)
    print(idEvenement)
    return render_template('achat_billet.html', id=idEvenement , date=resultat_string,nomScene=evenement[0][1],lieux=evenement[0][2],type="'evenement'")


# gestion organisateur
@app.route("/espace-organisateur")
def organisation():
    return render_template('espaceOrganisateur.html')

@app.route("/espace-organisateur/gestion-comptes")
def gestionComptes_avant():
    allUser = Spectateur.Get.get_all_spectateur(cnx)
    return render_template('gestionComptes.html', allUser=allUser)

@app.route("/espace-organisateur/gestion-comptes/<idUser>")
def gestionComptesUnique(idUser):
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    return render_template('gestionComptesUnique.html', user=user)

@app.route("/espace-organisateur/gestion-comptes/<idUser>/modifier_email")
def modifierEmail(idUser):
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    return render_template('modifierEmail.html', user=user)

@app.route("/espace-organisateur/gestion-comptes/<idUser>/modifier-mot-de-passe")
def modifierMdp(idUser):
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    return render_template('modifierEmail.html', user=user)

@app.route("/espace-organisateur/gestion-comptes/<idUser>/modifier-nom")
def modifierNom(idUser):
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    return render_template('modifierNom.html', user=user)

@app.route("/espace-organisateur/gestion-comptes/<idUser>/modifier-telephone")
def modifierTelephone(idUser):
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    return render_template('modifierTelephone.html', user=user)


# @app.route("/espace-organisateur/gestion-comptes/<idUser>/delete")
# def deleteCompte(idUser):
#     Spectateur.Delete.delete_spectateur(cnx, idUser)
#     return redirect(url_for('gestionComptes_avant'))
