IF OBBJECT_ID('Likes','U') IS NOT NULL
	DROP TABLE Likes
IF OBBJECT_ID('Coments','U') IS NOT NULL
	DROP TABLE Likes
IF OBBJECT_ID('Posts','U') IS NOT NULL
	DROP TABLE Likes
IF OBBJECT_ID('Users','U') IS NOT NULL
	DROP TABLE Likes
IF OBBJECT_ID('Pages','U') IS NOT NULL
	DROP TABLE Likes
IF OBBJECT_ID('Categories','U') IS NOT NULL
	DROP TABLE Likes
GO

CREATE TABLE Categories(
	CaId smallint primary key identity(1,1),
	CaName VARCHAR(50),
	CaDescription VARCHAR(500)
)

CREATE TABLE
