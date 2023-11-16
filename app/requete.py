from sqlalchemy import text
from connexionPythonSQL import ouvrir_connexion


cnx = ouvrir_connexion()

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