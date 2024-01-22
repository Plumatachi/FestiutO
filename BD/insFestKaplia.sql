INSERT INTO FESTIVAL (datedebut, datefin)
VALUES
    ('2023-07-15', '2023-07-19'),
    ('2023-08-15', '2023-08-20');


INSERT INTO SCENE (nomScene, lieux)
VALUES ('Main Stage', 'Central Park'),
       ('Rock Stage', 'West Field'),
       ('Pop Stage', 'East Field'),
       ('Electronic Stage', 'South Field'),
       ('Mixt Stage', 'South Field'),
       ('HardStyle Stage', 'South Field');


INSERT INTO JOURNEE (nomJournee, dateDebutJ, dateFinJ, idfestival)
VALUES
    ('Opening Day', '2023-07-15', '2023-07-15', 1),
    ('Rock Day', '2023-07-16', '2023-07-16', 1),
    ('Pop Day', '2023-07-17', '2023-07-17', 1);



INSERT INTO ACTIVITE (nomactivite, privatitation)
VALUES
    ('Concert', 'Publique'),
    ('Rencontre avec les artistes', 'Privée'),
    ('Atelier de musique', 'Publique'),
    ('Conférence', 'Publique'),
    ('Exposition', 'Publique');

INSERT INTO CONCERT (demontage, montage)
VALUES
    (30, 60),
    (120, 120),
    (45 , 60),
    (60 , 120);




INSERT INTO EVENEMENT (dateDebutE, dateFinE, idScene, idJournee, idActivite, idConcert)
VALUES ('2023-07-15 18:00:00', '2023-07-15 20:00:00', 3, 11, NULL, 2),
        ('2023-07-15 19:00:00', '2023-07-15 20:00:00', 5, 11, NULL, 1),
        ('2023-07-15 8:00:00', '2023-07-15 10:00:00', 4, 11, NULL, 4),
        ('2023-07-15 21:00:00', '2023-07-15 23:00:00', 5, 11, 2, NULL);



INSERT INTO SPECTATEUR (nom, numerotel, mail,motsDePasse)
VALUES
    ('Spectateur 1', '1234567890', 'spectateur1@example.com',"151654161246"),
    ('Spectateur 2', '9876543210', 'spectateur2@example.com',"60164849410148"),
    ('Spectateur 3', '1464565465', 'spectateur3@example.com',"161684321315"),
    ('Spectateur 4', '9461616160', 'spectateur4@example.com',"1019465031354"),
    ('Spectateur 5', '6494198848', 'spectateur5@example.com',"25406034841649");

INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
(1,'Les Rolling Stones', 'Un groupe de rock britannique formé à Londres en 1962.', 'twitter.com/rollingstones', "celtic_frost.png", 4);

INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
(2,'The Beatles', 'Un groupe de rock britannique formé à Liverpool en 1960.', 'twitter.com/thebeatles', "daft-punk-random-access-memories-Cover-Art.png", 4);

INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
(3,'AC/DC', 'Un groupe de hard rock australien formé à Sydney en 1973.', 'twitter.com/acdc', "david_guetta.png", 4);

INSERT INTO GROUPE (idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne) VALUES
(4,'Metallica', 'Un groupe de thrash metal américain formé à Los Angeles en 1981.', 'twitter.com/metallica', "sabaton.png", 4);


INSERT INTO PARTICIPE (idEvenement, idGroupe)
VALUES
    (1, 1),
    (2, 1),
    (34, 4),
    (36, 4);
    



INSERT INTO RESERVER (idspectateur, idJournee)
VALUES
    (1, 1),
    (1, 2),
    (3, 3),
    (4, 4),
    (5, 5);

INSERT INTO BILLETEVENEMENT (idspectateur, idEvenement)
VALUES
    (1, 1),
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

INSERT INTO INSTRUMENT(nominstrupent) VALUES
    ("Guitare"),
    ("Chant"),
    ("Basse"),
    ("Batterie");

INSERT INTO MUSICIEN (nom, adresseMail, numeroTelMusicien) VALUES
    ('Mick Jagger', 'mick@rollingstones.com', 0612345678,NULL),

    ('Keith Richards', 'keith@rollingstones.com', 0678901234,NULL),

    ('Charlie Watts', 'charlie@rollingstones.com', 0654321098,NULL),

    ('Ronnie Wood', 'ronnie@rollingstones.com', 0665432109,NULL),

    ('John Lennon', 'john@beatles.com', 0612345778,Lennon.jpg),

    ('Paul McCartney', 'paul@beatles.com', 0677901234,paul_McCartney.jpg),

    ('George Harrison', 'george@beatles.com', 0654321099,george_harris.jpg),

    ('Ringo Starr', 'ringo@beatles.com', 0765432109,Ringo_Starr.png),

    ('Angus Young', 'angus@acdc.com', 0662345678,NULL),

    ('Malcolm Young', 'malcolm@acdc.com', 0678911234,NULL),

    ('Brian Johnson', 'brian@acdc.com', 0674321098,NULL),

    ('Cliff Williams', 'cliff@acdc.com', 0666432109,NULL),

    ('James Hetfield', 'james@metallica.com', 0612345618,NULL),

    ('Lars Ulrich', 'lars@metallica.com', 0678901334,NULL),

    ('Kirk Hammett', 'kirk@metallica.com', 0654331098,NULL),

    ('Robert Trujillo', 'robert@metallica.com', 0667432109,NULL),

    ('Roger Waters', 'roger@pinkfloyd.com', 0712345678,NULL),

    ('David Gilmour', 'david@pinkfloyd.com', 0678901214,NULL),

    ('Richard Wright', 'richard@pinkfloyd.com', 0654821098,NULL),

    ('Nick Mason', 'nick@pinkfloyd.com', 0765432110,NULL);

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

INSERT INTO HEBERGEMENT(nbplace, lieux) VALUES
    (150, "Manhattan"),
    (100, "Queens"),
    (80, "Bronks"),
    (200, "Brooklyn");

INSERT INTO DORMIR(nbPersonneGroupe, dateArrivee, dateDepart, idgroupe, idhebergement) VALUES
    (4, '2023-07-15', '2023-07-19', 1, 1),
    (4, '2023-07-15', '2023-07-19', 2, 2),
    (4, '2023-07-15', '2023-07-19', 3, 4),
    (4, '2023-07-15', '2023-07-19', 4, 3),
    (4, '2023-07-15', '2023-07-19', 5, 1);
    



INSERT INTO PRESENT (idfestival, idgroupe, datearriver, datedepart) VALUES
    (1,1,'2023-07-15','2023-07-19'),
    (1,2,'2023-07-16','2023-07-19'),
    (1,3,'2023-08-15','2023-08-19'),
    (1,4,'2023-08-17','2023-08-19'),
    (1,5,'2023-07-15','2023-07-19'),
    (1,5,'2023-08-18','2023-08-19');




