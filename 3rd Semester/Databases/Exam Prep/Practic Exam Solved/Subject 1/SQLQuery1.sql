--Droping the tables if they already exists
IF OBJECT_ID('Clients','U') IS NOT NULL
	DROP TABLE Clients
IF OBJECT_ID('Salesman','U') IS NOT NULL
	DROP TABLE Salesman
IF OBJECT_ID('Products','U') IS NOT NULL
	DROP TABLE Products
IF OBJECT_ID('Bills','U') IS NOT NULL
	DROP TABLE Bills
IF OBJECT_ID('BillsProducts','U') IS NOT NULL
	DROP TABLE BillsProducts
GO

CREATE TABLE Clients
	(idclient SMALLINT PRIMARY KEY IDENTITY(1,1),
	clientName VARCHAR(500),
	code VARCHAR(50))
CREATE TABLE Salesman
	(idsaleman SMALLINT PRIMARY KEY IDENTITY(1,1),
	firstName VARCHAR(50),
	lastName VARCHAR(50))
CREATE TABLE Products
	(idproduct SMALLINT PRIMARY KEY IDENTITY(1,1),
	productName VARCHAR(50),
	unit VARCHAR(50))
CREATE TABLE Bills
	(idbill SMALLINT PRIMARY KEY IDENTITY(1,1),
	emissionDate DATE,
	idclient SMALLINT REFERENCES Clients(idclient) UNIQUE,
	idsaleman SMALLINT REFERENCES Salesman(idsaleman))
CREATE TABLE BillsProducts
	(idbill SMALLINT REFERENCES Bills(idbill),
	idproduct SMALLINT REFERENCES Products(idproduct),
	price int,
	quantity int,
	PRIMARY KEY (idbill,idproduct)
	)
GO

-- Inserting into the database
INSERT Clients VALUES ('Oscar Gal', '1980705'), ('Comsa Mihai', '1970720'), ('Limbean Anamaria', '1972005')
INSERT Salesman VALUES ('Specter','Harvy'), ('Bill', 'Gates'), ('Steve', 'Jobs')
INSERT Products VALUES('Shaorma', 'grame'), ('Coca Cola', 'litrii'), ('Tigari', 'bucata')
INSERT Bills VALUES('2018-02-02',1,1), ('2018-02-03',2,1), ('2018-02-03',3,2)
INSERT BillsProducts(idbill,idproduct,price,quantity) VALUES
	(1,1,13,20),(1,2,5,14),(1,3,18,15),
	(2,1,13,60),(2,3,18,2),
	(3,2,5,100)
GO

SELECT * FROM Clients
SELECT * FROM Salesman
SELECT * FROM Products
SELECT * FROM Bills
SELECT * FROM BillsProducts
GO