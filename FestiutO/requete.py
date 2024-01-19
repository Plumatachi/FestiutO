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

class Evenement:
    class Get:
        def get_evenement_with_idSpectateur_journee(id):
            res = []
            result = cnx.execute(text("SELECT idJournee,nomJournee,dateDebutJ,nombreDePlace FROM JOURNEE natural join RESERVER WHERE idSpectateur = '" + id + "';"))
            for row in result:
                res.append((row[0],row[1],row[2],row[3]))
            
            return res
        
        def get_evenement_with_idSpectateur_Evenement(id):
            res = []
            result = cnx.execute(text("SELECT idEvenement,nomScene,dateDebutE,lieux,idConcert FROM EVENEMENT natural join SCENE natural join BILLETEVENEMENT WHERE idSpectateur = '" + id + "';"))
            for row in result:
                res.append((row[0],row[1],row[2],row[4]))
            
            return res

        def get_evenement_with_id(id):
            try:
                res = []
                result = cnx.execute(text("SELECT dateDebutE,lieux,nomScene FROM EVENEMENT natural join SCENE WHERE idEvenement = '" + id + "';"))
                for row in result:
                    res.append((row[0],row[1],row[2]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise


    class Insert:
        def insert_billet_evenement(idSpectateur,idEvenement):
            try:
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                cnx.execute(text("INSERT INTO BILLETEVENEMENT(idspectateur,idEvenement) VALUES ('" + str(idSpectateur) + "','" + str(idEvenement) + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion du favoris1")
                raise

class Journee:
    class Get:
        def get_journee_date():
            try:
                res = []
                result = cnx.execute(text("SELECT dateDebutJ,idJournee FROM JOURNEE;"))
                for row in result:
                    res.append((row[0],row[1]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise

    class Insert :
        def insert_journee(idJournee,idspectateur,nombrePlace,type):
            if(type == "3"):
                result = cnx.execute(text("SELECT idJournee FROM JOURNEE ;"))
                for id in result:
                    try:
                        cnx.execute(text("INSERT INTO RESERVER(idJournee,idspectateur,nombreDePlace) VALUES ('" + str(id) + "','" + str(idspectateur) + "','" + str(nombrePlace) + "');"))
                        cnx.commit()
                    except Exception as e:
                        print(e)
                        raise
            else:
                for id in idJournee.split(" ")[:-1]:    
                    try:
                        cnx.execute(text("INSERT INTO RESERVER(idJournee,idspectateur,nombreDePlace) VALUES ('" + str(id) + "','" + str(idspectateur) + "','" + str(nombrePlace) + "');"))
                        cnx.commit()
                    except Exception as e:
                        print(e)
                        raise
        
class Musicien:
    class Get:
        def get_info_Musicien(id):
            try:
                res = []
                result = cnx.execute(text("select nominstrupent,nom,nomDuGroupe from MUSICIEN natural join APPARTIENT natural join GROUPE natural join JOUE natural join INSTRUMENT where idMusicien = '" + id + "' ;"))
                for row in result:
                    print(row)
                    res.append((row[0],row[1],row[2],row[3]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise

        def get_musicien_with_idgroupe(cnx, idGroupe):
            try:
                result = cnx.execute(text("SELECT idMusicien,nom,nominstrupent,photo FROM MUSICIEN natural join GROUPE natural join JOUE natural join INSTRUMENT WHERE idgroupe = '" + idGroupe + "';"))
                musiciens = []
                for row in result:
                    musiciens.append((row[0],row[1],row[2],row[3]))
                return musiciens
            except:
                print("Erreur lors de la récupération du groupe")
                raise

        def get_musicien_with_id(cnx, id):
            try:
                result = cnx.execute(text("SELECT * FROM MUSICIEN WHERE idMusicien = '" + id + "';"))
                for row in result:
                    print(row)
                    return row
            except:
                print("Erreur lors de la récupération du musicien")
                raise

    class Insert:
        def insert_musicien(cnx, nom, adresse_mail, numero_tel, photo):
            try:
                cnx.execute(text("INSERT INTO MUSICIEN( nom, adresseMail, numeroTelMusicien, photo) VALUES ('" + nom + "', '" + adresse_mail + "', '" + numero_tel + "', '" + photo + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion du membre dans le groupe")
                raise
    
    class Update:
        def update_email_musicien(cnx, adresseMail, newAdresseMail):
            try:
                cnx.execute(text("UPDATE MUSICIEN SET adresseMail = '" + newAdresseMail + "' WHERE adresseMail = '" + adresseMail + "';"))
                cnx.commit()
                print(True)
            except:
                print("Erreur lors de la mise à jour du numéro de téléphone")
                raise
        def update_numeroTelephone_musicien(cnx, adresseMail, numeroTelephone):
            try:
                cnx.execute(text("UPDATE MUSICIEN SET numeroTelMusicien = '" + numeroTelephone + "' WHERE adresseMail = '" + adresseMail + "';"))
                cnx.commit()
                print(True)
            except:
                print("Erreur lors de la mise à jour du numéro de téléphone")
                raise   
        def update_nom_musicien(cnx, adresseMail, nom):
            try:
                cnx.execute(text("UPDATE MUSICIEN SET nom = '" + nom + "' WHERE adresseMail = '" + adresseMail + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du nom")
                raise       
            
    class Delete:
        
        def delete_musicien(cnx, idMusicien):
            try:
                cnx.execute(text("DELETE FROM APPARTIENT WHERE idMusicien = '" + idMusicien + "' AND idGroupe = '" + str(Groupe.Get.get_idGroupe_musicien_avec_son_idMusicien(cnx, idMusicien)) + "';")),
                Joue.Delete.delete_instru_musicien(cnx, idMusicien)
                cnx.execute(text("DELETE FROM MUSICIEN WHERE idMusicien = '" + idMusicien + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression du musicien")
                raise
               
class Spectateur:
    class Get:
        def get_all_spectateur(cnx):
            try:
                res = []
                result = cnx.execute(text("SELECT * FROM SPECTATEUR natural join TYPECOMPTE;"))
                for row in result:
                    res.append(row)
                return res
            except:
                print("erreur lors de la récupération des spectateurs")
                raise
                    
        def get_all_spectateur_avec_email(cnx, email):
            try:
                result = cnx.execute(text("SELECT idSpectateur,nom,numerotel,mail,motsDePasse,idTypeCompte, nomTypeCompte  FROM SPECTATEUR natural join TYPECOMPTE WHERE mail = '" + email + "';"))
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

        def get_spectateur_with_id(cnx, id):
            try:
                result = cnx.execute(text("SELECT * FROM SPECTATEUR WHERE idSpectateur = '" + id + "';"))
                for row in result:
                    print(row)
                    return row
            except:
                print("Erreur lors de la récupération du spectateur")
                raise

    class Insert:
        def insert_spectateur(cnx, nom, telephone, email, password, idTypeCompte):
            try:
                cnx.execute(text("INSERT INTO SPECTATEUR(nom,numerotel,mail,motsDePasse, idTypeCompte) VALUES ('" + nom + "', '" + telephone + "', '" + email + "', '" + password + "', '" + idTypeCompte + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion du spectateur")
                raise

    class Update:
        def update_numeroTelephone(cnx, email, numeroTelephone):
            try:
                cnx.execute(text("UPDATE SPECTATEUR SET numerotel = '" + numeroTelephone + "' WHERE mail = '" + email + "';"))
                cnx.commit()
                print(True)
            except:
                print("Erreur lors de la mise à jour du numéro de téléphone")
                raise
        
        def update_nom(cnx, mail, nom):
            try:
                cnx.execute(text("UPDATE SPECTATEUR SET nom = '" + nom + "' WHERE mail = '" + mail + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du nom")
                raise
            
        def update_mdp(cnx, email, password):
            try:
                cnx.execute(text("UPDATE SPECTATEUR SET motsDePasse = '" + password + "' WHERE mail = '" + email + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du mot de passe")
                raise

        def update_email(cnx, email, new_email):
            user = Spectateur.Get.get_all_spectateur_avec_email(cnx, email)
            idUser = user[1]
            try:
                cnx.execute(text("UPDATE SPECTATEUR SET mail = '" + new_email + "' where idSpectateur = '" + str(idUser) + "';"))
                cnx.commit()
            except:
                print( "Erreur lors de la mise à jour de l'email")
                raise

    class Delete:
        def delete_spectateur(cnx, id):
            try:
                cnx.execute(text("DELETE FROM SPECTATEUR WHERE idSpectateur = '" + id + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression du spectateur")
                raise

class FAVORIS:
    class GET:
        def get_favoris_with_idSpectateur(cnx, idSpectateur):
            try:
                res = []
                result = cnx.execute(text("SELECT nomDuGroupe,  reseausocial, photo, idgroupe  FROM FAVORIS natural join GROUPE WHERE idSpectateur = '" + idSpectateur + "';"))
                for row in result:
                    res1 = []
                    for elem in row:
                        if elem is None:
                            res1.append("None")
                        else:
                            res1.append(elem)
                    res.append(res1)
                return res
            except:
                print("Erreur lors de la récupération des favoris")
                raise
        
        def get_list_idgroupe_in_favoris_with_idSpectateur(cnx, idSpectateur):
            try:
                res = []
                result = cnx.execute(text("SELECT idgroupe FROM FAVORIS WHERE idSpectateur = '" + idSpectateur + "';"))
                for row in result:
                    res.append(row[0])
                return res
            except:
                print("Erreur lors de la récupération des favoris")
                raise

    class Insert:
        def insert_favoris(cnx, idSpectateur, idGroupe):
            try:
                cnx.execute(text("INSERT INTO FAVORIS(idSpectateur, idGroupe) VALUES ('" + idSpectateur + "', '" + idGroupe + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion du favoris2")
                raise

    class Delete:
        def delete_favoris(cnx, idSpectateur, idGroupe):
            try:
                cnx.execute(text("DELETE FROM FAVORIS WHERE idSpectateur = '" + idSpectateur + "' AND idGroupe = '" + idGroupe + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression du favoris")
                raise

class FONCTION:
    def idGroupe_in_like_with_idSpectateur(cnx, idSpectateur, idGroupe):
        try:
            list = FAVORIS.GET.get_list_idgroupe_in_favoris_with_idSpectateur(cnx, idSpectateur)
            print(list)
            print(idGroupe)
            if int(idGroupe) in list:
                return True
            else:
                return False
        except:
            print("Erreur lors de la récupération des favoris")
            raise

class Groupe:
    class Get: 
        def get_groupe_with_idgroupe(cnx, idgroupe):
            try:
                result = cnx.execute(text("SELECT * FROM GROUPE WHERE idgroupe = '" + idgroupe + "';"))
                for row in result:
                    groupe = []
                    for elem in row:
                        print(elem)
                        if elem is None:
                            groupe.append("None")
                        else:
                            groupe.append(elem)
                    
                    return groupe
            except:
                print("Erreur lors de la récupération du groupe")
                raise
            
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

        def get_consert_groupe(idGroupe):
            try:
                res = []
                result = cnx.execute(text("select dateDebutE,dateFinE,nomScene,lieux,idEvenement,idConcert from GROUPE natural join PARTICIPE natural join EVENEMENT natural join SCENE where idgroupe = '" + idGroupe + "' AND idConcert IS NOT NULL;"))
                for row in result:
                    print(row)
                    res.append((row[0],row[1],row[2],row[3],row[4],row[5]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise

        def get_activite_groupe(idGroupe):
            try:
                res = []
                result = cnx.execute(text("select dateDebutE,dateFinE,nomScene,lieux,idEvenement,idConcert from GROUPE natural join PARTICIPE natural join EVENEMENT natural join SCENE where idgroupe = '" + idGroupe + "' AND idActivite IS NOT NULL;"))
                for row in result:
                    print(row)
                    res.append((row[0],row[1],row[2],row[3],row[4],row[5]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise
            
        def get_idGroupe_musicien_avec_son_idMusicien(cnx, idMusicien):
            try:
                result = cnx.execute(text("SELECT idGroupe FROM JOUE WHERE idMusicien = '" + idMusicien + "';"))
                for row in result:
                    print(row[0])
                    return row[0]
            except:
                print("Erreur lors de la récupération du groupe")
                raise

    class Insert:
        def insert_groupe(cnx, nom_groupe, description, reseausocial, photo, nb_personne):
            try:
                cnx.execute(text("INSERT INTO GROUPE(nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES ('" + nom_groupe + "', '" + description + "', '" + reseausocial + "', '" + photo + "', '" + str(nb_personne) + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion du groupe")
                raise

class Joue:
    class Get:
        def get_instru_musicien(idMusicien):
            try:
                res = []
                result = cnx.execute(text("SELECT idInstrument FROM JOUE WHERE idMusicien = '" + idMusicien + "';"))
                for row in result:
                    res.append(row[0])
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise

    class Delete:
        def delete_instru_musicien(cnx, idMusicien):
            try:
                cnx.execute(text("DELETE FROM JOUE WHERE idMusicien = '" + idMusicien + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression du favoris")
                raise

class Scene:
    class Insert:
        def insert_scene(cnx, nom_scene, lieux):
            try:
                cnx.execute(text("INSERT INTO SCENE(nomScene, lieux) VALUES ('" + nom_scene + "', '" + lieux + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion de la scene")
                raise
    class Update:
        def update_scene(cnx,id, new_nom):
            try:
                cnx.execute(text("UPDATE SCENE SET nomScene = '" + new_nom + "' WHERE idScene = '" + id + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour de la scene")
                raise

        def update_lieu(cnx, id, new_nom):
            try:
                cnx.execute(text("UPDATE SCENE SET lieux = '" + new_nom + "' WHERE idScene = '" + id + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour de la scene")
                raise

    class Delete:
        def delete_scene(cnx, id):
            try:
                cnx.execute(text("DELETE FROM SCENE WHERE idScene = '" + id + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression de la scene")
                raise
    
    
            
    class Get:
        def get_scene_with_id(cnx, idScene):
            try:
                result = cnx.execute(text("SELECT * FROM SCENE WHERE idScene = '" + idScene + "';"))
                for row in result:
                    print(row)
                    return row
            except:
                print("Erreur lors de la récupération de la scène")
                raise
