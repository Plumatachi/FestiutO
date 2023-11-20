from sqlalchemy import text
from .connexionPythonSQL import ouvrir_connexion


cnx = ouvrir_connexion()

def get_cnx():
    return cnx


def afficher_table(cnx, table):
    try:
        list = []
        result = cnx.execute(text("SELECT * FROM " + table + ";"))
        for row in result:
            print(row)
            list.append(row)
        return list
    except:
        print("Erreur lors de l'affichage de la table")
        raise
    
class Spectateur:
    class Get:
        def get_nom_spectateur_avec_email(cnx, email):
            try:
                result = cnx.execute(text("SELECT nom FROM SPECTATEUR WHERE mail = '" + email + "';"))
                for row in result:
                    print(row[0])
                    return row[0]
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise
            
        def get_password_with_email(cnx, email):
            try:
                result = cnx.execute(text("SELECT motsDePasse FROM SPECTATEUR WHERE mail = '" + email + "';"))
                for row in result:
                    print(row[0])
                    return row[0]
            except:
                print("Erreur lors de la récupération du mot de passe de l'utilisateur")
                raise
    class Insert:
        def insert_spectateur(cnx, nom, telephone, email, password):
            try:
                cnx.execute(text("INSERT INTO SPECTATEUR(nom,numerotel,mail,motsDePasse) VALUES ('" + nom + "', '" + telephone + "', '" + email + "', '" + password + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion du spectateur")
                raise
        
