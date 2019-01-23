-- Creating the tables a)
IF OBJECT_ID('Librarii','U') is not NULL
	DROP TABLE Librarii
IF OBJECT_ID('Domenii','U') is not NULL
	DROP TABLE Domenii
IF OBJECT_ID('Carti','U') is not NULL
	DROP TABLE Carti
IF OBJECT_ID('CartiAutori','U') is not NULL
	DROP TABLE CartiAutori
IF OBJECT_ID('Autori','U') is not NULL
	DROP TABLE Autori
GO

CREATE TABLE Librarii
	(LID SMALLINT PRIMARY KEY IDENTITY(1,1),
	nume VARCHAR(500),
	adresa VARCHAR(500))
CREATE TABLE Domenii
	(DID SMALLINT PRIMARY KEY IDENTITY(1,1),
	descriere VARCHAR(500))
CREATE TABLE Autori
	(AID SMALLINT PRIMARY KEY IDENTITY(1,1),
	nume VARCHAR(500))
CREATE TABLE Carti
	(CID SMALLINT PRIMARY KEY IDENTITY(1,1),
	titlu VARCHAR(500),
	ora TIME,
	DID SMALLINT REFERENCES Domenii(DID),
	LID SMALLINT REFERENCES Librarii(LID))
CREATE TABLE CartiAutori
	(CID SMALLINT REFERENCES Carti(CID),
	AID SMALLINT REFERENCES Autori(AID),
	PRIMARY KEY (CID,AID))
GO

INSERT Domenii VALUES ('Stiintifice'), ('Literatura')
INSERT dbo.Autori VALUES ('Mihai Eminescu'), ('Stephan'), ('Octavian Goga')
INSERT Librarii VALUES ('Corint','Str. George Enescu, nr. 12'), ('Humanitas','Str. Horea Closca si Crisan, nr. 14')
INSERT Carti VALUES ('Poezi','5:50pm',2,1), ('Cum s-a format universul','6:30pm',1,2)
INSERT CartiAutori VALUES (1,2), (1,3), (2,2)
GO

SELECT * FROM Librarii
SELECT * FROM Domenii
SELECT * FROM Autori
SELECT * FROM CartiAutori
SELECT * FROM Carti
GO

-- b) a procedure that receive an author name, 