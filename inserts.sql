
INSERT INTO SPECTATEUR (idspectateur, nom, numerotel, mail)
VALUES
    (1, 'Spectateur 1', '1234567890', 'spectateur1@example.com'),
    (3, 'Spectateur 3', '1464565465', 'spectateur3@example.com'),
    (4, 'Spectateur 4', '9461616160', 'spectateur4@example.com'),
    (5, 'Spectateur 5', '6494198848', 'spectateur5@example.com'),
    (2, 'Spectateur 2', '9876543210', 'spectateur2@example.com');




INSERT INTO INSTRUMENT (idinstrument, nominstrupent)
VALUES
    (1, 'flute'),
    (3, 'harpe'),
    (2, 'gitard');


INSERT INTO HEBERGEMENT (idhebergement, nbplace, lieux)
VALUES
    (1, 50, 'Lieu 1'),
    (2, 30, 'Lieu 2');

INSERT INTO GROUPE (idgroupe,nomDuGroupe, description, reseausocial, photo, nbpersone, idhebergement)
VALUES
    (1,"imagine dragons" ,'Description du groupe 1', 'insta', 'photo1.jpg', 5, 1),
    (2,"johnny hallyday", 'Description du groupe 2', 'twitter', 'photo2.jpg', 4, 2);


    INSERT INTO JOUE (idgroupe, idinstrument)
VALUES
    (1, 1),
    (1, 2),
    (2, 1);

INSERT INTO STYLE (idgroupe, typestyle)
VALUES
    (1, 'hard'),
    (2, 'rap');
    -- (1, 'electro');

INSERT INTO FESTIVAL (idfestival, datedebut, datefin)
VALUES
    (1, '2023-09-14', '2023-09-16'),
    (2, '2023-09-15', '2023-09-19');

INSERT INTO PRESENT (idfestival, idgroupe, datearriver, datedepart)
VALUES
    (1, 1, '2023-09-13', '2023-09-17'),
    (1, 2, '2023-09-14', '2023-09-16'),
    (2, 1, '2023-09-14', '2023-09-18');

INSERT INTO CONCERT (idConcert, dateC, heureC, idgroupe, tarif, demontage, montage, duree)
VALUES
    (1, '2023-09-15', 18, 1, 25, 2, 3, 3),
    (2, '2023-09-16', 20, 2, 0, 2, 3, 4),
    (3, '2023-09-17', 19, 1, 2, 2, 3, 2);

INSERT INTO BILLET (idspectateur, idfestival, type)
VALUES
    (1, 1,  2),
    (2, 1,  1),
    (3, 2,  4);

INSERT INTO ACTIVITE (idActivite, idgroupe, dateA, heureA,duree, nomactivite, privatitation)
VALUES
    (1, 1, '2023-09-14', 15 ,1, 'radio', 'private'),
    (2, 2, '2023-09-15', 16 ,3, 'showcase', 'public'),
    (3, 1, '2023-09-16', 14 ,2, 'autographe', 'public');