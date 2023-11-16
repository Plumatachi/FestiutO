from sqlalchemy import text
from connexionPythonSQL import ouvrir_connexion


cnx = ouvrir_connexion()

def afficher_table(cnx, table):
    try:
        res = []
        result = cnx.execute(text("SELECT * FROM " + table + ";"))
        for row in result:
            print(row)
            res.append(row)
        return res
    except:
        print( "La classe Requete a rencontré une erreur lors de l'affichage de la table " + table + ".")
        raise

class Utilisateur:
        def get_tout_utilisateurs(cnx):
            try:
                res = []
                result = cnx.execute(text("SELECT * FROM SPECTATEUR;"))
                for row in result:
                    print(row)
                    res.append(row)
                return res
            except:
                print("La classe Requete a rencontré une erreur lors de l'affichage de tous les utilisateurs.")
                raise

Utilisateur.get_tout_utilisateurs(cnx)