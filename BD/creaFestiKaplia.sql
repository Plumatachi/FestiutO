CREATE TABLE `JOURNEE`(
  `idJournee` int auto_increment,
  `nomJournee` VARCHAR(42),
  `dateDebutJ` date,
  `dateFinJ` date,
  `idfestival` int,
  PRIMARY KEY(`idJournee`)
);

CREATE TABLE `EVENEMENT`(
  `idEvenement` int auto_increment,
  `dateDebutE` DATETIME,
  `dateFinE` DATETIME,
  `idScene` int,
  `idJournee` int,
  `idActivite` int,
  `idConcert` int,
  PRIMARY KEY(`idEvenement`)
);

CREATE TABLE `SCENE` (
  `idScene` int auto_increment,
  `nomScene` VARCHAR(42),
  `lieux` VARCHAR(42),
  PRIMARY KEY(idScene)
);

CREATE TABLE `ACTIVITE` (
  `idActivite` int auto_increment,
  `nomactivite` VARCHAR(42),
  `privatitation` VARCHAR(42),
  PRIMARY KEY ( `idActivite`)
)  ;

CREATE TABLE `CONCERT` (
  `idConcert` int auto_increment,
  `demontage` int,
  `montage` int,
  PRIMARY KEY ( `idConcert`)
)  ;

CREATE TABLE `RESERVER` (
  `idspectateur` int,
  `idJournee` int,
  PRIMARY KEY (`idspectateur`, `idJournee`)
)  ;

CREATE TABLE `BILLETEVENEMENT` (
  `idspectateur` int,
  `idEvenement` int,
  PRIMARY KEY (`idspectateur`, `idEvenement`)
)  ;

CREATE TABLE `FESTIVAL` (
  `idfestival` int auto_increment,
  `datedebut` date,
  `datefin` date,
  PRIMARY KEY (`idfestival`)
)  ;


CREATE TABLE `GROUPE` (
  `idgroupe` int auto_increment,
  `nomDuGroupe` VARCHAR(42),
  `description` VARCHAR(100),
  `reseausocial` VARCHAR(100),
  `photo` VARCHAR(200),  
  `nbpersonne` int,
  PRIMARY KEY (`idgroupe`)
)  ;

CREATE TABLE `HEBERGEMENT` (
  `idhebergement` int auto_increment,
  `nbplace` int,
  `lieux` VARCHAR(100),
  PRIMARY KEY (`idhebergement`)
)  ;

CREATE TABLE `INSTRUMENT` (
  `idinstrument` int auto_increment,
  `nominstrupent` VARCHAR(42),  
  PRIMARY KEY (`idinstrument`)
)  ;

CREATE TABLE `JOUE` (
  `idgroupe` int,
  `idinstrument` int,
  `idMusicien` int,
  PRIMARY KEY (`idgroupe`, `idinstrument`,`idMusicien`)
)  ;

CREATE TABLE `PRESENT` (
  `idfestival` int,
  `idgroupe` int,
  `datearriver` date,
  `datedepart` date,
  PRIMARY KEY (`idfestival`, `idgroupe`)
)  ;

CREATE TABLE `STYLEDEMUSIQUE` (
  `typeDeMusique` VARCHAR(42),
  PRIMARY KEY(`typeDeMusique`)
) ;

CREATE TABLE `SPECTATEUR` (
  `idspectateur` int auto_increment,
  `nom` VARCHAR(42),
  `numerotel` VARCHAR(10),
  `mail` VARCHAR(100) UNIQUE,
  `motsDePasse` varchar(20),
  PRIMARY KEY (`idspectateur`)
)  ;

CREATE TABLE `STYLE` (
  `idgroupe` int,
  `typeDeMusique` VARCHAR(42),
  PRIMARY KEY (`idgroupe` ,`typeDeMusique`)
)  ;

CREATE TABLE `DORMIR` (
  `nbPersonneGroupe` int,
  `dateArrivee` date,
  `dateDepart` date,
  `idgroupe` int,
  `idhebergement` int,
  PRIMARY KEY (`idgroupe`,`idhebergement`) 
) ;

CREATE TABLE `MUSICIEN` (
  `idMusicien` int auto_increment,
  `nom` VARCHAR(42),
  `adresseMail` VARCHAR(42),
  `numeroTelMusicien` int,
  PRIMARY KEY (`idMusicien`)
) ;

-- A demander au prof
CREATE TABLE `RESSEMBLE` (
  `typeDeMusique` VARCHAR(42),
  `typeDeMusique2` VARCHAR(42),
  PRIMARY KEY(`typeDeMusique`)
);

CREATE TABLE `PARTICIPE` (
  `idEvenement` int,
  `idGroupe` int,
  PRIMARY KEY(`idEvenement`, `idGroupe`)
);

CREATE TABLE `APPARTIENT` (
    `idGroupe` int,
    `idMusicien` int,
    PRIMARY KEY (`idGroupe`, `idMusicien`)
);

CREATE TABLE `FAVORIS` (
    `idFav` int auto_increment,
    `idspectateur` int REFERENCES `SPECTATEUR` (`idspectateur`),
    `idgroupe` int REFERENCES `GROUPE` (`idgroupe`),
    PRIMARY KEY (`idFav`)
);

ALTER TABLE `JOURNEE` ADD FOREIGN KEY(`idfestival`) REFERENCES `FESTIVAL` (`idfestival`);
ALTER TABLE `BILLETEVENEMENT` ADD FOREIGN KEY(`idEvenement`) REFERENCES `EVENEMENT` (`idEvenement`);
ALTER TABLE `BILLETEVENEMENT` ADD FOREIGN KEY(`idspectateur`) REFERENCES `SPECTATEUR` (`idspectateur`);
ALTER TABLE `RESERVER` ADD FOREIGN KEY (`idJournee`) REFERENCES `JOURNEE` (`idJournee`);
ALTER TABLE `RESERVER` ADD FOREIGN KEY (`idspectateur`) REFERENCES `SPECTATEUR` (`idspectateur`);
ALTER TABLE `JOUE` ADD FOREIGN KEY (`idinstrument`) REFERENCES `INSTRUMENT` (`idinstrument`);
ALTER TABLE `JOUE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `JOUE` ADD FOREIGN KEY (`idMusicien`) REFERENCES `MUSICIEN` (`idMusicien`);
ALTER TABLE `PRESENT` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `PRESENT` ADD FOREIGN KEY (`idfestival`) REFERENCES `FESTIVAL` (`idfestival`);
ALTER TABLE `STYLE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `STYLE` ADD FOREIGN KEY (`typeDeMusique`) REFERENCES `STYLEDEMUSIQUE` (`typeDeMusique`);
ALTER TABLE `DORMIR` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `DORMIR` ADD FOREIGN KEY (`idhebergement`) REFERENCES `HEBERGEMENT` (`idhebergement`);
ALTER TABLE `RESSEMBLE` ADD FOREIGN KEY (`typeDeMusique`) REFERENCES `STYLEDEMUSIQUE` (`typeDeMusique`);
ALTER TABLE `PARTICIPE` ADD FOREIGN KEY (`idEvenement`) REFERENCES `EVENEMENT` (`idEvenement`);
ALTER TABLE `PARTICIPE` ADD FOREIGN KEY (`idGroupe`) REFERENCES `GROUPE` (`idGroupe`);
ALTER TABLE `EVENEMENT` ADD FOREIGN KEY(`idScene`) REFERENCES `SCENE` (`idScene`);
ALTER TABLE `EVENEMENT` ADD FOREIGN KEY(`idJournee`) REFERENCES `JOURNEE` (`idJournee`);
ALTER TABLE `EVENEMENT` ADD FOREIGN KEY(`idConcert`) REFERENCES `CONCERT` (`idConcert`);
ALTER TABLE `EVENEMENT` ADD FOREIGN KEY(`idActivite`) REFERENCES `ACTIVITE` (`idActivite`);
ALTER TABLE `APPARTIENT` ADD FOREIGN KEY(`idGroupe`) REFERENCES `GROUPE` (`idGroupe`);
ALTER TABLE `APPARTIENT` ADD FOREIGN KEY(`idMusicien`) REFERENCES `MUSICIEN` (`idMusicien`);




-- Trigger permettant à un evenement d'avoir seulement un type : soit un concert, soit une activité. 
delimiter |
create or replace trigger seulement_1_type_evenement before insert on EVENEMENT for each row 
begin
    IF ( NEW.idConcert is not NULL  and NEW.idActivite is not NULL ) THEN

        signal SQLSTATE '45000' set MESSAGE_TEXT = "Il n'est pas possible pour un événement d'avoir deux types";

    end IF;
end |



-- Trigger permettant d'éviter qu'une scène est 2 événements renseigné sur elle même en même temps.
delimiter |
create or replace trigger evenement_pas_sur_2_scene_en_meme_temps before insert on EVENEMENT for each row
begin
declare cpt int;
    SELECT COUNT(*)
    INTO cpt
    FROM EVENEMENT
    WHERE idScene = NEW.idScene
    AND DATE_FORMAT(dateDebutE,"%Y-%m-%d %H:%i:%S" ) <= DATE_FORMAT(NEW.dateFinE,"%Y-%m-%d %H:%i:%S")
    AND DATE_FORMAT(dateFinE,"%Y-%m-%d %H:%i:%S") >= DATE_FORMAT(NEW.dateDebutE,"%Y-%m-%d %H:%i:%S");
    
    IF cpt > 0 THEN
        signal SQLSTATE '45000' set MESSAGE_TEXT = "Un événement existe déjà sur la même scène au même moment";
    END IF;
end |



-- Trigger permettant qu'un événement est bien ses dates comprisent dans la journée ou il se déroule.
delimiter |
create or replace trigger evenement_present_dans_la_bonne_journee before insert on EVENEMENT for each row
begin
    declare v_day_start DATE;
    declare v_day_end DATE;
    -- Obtenir la date de début et de fin de la journée associée à l'événement
    SELECT DATE_FORMAT(dateDebutJ, "%Y-%m-%d"),  DATE_FORMAT(dateFinJ, "%Y-%m-%d")
    INTO v_day_start, v_day_end
    FROM JOURNEE
    WHERE idJournee = NEW.idJournee;
    
    IF DATE_FORMAT(NEW.dateDebutE, "%Y-%m-%d") < v_day_start OR DATE_FORMAT(NEW.dateFinE, "%Y-%m-%d") > v_day_end THEN
        signal SQLSTATE '45000' set MESSAGE_TEXT = "L'événement doit se dérouler entièrement dans la journée associée.";
    END IF;
end |



-- Trigger permettant de mettre à jour la capacité de l'hebergement quand des personnes reservent des chambres pour celui-ci.
delimiter |
create trigger mise_a_jour_capacite_hebergement after insert on DORMIR for each row
begin
    declare v_total_reserved INT;
    -- Obtenir le nombre total de personnes réservées pour cet hébergement
    SELECT SUM(nbPersonneGroupe) INTO v_total_reserved
    FROM DORMIR
    WHERE idhebergement = NEW.idhebergement;
    
    -- Mettre à jour la capacité de l'hébergement
    UPDATE HEBERGEMENT
    SET nbplace = nbplace - v_total_reserved
    WHERE idhebergement = NEW.idhebergement;
end |



-- Trigger permettant de vérifier que le nombre de personne voulant reserver un hotel ne depasse la capacité d'accueil de cet hotel.
delimiter |
create or replace trigger check_capacite_hebergement before insert on DORMIR for each row
begin
    declare v_capacity int;
    -- Obtenir la capacité de l'hébergement choisi
    SELECT nbplace INTO v_capacity
    FROM HEBERGEMENT
    WHERE idhebergement = NEW.idhebergement;

    IF NEW.nbPersonneGroupe > v_capacity THEN
        signal SQLSTATE '45000' set MESSAGE_TEXT = "La capacité d'hébergement n'est pas suffisante pour ce groupe.";
    END IF;
end |



-- Trigger permettant de vérifier que la date d'une journée se trouve bien entre les dates du festival qui lui est associé.
delimiter |
create trigger date_journee_comprise_dans_le_festival before insert on JOURNEE for each row
begin
    declare v_festival_start DATE;
    declare v_festival_end DATE;

    -- Obtenir la date de début et de fin du festival associé
    SELECT datedebut, datefin
    INTO v_festival_start, v_festival_end
    FROM FESTIVAL
    WHERE idfestival = NEW.idfestival;

    IF NEW.dateDebutJ < v_festival_start OR NEW.dateFinJ > v_festival_end THEN
        signal SQLSTATE '45000' SET MESSAGE_TEXT = 'Les dates de la journée doivent être comprises entre les dates du festival associé.';
    END IF;
end |



-- Trigger permettant d'interdir à un spectateur d'acheter 2 fois le même billet pour le même événement.
delimiter |
create trigger seulement_1_billet_pour_1_evenement before insert on BILLETEVENEMENT for each row
begin
    DECLARE v_ticket_count int;

    -- Vérifier si le spectateur a déjà acheté un billet pour le même événement
    SELECT COUNT(*) INTO v_ticket_count
    FROM BILLETEVENEMENT
    WHERE idspectateur = NEW.idspectateur AND idEvenement = NEW.idEvenement;

    IF v_ticket_count > 0 THEN
        signal SQLSTATE '45000' SET MESSAGE_TEXT = 'Un spectateur ne peut pas acheter deux fois le même billet pour le même événement.';
    END IF;
end |


-- Trigger permettant d'interdir à un spectateur d'acheter 2 réservations d'une journée en même temps.
delimiter |
create trigger seulement_1_reservation_pour_1_journee before insert on RESERVER for each row
begin
    DECLARE v_ticket_count int;

    -- Vérifier si le spectateur a déjà acheté un billet pour le même événement
    SELECT COUNT(*) INTO v_ticket_count
    FROM RESERVER
    WHERE idspectateur = NEW.idspectateur AND idJournee = NEW.idJournee;

    IF v_ticket_count > 0 THEN
        signal SQLSTATE '45000' SET MESSAGE_TEXT = 'Un spectateur ne peut pas réserver deux fois la même journée.';
    END IF;
end |


