from flask import render_template, url_for, redirect, request, session, jsonify, send_file
from .formulaire import LoginForm,RegisterForm
from flask_login import login_user, current_user, logout_user, login_required
from .app import app
from .requete import get_cnx , Spectateur


cnx = get_cnx()

@app.route("/")
def home():
    return render_template(
    "home.html",
    title="Home"
    )

@app.route("/Billeterie/")
def billeterie():
    return render_template(
    "billeterie.html",
    title="Home"
    )

@app.route("/Programme/")
def programme():
    return render_template(
    "programme.html",
    title="Home"
    )

@app.route("/Login/", methods=("GET","POST",))
def login():
    f = LoginForm ()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user != None:
            session['utilisateur'] = user
            print("login : "+str(session['utilisateur']))
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