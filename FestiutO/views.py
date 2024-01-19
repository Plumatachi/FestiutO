from flask import render_template, url_for, redirect, request, session, jsonify, send_file
from .formulaire import *
from flask_login import login_user, current_user, logout_user, login_required
from .app import app
from .requete import Scene, afficher_table, get_cnx , Spectateur, Journee , Musicien, FAVORIS, FONCTION, Groupe , Evenement


cnx = get_cnx()

@app.route("/")
def home():
    try:
        user = session['utilisateur'][0]
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
    
    


@app.route("/Billeterie/acheterBillet", methods=(["GET"]))
def acheterBillet():
    idJournee = request.args.get('idJournee')
    param2 = request.args.get('type')
    param3 = request.args.get('nombre')
    user = session['utilisateur'][0]
    Journee.Insert.insert_journee(idJournee,user)

    return render_template(
        "login.html",
        title="Profil"
    )
    
    

@app.route("/Programme/")
def programme():
    user = session['utilisateur'][0]
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

            session['utilisateur'] = (user[0],user[6])
            print("login : "+str(user))
            if user[6] != "Spectateur":
                return redirect(url_for("organisation"))
            else:
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
        Spectateur.Insert.insert_spectateur(cnx, f.nom.data, f.numerotelephone.data, f.email.data, f.password.data, 0)
        return render_template("login.html",title="login",form=LoginForm())
    return render_template(
        "register.html",
        title="register",
        form=f,
    )

@app.route("/Profil/")
def profil():
    user = session['utilisateur'][0]
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
     return jsonify(listeInfo)
 
@app.route('/Profil/favoris/<idUser>')
def favoris(idUser):
    userInfo = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    groupFavorisList = FAVORIS.GET.get_favoris_with_idSpectateur(cnx, idUser)

    return render_template('favoris.html', user=userInfo, groupFavorisList=groupFavorisList)

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
    



@app.route("/acheter_billet_evenement", methods=(["GET"]))
def acheter_billet_evenement():
    idEvenement = request.args.get('idEvenement')
    user = session['utilisateur'][0]
    Evenement.Insert.insert_billet_evenement(user,idEvenement)
    return redirect(url_for('achat_billet_evenement', idEvenement=idEvenement))



@app.route("/achat_billet_evenement/<idEvenement>")
def achat_billet_evenement(idEvenement):
    return render_template('achat_billet.html', idEvenement=idEvenement)


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

@app.route("/espace-organisateur/gestion-comptes//modifier_email/<idUser>",methods=("GET","POST",))
def modifierEmail(idUser):
    form = ModifierEmailFormORG()
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    if form.is_submitted():
        res = form.change_email()
        if res:
            return redirect(url_for('modifierEmail', idUser=idUser, erreur="Email modifié", form=form))
        else:
            render_template('modifierEmail.html', user=user , erreur="Les emails ne correspondent pas", form=form)
    return render_template('modifierEmail.html', user=user, form=form)

@app.route("/espace-organisateur/gestion-comptes//modifier-mot-de-passe/<idUser>",methods=("GET","POST",))
def modifierMdp(idUser):
    form = ModifierPasswordFormORG()
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    if form.is_submitted():
        res = form.change_password()
        if res:
            return redirect(url_for('modifierMdp', user=user, erreur="Mot de passe modifié"))
        else:
            return render_template('modifierMDP.html', user=user, erreur="Les mots de passe ne correspondent pas")            
    return render_template('modifierMDP.html', user=user, form=form)

@app.route("/espace-organisateur/gestion-comptes//modifier-nom/<idUser>" ,methods=("GET","POST",))
def modifierNom(idUser):
    form = ModifierNomFormORG()
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    if form.is_submitted():
        res = form.change_nom()
        if res:
            return redirect(url_for('modifierNom', idUser=idUser, form=form, erreur="Nom modifié"))
        else:
            return render_template('modifierNom.html', user=user, form=form, erreur="Les nom ne correspondent pas")
    return render_template('modifierNom.html', user=user, form=form)

@app.route("/espace-organisateur/gestion-comptes//modifier-telephone/<idUser>", methods=("GET","POST",))
def modifierTelephone(idUser):
    user = Spectateur.Get.get_spectateur_with_id(cnx, idUser)
    form = ModifierNumeroTelephoneFormORG()
    if form.is_submitted():
        res = form.change_numeroTelephone()
        if res:
            return redirect(url_for('modifierTelephone', idUser=idUser, form=form, erreur="Numéro de téléphone modifié"))
        else:
            return render_template('modifierTelephone.html', user=user, form=form, erreur="Les numéros de téléphone ne correspondent pas")
    return render_template('modifierTelephone.html', user=user, form=form)


# @app.route("/espace-organisateur/gestion-comptes/<idUser>/delete")
# def deleteCompte(idUser):
#     Spectateur.Delete.delete_spectateur(cnx, idUser)
#     return redirect(url_for('gestionComptes_avant'))


@app.route("/espace-organisateur/gestion-comptes/ajouter-compte-organisateur", methods=("GET","POST",))
def ajouterCompteOrganisateur():
    form = AjouterCompteOrganisateurForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm.data:
            return render_template("ajouterCompteOrganisateur.html", form=form, erreur="Les mots de passe ne correspondent pas"
            )
        res = form.ajouter_compte()
        if res:
            return redirect(url_for("ajouterCompteOrganisateur", erreur="Compte ajouté", form=form))
        else:
            return render_template("ajouterCompteOrganisateur.html", form=form, erreur="L'email existe déjà")
    return render_template(
        "ajouterCompteOrganisateur.html",
        title="Ajouter compte organisateur",
        form=form,
    )
    
@app.route("/espace-organisateur/gestion-comptes/<idUser>/delete")
def supprimerCompte(idUser):
    Spectateur.Delete.delete_spectateur(cnx, idUser)
    return redirect(url_for('gestionComptes_avant'))

@app.route("/espace-organisateur/gestion-artiste/")
def gestionArtiste():
    allArtiste = afficher_table(cnx, "MUSICIEN")
    return render_template('gestionArtiste.html', allArtiste=allArtiste)

@app.route("/espace-organisateur/gestion-artiste/<idUser>")
def modifierArtiste(idUser):
    user = Musicien.Get.get_musicien_with_id(cnx, idUser)
    return render_template('modifierArtiste.html', user=user)

@app.route("/espace-organisateur/gestion-artiste/<idUser>/modifier-email", methods=("GET","POST",))
def modifierEmailMusicien(idUser):
    musicien = Musicien.Get.get_musicien_with_id(cnx, idUser)
    form = ModifierEmailFormORG()
    if form.is_submitted():
        res = form.change_email_musicien()
        if res:
            return redirect(url_for('modifierEmailMusicien', erreur="Artiste modifié", form=form, idUser=idUser))
        else:
            return render_template('modifierEmailMusicien.html', form=form, erreur="Les informations ne sont pas valides")
    return render_template('modifierEmailMusicien.html', form=form, user=musicien)

@app.route("/espace-organisateur/gestion-artiste/<idUser>/modifier-nom", methods=("GET","POST",))
def modifierNomMusicien(idUser):
    musicien = Musicien.Get.get_musicien_with_id(cnx, idUser)
    form = ModifierNomFormORG()
    if form.is_submitted():
        res = form.change_nom_musicien()
        if res:
            return redirect(url_for('modifierNomMusicien', erreur="Artiste modifié", form=form, idUser=idUser))
        else:
            return render_template('modifierNomMusicien.html', form=form, erreur="Les informations ne sont pas valides")
    return render_template('modifierNomMusicien.html', form=form, user=musicien)

@app.route("/espace-organisateur/gestion-artiste/<idUser>/modifier-telephone", methods=("GET","POST",))
def modifierTelephoneMusicien(idUser):
    musicien = Musicien.Get.get_musicien_with_id(cnx, idUser)
    form = ModifierNumeroTelephoneFormORG()
    if form.is_submitted():
        res = form.change_numeroTelephone_musicien()
        if res:
            return redirect(url_for('modifierTelephoneMusicien', erreur="Artiste modifié", form=form, idUser=idUser))
        else:
            return render_template('modifierTelephoneMusicien.html', form=form, erreur="Les informations ne sont pas valides", user=musicien)
    return render_template('modifierTelephoneMusicien.html', form=form, user=musicien)

@app.route("/espace-organisateur/gestion-artiste/<idUser>/delete", methods=("GET","POST",))
def supprimerMusicien(idUser):
    Musicien.Delete.delete_musicien(cnx, idUser)
    return redirect(url_for('gestionArtiste'))

@app.route("/espace-organisateur/gestion-artiste/ajouter-artiste", methods=("GET","POST",))
def ajouterArtiste():
    form = AjouterArtisteForm()
    if form.validate_on_submit():
        res = form.ajouter_artiste()
        if res:
            return redirect(url_for("gestionArtiste"))
        else:
            return render_template("ajouterArtiste.html", form=form, erreur="Erreur lors de l'ajout de l'artiste")
    return render_template("ajouterArtiste.html", form=form)

     
    
@app.route("/espace-organisateur/gestion-lieu")
def gestionLieu():
    allLieu = afficher_table(cnx, "SCENE")
    return render_template('gestionLieu.html', allLieu=allLieu)


@app.route("/espace-organisateur/gestion-lieu/<idLieu>")
def gestionLieuUnique(idLieu):
    scene = Scene.Get.get_scene_with_id(cnx, idLieu)
    return render_template('gestionLieuUnique.html', scene=scene)

@app.route("/espace-organisateur/gestion-lieu/ajoute-lieu", methods=("GET","POST",))
def ajouterScene():
    form = AjouterSceneForm()
    if form.validate_on_submit():
        res = form.ajouter_scene()
        if res:
            return redirect(url_for("gestionLieu"))
        else:
            return render_template("ajouterScene.html", form=form, erreur="Erreur lors de l'ajout de la scene")
    return render_template("ajouterScene.html", form=form)

@app.route("/espace-organisateur/gestion-lieu/modifier/<idLieu>", methods=("GET","POST",))
def gestionLieuModifier(idLieu):
    scene = Scene.Get.get_scene_with_id(cnx, idLieu)
    return render_template('gestionLieuModifier.html', scene=scene)

@app.route("/espace-organisateur/gestion-lieu/modifier/<idLieu>/modifier-nom", methods=("GET","POST",))
def modifierNomScene(idLieu):
    scene = Scene.Get.get_scene_with_id(cnx, idLieu)
    form = ModifierNomSceneForm()
    if form.is_submitted():
        res = form.change_nom_scene(idLieu)
        if res:
            return redirect(url_for('modifierNomScene', erreur="Scene modifié", form=form, idLieu=idLieu))
        else:
            return render_template('modifierNomScene.html', form=form, erreur="Les informations ne sont pas valides")
    return render_template('modifierNomScene.html', form=form, scene=scene)

@app.route("/espace-organisateur/gestion-lieu/modifier/<idLieu>/modifier-lieu", methods=("GET","POST",))
def modifierNomLieu(idLieu):
    scene = Scene.Get.get_scene_with_id(cnx, idLieu)
    form = ModifierNomLieuForm()
    if form.is_submitted():
        res = form.change_nom_lieu(idLieu)
        if res:
            return redirect(url_for('modifierNomLieu', erreur="Scene modifié", form=form, idLieu=idLieu))
        else:
            return render_template('modifierNomLieu.html', form=form, erreur="Les informations ne sont pas valides")
    return render_template('modifierNomLieu.html', form=form, scene=scene)

@app.route("/espace-organisateur/gestion-lieu/modifier/<idLieu>/delete", methods=("GET","POST",))
def supprimerScene(idLieu):
    Scene.Delete.delete_scene(cnx, idLieu)
    return redirect(url_for('gestionLieu'))

@app.route("/espace-organisateur/gestion-groupes")
def gestionGroupe():
    allGroupe = afficher_table(cnx, "GROUPE")
    return render_template('gestionGroupe.html', allGroupe=allGroupe)

@app.route("/espace-organisateur/gestion-groupes/<idGroupe>")
def modifierGroupe(idGroupe):
    groupe = Groupe.Get.get_groupe_with_idgroupe(cnx, idGroupe)
    return render_template('gestionGroupeUnique.html', groupe=groupe)

@app.route("/espace-organisateur/gestion-groupes/ajouter-groupe", methods=("GET","POST",))
def ajouterGroupe():
    form = AjouterGroupeForm()
    if form.validate_on_submit():
        res = form.ajouter_groupe()
        if res:
            return redirect(url_for("gestionGroupe"))
        else:
            return render_template("ajouterGroupe.html", form=form, erreur="Erreur lors de l'ajout du groupe")
    return render_template("ajouterGroupe.html", form=form)

# def gestionLieu():
#     allLieu = afficher_table(cnx, "LIEU")
#     return render_template('gestionLieu.html', allLieu=allLieu)


# def gestionGroupe():
#     allGroupe = afficher_table(cnx, "GROUPE")
#     return render_template('gestionGroupe.html', allGroupe=allGroupe)



