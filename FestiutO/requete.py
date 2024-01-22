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
        def afficher_evenement_concert(cnx):
            try:
                res = []
                result = cnx.execute(text("SELECT idEvenement,nomDuGroupe,photo,nomScene FROM EVENEMENT natural join CONCERT natural join SCENE natural join PARTICIPE natural join GROUPE;"))
                for row in result:
                    res.append(row)
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise    
        
        def afficher_evenement_activite(cnx):
            try:
                res = []
                result = cnx.execute(text("SELECT idEvenement,nomDuGroupe,photo,nomScene,nomActivite FROM EVENEMENT natural join ACTIVITE  natural join SCENE natural join PARTICIPE natural join GROUPE;"))
                for row in result:
                    res.append(row)
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise    

        def get_evenement_concert(cnx,idEvenement):
            try:
                res = []
                result = cnx.execute(text("SELECT idEvenement,nomDuGroupe,photo,nomScene,montage,demontage,dateDebutE,dateFinE FROM EVENEMENT natural join CONCERT natural join SCENE natural join PARTICIPE natural join GROUPE WHERE idEvenement = '" + idEvenement + "';"))
                for row in result:
                    res.append(row)
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise

        def get_evenement_activite(cnx,idEvenement):
            try:
                res = []
                result = cnx.execute(text("SELECT idEvenement,nomDuGroupe,photo,nomScene,nomActivite,privatitation,dateDebutE,dateFinE FROM EVENEMENT natural join ACTIVITE natural join SCENE natural join PARTICIPE natural join GROUPE WHERE idEvenement = '" + idEvenement + "';"))
                for row in result:
                    res.append(row)
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise



    class Update:
        def update_evenement_groupe(cnx, idEvenement, nomGroupe):
            try:
                # Récupérer l'idGroupe
                idGroupe = cnx.execute(text("SELECT idGroupe FROM GROUPE WHERE nomDuGroupe = :nomGroupe"), {"nomGroupe": nomGroupe}).scalar()

                # Mettre à jour la participation
                cnx.execute(text("UPDATE PARTICIPE SET idGroupe = :idGroupe WHERE idEvenement = :idEvenement"), {"idGroupe": idGroupe, "idEvenement": idEvenement})

                cnx.commit()
            except Exception as e:
                print("Erreur lors de la mise à jour du concert:", str(e))
                cnx.rollback()
                raise
        def update_evenement_scene(cnx, idEvenement, nomScene):
            try:
                # Récupérer l'idScene
                print(nomScene)
                idScene = cnx.execute(text("SELECT idScene FROM SCENE WHERE nomScene = :nomScene"), {"nomScene": nomScene}).scalar()

                # Mettre à jour la participation
                cnx.execute(text("UPDATE EVENEMENT SET idScene = :idScene WHERE idEvenement = :idEvenement"), {"idScene": idScene, "idEvenement": idEvenement})

                cnx.commit()
            except Exception as e:
                print("Erreur lors de la mise à jour du concert:", str(e))
                cnx.rollback()
                raise
        def update_evenement_montage(cnx, idEvenement, montage):
            try:
                idConsert = cnx.execute(text("select idConcert from EVENEMENT where idEvenement = '" + idEvenement + "';"))
                cnx.execute(text("UPDATE CONCERT SET montage = :montage WHERE idConcert = :idConcert"), {"montage": montage, "idConcert": idConsert})
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du Evenement")
                raise

        def update_evenement_demontage(cnx, idEvenement, montage):
            try:
                idConsert = cnx.execute(text("select idConcert from EVENEMENT where idEvenement = '" + idEvenement + "';"))
                cnx.execute(text("UPDATE CONCERT SET montage = :montage WHERE idConcert = :idConcert"), {"montage": montage, "idConcert": idConsert})
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du Evenement")
                raise

        def update_evenement_dateDebut(cnx, idEvenement, dateDebutE):
            try:
                cnx.execute(text("UPDATE EVENEMENT SET dateDebutE = :dateDebutE WHERE idEvenement = :idEvenement"), {"dateDebutE": dateDebutE, "idEvenement": idEvenement})
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du Evenement")
                raise

        def update_evenement_dateFin(cnx, idEvenement, dateFinE):
            try:
                cnx.execute(text("UPDATE EVENEMENT SET dateFinE = :dateFinE WHERE idEvenement = :idEvenement"), {"dateFinE": dateFinE, "idEvenement": idEvenement})
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du Evenement")
                raise

        def update_evenement_nomActivite(cnx, idEvenement, nomActivite):
            try:
                idActivite = cnx.execute(text("select idActivite from EVENEMENT where idEvenement = '" + idEvenement + "';"))
                cnx.execute(text("UPDATE ACTIVITE SET nomActivite = :nomActivite WHERE idActivite = :idActivite"), {"nomActivite": nomActivite, "idActivite": idActivite})
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du Evenement")
                raise

        def update_evenement_privatisation(cnx, idEvenement, privatitation):
            try:
                idActivite = cnx.execute(text("select idActivite from EVENEMENT where idEvenement = '" + idEvenement + "';"))
                cnx.execute(text("UPDATE ACTIVITE SET privatitation = :privatitation WHERE idActivite = :idActivite"), {"privatitation": privatitation, "idActivite": idActivite})
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du Evenement")
                raise

    class Delete:
        def delete_evenement(cnx, idEvenement):
            try:
                cnx.execute(text("DELETE FROM BILLETEVENEMENT WHERE idEvenement = '" + idEvenement + "';"))
                cnx.execute(text("DELETE FROM PARTICIPE WHERE idEvenement = '" + idEvenement + "';"))
                cnx.execute(text("DELETE FROM EVENEMENT WHERE idEvenement = '" + idEvenement + "';"))
                cnx.execute(text("DELETE FROM CONCERT WHERE idConcert IN (SELECT idConcert FROM EVENEMENT WHERE idEvenement = + '" + idEvenement + "');"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression de l'evenement")
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

        def insert_concert(cnx, nomGroupe,montage ,demontage , dateDebutE, dateFinE,scene,nomJournee):
            try:
                # Récupérer l'idScene
                idScene = cnx.execute(text("SELECT idScene FROM SCENE WHERE nomScene = :scene"), {"scene": scene}).scalar()

                # Récupérer l'idJournee
                idJournee = cnx.execute(text("SELECT idJournee FROM JOURNEE WHERE nomJournee = :nomJournee"), {"nomJournee": nomJournee}).scalar()

                # Insérer le concert
                cnx.execute(text("INSERT INTO CONCERT(montage, demontage) VALUES (:montage, :demontage)"), {"montage": montage, "demontage": demontage})

                # Récupérer l'idConcert
                idConcert = cnx.execute(text("SELECT idConcert FROM CONCERT ORDER BY idConcert DESC LIMIT 1")).scalar()

                # Insérer l'événement
                cnx.execute(text("INSERT INTO EVENEMENT(dateDebutE, dateFinE, idScene, idJournee, idActivite, idConcert) VALUES (:dateDebutE, :dateFinE, :idScene, :idJournee, NULL, :idConcert)"),
                            {"dateDebutE": dateDebutE, "dateFinE": dateFinE, "idScene": idScene, "idJournee": idJournee, "idConcert": idConcert})

                # Récupérer l'idEvenement
                idEvenement = cnx.execute(text("SELECT idEvenement FROM EVENEMENT ORDER BY idEvenement DESC LIMIT 1")).scalar()

                # Récupérer l'idGroupe
                idGroupe = cnx.execute(text("SELECT idGroupe FROM GROUPE WHERE nomDuGroupe = :nomGroupe"), {"nomGroupe": nomGroupe}).scalar()

                # Insérer la participation
                cnx.execute(text("INSERT INTO PARTICIPE(idEvenement, idGroupe) VALUES (:idEvenement, :idGroupe)"),
                            {"idEvenement": idEvenement, "idGroupe": idGroupe})

                cnx.commit()
            except Exception as e:
                print("Erreur lors de l'insertion du concert:", str(e))
                cnx.rollback()
                raise

        def insert_activite(cnx, nomGroupe, privatitation, dateDebutE, dateFinE, scene, nomJournee, nomActivite):
            try:
                # Récupérer l'idScene
                idScene = cnx.execute(text("SELECT idScene FROM SCENE WHERE nomScene = :scene"), {"scene": scene}).scalar()

                # Récupérer l'idJournee
                idJournee = cnx.execute(text("SELECT idJournee FROM JOURNEE WHERE nomJournee = :nomJournee"), {"nomJournee": nomJournee}).scalar()

                # Insérer l'activité
                cnx.execute(text("INSERT INTO ACTIVITE(nomActivite, privatitation) VALUES (:nomActivite, :privatitation)"),
                            {"nomActivite": nomActivite, "privatitation": privatitation})

                # Récupérer l'idActivite
                idActivite = cnx.execute(text("SELECT idActivite FROM ACTIVITE ORDER BY idActivite DESC LIMIT 1")).scalar()

                # Insérer l'événement
                cnx.execute(text("INSERT INTO EVENEMENT(dateDebutE, dateFinE, idScene, idJournee, idActivite, idConcert) VALUES (:dateDebutE, :dateFinE, :idScene, :idJournee, :idActivite, NULL)"),
                            {"dateDebutE": dateDebutE, "dateFinE": dateFinE, "idScene": idScene, "idJournee": idJournee, "idActivite": idActivite})

                # Récupérer l'idEvenement
                idEvenement = cnx.execute(text("SELECT idEvenement FROM EVENEMENT ORDER BY idEvenement DESC LIMIT 1")).scalar()

                # Récupérer l'idGroupe
                idGroupe = cnx.execute(text("SELECT idGroupe FROM GROUPE WHERE nomDuGroupe = :nomGroupe"), {"nomGroupe": nomGroupe}).scalar()

                # Insérer la participation
                cnx.execute(text("INSERT INTO PARTICIPE(idEvenement, idGroupe) VALUES (:idEvenement, :idGroupe)"),
                            {"idEvenement": idEvenement, "idGroupe": idGroupe})

                cnx.commit()
            except Exception as e:
                print("Erreur lors de l'insertion de l'activité:")

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
        def get_all_musicien_not_in_groupe(cnx, idGroupe):
            try:
                res = []
                result = cnx.execute(text("SELECT idMusicien,nom FROM MUSICIEN WHERE idMusicien NOT IN (SELECT idMusicien FROM APPARTIENT WHERE idGroupe = '" + idGroupe + "');"))
                for row in result:
                    res.append((row[0],row[1]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise

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

        def get_id_musicien_with_nom(cnx, nom):
            try:
                result = cnx.execute(text("SELECT idMusicien FROM MUSICIEN  WHERE nom = '" + nom + "';"))
                for row in result:
                    return row[0]
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
                liste_groupe = Groupe.Get.get_groupe_with_idMusicien(cnx, idMusicien)
                for groupe in liste_groupe:
                    cnx.execute(text("DELETE FROM APPARTIENT WHERE idMusicien = '" + idMusicien + "' AND idGroupe = '" + str(groupe[0]) + "';")),
                Joue.Delete.delete_instru_musicien(cnx, idMusicien)
                cnx.execute(text("DELETE FROM MUSICIEN WHERE idMusicien = '" + idMusicien + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression du musicien")
                raise
class Hebergement:
    class Get:

        def get_bool_hebergement_groupe(cnx, idGroupe):
            try:
                result = cnx.execute(text("SELECT idHebergement FROM DORMIR WHERE idGroupe = '" + idGroupe + "';"))
                for row in result:
                    return True
                return False
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise

        def get_all_hebergement(cnx):
            try:
                res = []
                result = cnx.execute(text("SELECT * FROM HEBERGEMENT;"))
                for row in result:
                    res.append(row)
                return res
            except:
                print("Erreur lors de la récupération des hebergements")
                raise

        def get_hebergement_with_id(cnx, id):
            try:
                result = cnx.execute(text("SELECT * FROM HEBERGEMENT WHERE idHebergement = '" + id + "';"))
                for row in result:
                    print(row)
                    return row
            except:
                print("Erreur lors de la récupération de l'hebergement")
                raise
    class Insert:
        def insert_hebergement(cnx, nbplace, nom):
            try:
                cnx.execute(text("INSERT INTO HEBERGEMENT(nbplace, lieux) VALUES ('" + str(nbplace) + "', '" + nom + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion de l'hebergement")
                raise
    class Update:

        def update_nom_hebergement(cnx,id, new_nom):
            try:
                cnx.execute(text("UPDATE HEBERGEMENT SET lieux = '" + new_nom + "' WHERE idHebergement = '" + id + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour de l'hebergement")
                raise

        def update_place_hebergement(cnx,id, new_place):
            try:
                cnx.execute(text("UPDATE HEBERGEMENT SET nbplace = '" + str(new_place) + "' WHERE idHebergement = '" + id + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour de l'hebergement")
                raise
    class Delete:
        def delete_hebergement(cnx, id):
            try:
                cnx.execute(text("DELETE FROM DORMIR WHERE idHebergement = '" + id + "';"))
                cnx.execute(text("DELETE FROM HEBERGEMENT WHERE idHebergement = '" + id + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression de l'hebergement")
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
                cnx.execute(text("INSERT INTO SPECTATEUR(nom,numerotel,mail,motsDePasse, idTypeCompte) VALUES ('" + nom + "', '" + telephone + "', '" + email + "', '" + password + "', '" + str(idTypeCompte) + "');"))
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
                cnx.execute(text("DELETE FROM RESERVER WHERE idSpectateur = '" + id + "';"))
                cnx.execute(text("DELETE FROM BILLETEVENEMENT WHERE idSpectateur = '" + id + "';"))
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
        def get_groupe_with_nom(cnx, nom):
            try:
                result = cnx.execute(text("SELECT * FROM GROUPE WHERE nomDuGroupe = '" + nom + "';"))
                for row in result:
                    return row
            except:
                print("Erreur lors de la récupération du groupe")
                raise

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

        def get_membre_groupe(cnx, idGroupe):
            try:
                res = []
                result = cnx.execute(text("SELECT * FROM MUSICIEN natural join APPARTIENT WHERE idGroupe = '" + idGroupe + "';"))
                for row in result:
                    res.append(row)
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
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

        def get_groupe_with_idMusicien(cnx, idMusicien):
            try:
                res =  []
                result = cnx.execute(text("SELECT * FROM GROUPE natural join APPARTIENT WHERE idMusicien = '" + idMusicien + "';"))
                for row in result:
                    res.append(row)
                return res
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

    class Update:
        def update_description(cnx, idgroupe, description):
            try:
                cnx.execute(text("UPDATE GROUPE SET description = '" + description + "' WHERE idgroupe = '" + idgroupe + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour de la description")
                raise

        def update_nom_groupe(cnx, idgroupe, nom_groupe):
            try:
                cnx.execute(text("UPDATE GROUPE SET nomDuGroupe = '" + nom_groupe + "' WHERE idgroupe = '" + idgroupe + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la mise à jour du nom du groupe")
                raise
    class Delete:
        def delete_membre_groupe(cnx, idGroupe, idMusicien):
            try:
                cnx.execute(text("DELETE FROM APPARTIENT WHERE idGroupe = '" + idGroupe + "' AND idMusicien = '" + idMusicien + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression du membre")
                raise

        def delete_groupe(cnx, idGroupe):
            try:
                cnx.execute(text("DELETE FROM DORMIR WHERE idGroupe = '" + idGroupe + "';"))
                listeMembre = Groupe.Get.get_membre_groupe(cnx, idGroupe)
                for membre in listeMembre:
                    cnx.execute(text("DELETE FROM JOUE WHERE idMusicien = '" + str(membre[0]) + "';"))
                cnx.execute(text("DELETE FROM APPARTIENT WHERE idGroupe = '" + idGroupe + "';"))
                cnx.execute(text("DELETE FROM PARTICIPE WHERE idGroupe = '" + idGroupe + "';"))
                cnx.execute(text("DELETE FROM PRESENT WHERE idGroupe = '" + idGroupe + "';"))
                cnx.execute(text("DELETE FROM STYLE WHERE idGroupe = '" + idGroupe + "';"))
                cnx.execute(text("DELETE FROM GROUPE WHERE idGroupe = '" + idGroupe + "';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression du groupe")
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
class Appartient:
    class Insert:
        def insert_membre(cnx, idMusicien, idGroupe):
            try:
                cnx.execute(text("INSERT INTO APPARTIENT(idGroupe, idMusicien ) VALUES ('" + str(idGroupe) + "', '" + str(idMusicien) + "');"))
                cnx.commit()
            except:
                print("Erreur lors de l'insertion du membre dans le groupe")
                raise


class Reserver:
    class Get:

        def afficher_billet_festival(cnx):
            try:
                res = []
                result = cnx.execute(text("SELECT idSpectateur,idJournee,nombreDePlace,nomJournee , mail FROM RESERVER natural join JOURNEE natural join SPECTATEUR ;"))
                for row in result:
                    res.append((row[0],row[1],row[2],row[3],row[4]))
                return res
            except:
                print("Erreur lors de la récupération du nom de l'utilisateur")
                raise


        def get_Billet(cnx, idpectateur,idJournee):
            try:
                result = cnx.execute(text("SELECT * FROM RESERVER WHERE idSpectateur = '" + idpectateur + "'and idJournee ='"+idJournee+"';"))
                for row in result:
                    print(row)
                    return row
            except:
                print("Erreur lors de la récupération du billet")
                raise

    class Delete:
        def delete_billet(cnx, idSpectateur,idJournee):
            try:
                cnx.execute(text("DELETE FROM RESERVER WHERE idSpectateur = '" + idSpectateur + "'and idJournee ='"+idJournee+"';"))
                cnx.commit()
            except:
                print("Erreur lors de la suppression du billet")
                raise

    class Update:
        def update_journee(cnx, idSpectateur, oldIdJournee,nomJournee):
            try:
                # Récupérer l'idJournee à partir du nomJournee
                result = cnx.execute(text("SELECT idJournee FROM JOURNEE WHERE nomJournee = :nomJournee"), {"nomJournee": nomJournee})
                idJournee= result.scalar()  # Utiliser scalar() pour obtenir la valeur unique

                # Mettre à jour RESERVER avec le nouvel idJournee
                cnx.execute(text("UPDATE RESERVER SET idJournee = :idJournee WHERE idSpectateur = :idSpectateur AND idJournee = :oldIdJournee"), {"idJournee": idJournee, "idSpectateur": idSpectateur, "oldIdJournee": oldIdJournee})
                
                cnx.commit()
            except Exception as e:
                print("Erreur lors de la mise à jour du billet:", str(e))
                raise
