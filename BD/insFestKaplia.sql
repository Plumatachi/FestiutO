INSERT INTO FESTIVAL (idfestival, datedebut, datefin)
VALUES
    (1, '2023-07-15', '2023-07-19'),
    (2, '2023-08-15', '2023-08-20');


INSERT INTO SCENE (idScene, nomScene, lieux)
VALUES (1, 'Main Stage', 'Central Park');

INSERT INTO SCENE (idScene, nomScene, lieux)
VALUES (2, 'Rock Stage', 'West Field');

INSERT INTO SCENE (idScene, nomScene, lieux)
VALUES (3, 'Pop Stage', 'East Field');

INSERT INTO SCENE (idScene, nomScene, lieux)
VALUES (4, 'Electronic Stage', 'South Field');

INSERT INTO SCENE (idScene, nomScene, lieux)
VALUES (5, 'Mixt Stage', 'South Field');

INSERT INTO SCENE (idScene, nomScene, lieux)
VALUES (6, 'HardStyle Stage', 'South Field');


INSERT INTO JOURNEE (idJournee, nomJournee, dateDebutJ, dateFinJ, idfestival)
VALUES
    (1, 'Opening Day', '2023-07-15', '2023-07-15', 1),
    (2, 'Rock Day', '2023-07-16', '2023-07-16', 1),
    (3, 'Pop Day', '2023-07-17', '2023-07-17', 1),
    (4, 'Electronic Day', '2023-08-18', '2023-08-18', 2),
    (5, 'Closing Day', '2023-08-19', '2023-08-19', 2);


INSERT INTO ACTIVITE (idActivite, nomactivite, privatitation)
VALUES
    (1, 'Concert', 'Publique'),
    (2, 'Rencontre avec les artistes', 'Privée'),
    (3, 'Atelier de musique', 'Publique'),
    (4, 'Conférence', 'Publique'),
    (5, 'Exposition', 'Publique');

INSERT INTO CONCERT (idConcert, demontage, montage)
VALUES
    (1, 30, 60),
    (2, 120, 120),
    (3, 45 , 60),
    (4, 60 , 120);




INSERT INTO EVENEMENT (idEvenement, dateDebutE, dateFinE, idScene, idJournee, idActivite, idConcert)
VALUES (2, '2023-07-17 18:00:00', '2023-07-17 20:00:00', 3, 3, NULL, 2);

INSERT INTO EVENEMENT (idEvenement, dateDebutE, dateFinE, idScene, idJournee, idActivite, idConcert)
VALUES (3, '2023-08-18 22:00:00', '2023-08-18 23:00:00', 2, 4, NULL, 3);

INSERT INTO EVENEMENT (idEvenement, dateDebutE, dateFinE, idScene, idJournee, idActivite, idConcert)
VALUES (4, '2023-08-19 12:00:00', '2023-08-19 14:00:00', 1, 5, 1, NULL);


INSERT INTO EVENEMENT (idEvenement, dateDebutE, dateFinE, idScene, idJournee, idActivite, idConcert)
VALUES
(10, '2023-07-15 19:00:00', '2023-07-15 20:00:00', 5, 1, NULL, 1);

INSERT INTO EVENEMENT (idEvenement, dateDebutE, dateFinE, idScene, idJournee, idActivite, idConcert)
VALUES
(9, '2023-07-15 21:00:00', '2023-07-15 23:00:00', 5, 1, 2, NULL);



INSERT INTO SPECTATEUR (idspectateur, nom, numerotel, mail,motsDePasse)
VALUES
    (1, 'Spectateur 1', '1234567890', 'spectateur1@example.com',"151654161246"),
    (3, 'Spectateur 3', '1464565465', 'spectateur3@example.com',"161684321315"),
    (4, 'Spectateur 4', '9461616160', 'spectateur4@example.com',"1019465031354"),
    (5, 'Spectateur 5', '6494198848', 'spectateur5@example.com',"25406034841649"),
    (2, 'Spectateur 2', '9876543210', 'spectateur2@example.com',"60164849410148");

-- INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
-- (1,'Les Rolling Stones', 'Un groupe de rock britannique formé à Londres en 1962.', 'twitter.com/rollingstones', NULL, 4);

-- INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
-- (2,'The Beatles', 'Un groupe de rock britannique formé à Liverpool en 1960.', 'twitter.com/thebeatles', NULL, 4);

-- INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
-- (3,'AC/DC', 'Un groupe de hard rock australien formé à Sydney en 1973.', 'twitter.com/acdc', NULL, 4);

-- INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
-- (4,'Metallica', 'Un groupe de thrash metal américain formé à Los Angeles en 1981.', 'twitter.com/metallica', NULL, 4);

-- INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
-- (5,'Pink Floyd', 'Un groupe de rock progressif britannique formé à Londres en 1965.', 'twitter.com/pinkfloyd', NULL, 4);

-- lancer le fichier python avant de continuer

INSERT INTO PARTICIPE (idEvenement, idGroupe)
VALUES
    (10, 1),
    (2, 1),
    (3, 3),
    (4, 4);



INSERT INTO RESERVER (idspectateur, idJournee)
VALUES
    (1, 1),
    (1, 2),
    (3, 3),
    (4, 4),
    (5, 5);

INSERT INTO BILLETEVENEMENT (idspectateur, idEvenement)
VALUES
    (1, 10),
    (1, 3),
    (3, 3),
    (4, 4);


INSERT INTO STYLEDEMUSIQUE (typeDeMusique) VALUES
    ("Rock"),
    ("Hard Rock"),
    ("Trash Metal"),
    ("Rock Progressif");


INSERT INTO STYLE (idgroupe, typeDeMusique) VALUES 
    (1,"Rock"),
    (2,"Rock"),
    (3,"Hard Rock"),
    (4,"Trash Metal"),
    (5,"Rock Progressif"); 

INSERT INTO RESSEMBLE (typeDeMusique, typeDeMusique2) VALUES
    ("Rock","Rock Progressif"),
    ("Hard Rock","Trash Metal");

INSERT INTO INSTRUMENT(idinstrument, nominstrupent) VALUES
    (1, "Guitare"),
    (2, "Chant"),
    (3,"Basse"),
    (4,"Batterie");

INSERT INTO MUSICIEN (idMusicien, nom, adresseMail, numeroTelMusicien) VALUES
    (1, 'Mick Jagger', 'mick@rollingstones.com', 0612345678),

    (2, 'Keith Richards', 'keith@rollingstones.com', 0678901234),

    (3, 'Charlie Watts', 'charlie@rollingstones.com', 0654321098),

    (4, 'Ronnie Wood', 'ronnie@rollingstones.com', 0665432109),

    (5, 'John Lennon', 'john@beatles.com', 0612345778),

    (6, 'Paul McCartney', 'paul@beatles.com', 0677901234),

    (7, 'George Harrison', 'george@beatles.com', 0654321099),

    (8, 'Ringo Starr', 'ringo@beatles.com', 0765432109),

    (9, 'Angus Young', 'angus@acdc.com', 0662345678),

    (10, 'Malcolm Young', 'malcolm@acdc.com', 0678911234),

    (11, 'Brian Johnson', 'brian@acdc.com', 0674321098),

    (12, 'Cliff Williams', 'cliff@acdc.com', 0666432109),

    (13, 'James Hetfield', 'james@metallica.com', 0612345618),

    (14, 'Lars Ulrich', 'lars@metallica.com', 0678901334),

    (15, 'Kirk Hammett', 'kirk@metallica.com', 0654331098),

    (16, 'Robert Trujillo', 'robert@metallica.com', 0667432109),

    (17, 'Roger Waters', 'roger@pinkfloyd.com', 0712345678),

    (18, 'David Gilmour', 'david@pinkfloyd.com', 0678901214),

    (19, 'Richard Wright', 'richard@pinkfloyd.com', 0654821098),

    (20, 'Nick Mason', 'nick@pinkfloyd.com', 0765432110);

INSERT INTO APPARTIENT(idGroupe, idMusicien) VALUES
    (1,1),
    (1,2),
    (1,3),
    (1,4),
    (2,5),
    (2,6),
    (2,7),
    (2,8),
    (3,9),
    (3,10),
    (3,11),
    (3,12),
    (4,13),
    (4,14),
    (4,15),
    (4,16),
    (5,17),
    (5,18),
    (5,19),
    (5,20);


INSERT INTO JOUE (idgroupe, idinstrument, idMusicien) VALUES 
    (1, 1, 1),

    (1, 2, 2),

    (1, 3, 3),

    (1, 4, 4),

    (2, 1, 5),

    (2, 2, 6),

    (2, 3, 7),

    (2, 4, 8),

    (3, 1, 9),

    (3, 2, 10),

    (3, 3, 11),

    (3, 4, 12),

    (4, 1, 13),

    (4, 2, 14),

    (4, 3, 15),

    (4, 4, 16),

    (5, 1, 17),

    (5, 2, 18),

    (5, 3, 19),

    (5, 4, 20);

INSERT INTO HEBERGEMENT(idhebergement, nbplace, lieux) VALUES
    (1, 150, "Manhattan"),
    (2, 100, "Queens"),
    (3, 80, "Bronks"),
    (4, 200, "Brooklyn");

INSERT INTO DORMIR(nbPersonneGroupe, dateArrivee, dateDepart, idgroupe, idhebergement) VALUES
    (4, '2023-07-15', '2023-07-19', 1, 1),
    (4, '2023-07-15', '2023-07-19', 2, 2),
    (4, '2023-07-15', '2023-07-19', 3, 4),
    (4, '2023-07-15', '2023-07-19', 4, 3),
    (4, '2023-07-15', '2023-07-19', 5, 1);
    



INSERT INTO PRESENT (idfestival, idgroupe, datearriver, datedepart) VALUES
    (1,1,'2023-07-15','2023-07-19'),
    (1,2,'2023-07-16','2023-07-19'),
    (2,3,'2023-08-15','2023-08-19'),
    (2,4,'2023-08-17','2023-08-19'),
    (1,5,'2023-07-15','2023-07-19'),
    (2,5,'2023-08-18','2023-08-19');




