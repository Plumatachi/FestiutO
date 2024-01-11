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
    
    
class Journee:
    class Get:
        def get_journee_date():
            try:
                res = []
                result = cnx.execute(text("SELECT dateDebutJ FROM JOURNEE;"))
                for row in result:
                    res.append(row[0])
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise
        
        
class Groupe:
    class Get:
        def get_images_groupe():
            try:
                res = []
                result = cnx.execute(text("SELECT photo,idgroupe,nomDuGroupe FROM GROUPE;"))
                for row in result:
                    print(row)
                    res.append((row[0],row[1],row[2]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise
            
            
        def get_activite_groupe(idGroupe):
            try:
                res = []
                result = cnx.execute(text("select dateDebutE,dateFinE,nomScene from GROUPE natural join PARTICIPE natural join EVENEMENT natural join SCENE where idgroupe = '" + idGroupe + "' AND idConcert IS NOT NULL;"))
                for row in result:
                    print(row)
                    res.append((row[0],row[1],row[2]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise
        
        
class Spectateur:
    class Get:
        def get_all_spectateur_avec_email(cnx, email):
            try:
                result = cnx.execute(text("SELECT * FROM SPECTATEUR WHERE mail = '" + email + "';"))
                for row in result:
                    print (row)
                    return row
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
    class Update:
        def update_mdp(cnx, email, password):
            try:
                cnx.execute(text("UPDATE SPECTATEUR SET motsDePasse = '" + password + "' WHERE mail = '" + email + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du mot de passe")
                raise

        def update_email(cnx, email, new_email):
            try:
                cnx.execute(text("UPDATE SPECTATEUR SET mail = '" + new_email + "' where mail = '" + email + "';"))
                cnx.commit()
            except:
                print( "Erreur lors de la mise à jour de l'email")
                raise