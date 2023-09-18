drop table IF EXISTS `STYLE` ;
drop table IF EXISTS `ACTIVITE`;
drop table IF EXISTS `BILLET`;
drop table IF EXISTS `CONCERT`;
drop table IF EXISTS `JOUE`;
drop table IF EXISTS `INSTRUMENT`;
drop table IF EXISTS `SPECTATEUR`;
drop table IF EXISTS `PRESENT`;
drop table IF EXISTS `FESTIVAL`;
drop table IF EXISTS `GROUPE`;
drop table IF EXISTS `HEBERGEMENT`;



CREATE TABLE `ACTIVITE` (
  `idActivite` int,
  `idgroupe` int,
  `dateA` date,
  `heureA` int,
  `duree` int,
  `nomactivite` VARCHAR(42),
  `privatitation` VARCHAR(42),
  PRIMARY KEY ( `idActivite`),check("heureA"+`duree`  <= 24 and "heureA"<= 24)
)  ;

CREATE TABLE `BILLET` (
  `idspectateur` int,
  `idfestival` int,
  `type` int,
  PRIMARY KEY (`idspectateur`, `idfestival`)
)  ;

CREATE TABLE `CONCERT` (
  `idConcert` int,
  `dateC` date,
  `heureC` int, check("heureC"+duree between 1 and 24 and "heureC" between 1 and 24)
  `idgroupe` int,
  `tarif` int,
  `demontage` int,
  `montage` int,
  `duree` int,
  PRIMARY KEY ( `idConcert`)
)  ;

CREATE TABLE `FESTIVAL` (
  `idfestival` int,
  `datedebut` date,
  `datefin` date,
  PRIMARY KEY (`idfestival`)
)  ;
--regarder pour les photos plus tard 
CREATE TABLE `GROUPE` (
  `idgroupe` int,
  `nomDuGroupe` VARCHAR(42),
  `description` VARCHAR(100),
  `reseausocial` VARCHAR(100),
  `photo` VARCHAR(42),  
  `nbpersone` int,
  `idhebergement` int,
  PRIMARY KEY (`idgroupe`)
)  ;

CREATE TABLE `HEBERGEMENT` (
  `idhebergement` int,
  `nbplace` int,
  `lieux` VARCHAR(100),
  PRIMARY KEY (`idhebergement`)
)  ;

CREATE TABLE `INSTRUMENT` (
  `idinstrument` int,
  `nominstrupent` VARCHAR(42),
  PRIMARY KEY (`idinstrument`)
)  ;

CREATE TABLE `JOUE` (
  `idgroupe` int,
  `idinstrument` int,
  PRIMARY KEY (`idgroupe`, `idinstrument`)
)  ;

CREATE TABLE `PRESENT` (
  `idfestival` int,
  `idgroupe` int,
  `datearriver` date,
  `datedepart` date,
  PRIMARY KEY (`idfestival`, `idgroupe`)
)  ;

CREATE TABLE `SPECTATEUR` (
  `idspectateur` int,
  `nom` VARCHAR(42),
  `numerotel` VARCHAR(10),
  `mail` VARCHAR(100),
  PRIMARY KEY (`idspectateur`)
)  ;

CREATE TABLE `STYLE` (
  `idgroupe` int,
  `typestyle` VARCHAR(42),
  PRIMARY KEY (`idgroupe`, `typestyle`)
)  ;

ALTER TABLE `ACTIVITE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `BILLET` ADD FOREIGN KEY (`idfestival`) REFERENCES `FESTIVAL` (`idfestival`);
ALTER TABLE `BILLET` ADD FOREIGN KEY (`idspectateur`) REFERENCES `SPECTATEUR` (`idspectateur`);
ALTER TABLE `CONCERT` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `GROUPE` ADD FOREIGN KEY (`idhebergement`) REFERENCES `HEBERGEMENT` (`idhebergement`);
ALTER TABLE `JOUE` ADD FOREIGN KEY (`idinstrument`) REFERENCES `INSTRUMENT` (`idinstrument`);
ALTER TABLE `JOUE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `PRESENT` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);
ALTER TABLE `PRESENT` ADD FOREIGN KEY (`idfestival`) REFERENCES `FESTIVAL` (`idfestival`);
ALTER TABLE `STYLE` ADD FOREIGN KEY (`idgroupe`) REFERENCES `GROUPE` (`idgroupe`);