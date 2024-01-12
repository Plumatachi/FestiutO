from flask import render_template, url_for, redirect, request, session, jsonify, send_file
from .formulaire import CalendarForm, LoginForm, ModifierEmailForm, ModifierMdpForm,RegisterForm
from flask_login import login_user, current_user, logout_user, login_required
from .app import app
from .requete import get_cnx , Spectateur ,Groupe, Journee , Musicien
from .requete import FAVORIS, FONCTION, get_cnx , Spectateur, Groupe


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
    form=form,
    listeDate = listeInfoDate
    )
    
    


@app.route("/Billeterie/billeterie_post", methods=("GET","POST",))
def billeterie_post():
    form = CalendarForm()
    if form.validate_on_submit():
        selected_date = form.date.data
        # Effectuez des actions avec la date sélectionnée
        # Par exemple, imprimez-la dans la console
        print(selected_date)
    return render_template(
    "billeterie.html",
    title="Home",
    form=form
    )

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

@app.route('/Billeterie/acheter_le_billet/', methods=['GET', 'POST'])
def index():
    form = CalendarForm()
    if form.validate_on_submit():
        selected_date = form.date.data
        # Effectuez des actions avec la date sélectionnée
        # Par exemple, imprimez-la dans la console
        print(selected_date)
    return render_template('index.html', form=form)


@app.route('/Billeterie/acheter_le_billet/confirmation', methods=['GET', 'POST'])
def confirmation():
    return render_template('confirmation.html')

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
    isInFavoris = FONCTION.idGroupe_in_like_with_idSpectateur(cnx, idUser, idGroupe)
    
    if isInFavoris:
        isInFavoris = 1
    else:
        isInFavoris = 0

    print(isInFavoris)
    return render_template('groupe.html', groupe=groupInfo, user=idUser, like=isInFavoris)

@app.route('/Profil/favoris/<idUser>/<idGroupe>/like')
def like(idUser, idGroupe):
    FAVORIS.Insert.insert_favoris(cnx, idUser, idGroupe)
    return redirect(url_for('groupe', idUser=idUser, idGroupe=idGroupe))

@app.route('/Profil/favoris/<idUser>/<idGroupe>/dislike')
def dislike(idUser, idGroupe):
    FAVORIS.Delete.delete_favoris(cnx, idUser, idGroupe)
    return redirect(url_for('groupe', idUser=idUser, idGroupe=idGroupe))
