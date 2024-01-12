from flask import render_template, url_for, redirect, request, session, jsonify, send_file
from .formulaire import CalendarForm, LoginForm, ModifierEmailForm, ModifierMdpForm,RegisterForm
from flask_login import login_user, current_user, logout_user, login_required
from .app import app
from .requete import get_cnx , Spectateur ,Groupe, Journee , Musicien


cnx = get_cnx()

@app.route("/")
def home():
    listeImageId = Groupe.Get.get_images_groupe()
    return render_template(
    "acceuil.html",
    title="Home",
    lireImage= listeImageId
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
    listeImageId = Groupe.Get.get_images_groupe()
    return render_template(
    "programme.html",
    title="Home",
    lireImage= listeImageId
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
    profil_id = session['utilisateur']
    print("profil : "+str(profil_id))
    return render_template( "profil.html", title="Profil", profil_id=profil_id)

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

@app.route('/Profil/favoris')
def favoris():
    return render_template('favoris.html')


@app.route('/get_Info_journee_Groupe', methods=['GET'])
def get_Info_journee_Groupe():
     param1 = request.args.get('idgroupe')
     listeInfo = Groupe.Get.get_consert_groupe(param1)
     return jsonify(listeInfo)
 

@app.route('/get_Info_journee_activiter', methods=['GET'])
def get_Info_journee_Groupe():
     param1 = request.args.get('idgroupe')
     listeInfo = Groupe.Get.get_activite_groupe(param1)
     return jsonify(listeInfo)



