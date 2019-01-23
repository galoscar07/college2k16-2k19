--a)
IF OBJECT_ID('RoutesStations','U') is not NULL
	DROP TABLE RoutesStations
IF OBJECT_ID('Stations','U') is not NULL
	DROP TABLE Stations
IF OBJECT_ID('Routes','U') is not NULL
	DROP TABLE [Routes]
IF OBJECT_ID('Trains','U') is not NULL
	DROP TABLE Trains
IF OBJECT_ID('TrainTypes','U') is not NULL
	DROP TABLE TrainTypes
GO

CREATE TABLE TrainTypes
	(TTID TINYINT PRIMARY KEY IDENTITY(1,1),
	TTDescription VARCHAR(500))
CREATE TABLE Trains
	(TID SMALLINT PRIMARY KEY IDENTITY(1,1),
	TName VARCHAR(50),
	TTID TINYINT REFERENCES TrainTypes(TTID))
CREATE TABLE[Routes]
	(RID SMALLINT PRIMARY KEY IDENTITY(1,1),
	RName VARCHAR(50) UNIQUE,
	TID SMALLINT REFERENCES Trains(TID))
CREATE TABLE Stations
	([SID] SMALLINT PRIMARY KEY IDENTITY(1,1),
	SName VARCHAR(50) UNIQUE)
CREATE TABLE RoutesStations
	(RID SMALLINT REFERENCES [Routes](RID),
	[SID] SMALLINT REFERENCES Stations([SID]),
	Arrival TIME,
	Departure TIME,
	PRIMARY KEY (RID,[SID])
	)
GO

INSERT TrainTypes VALUES('regio'), ('interregio')
INSERT Trains VALUES('t1',1), ('t2',1), ('t3',1)
INSERT [Routes] VALUES('r1',1), ('r2',2), ('r3',3)
INSERT Stations VALUES('s1'), ('s2'), ('s3')
INSERT RoutesStations(RID,[SID],Arrival,Departure) VALUES
	(1,1,'6:00am','6:10am'),(1,2,'7:00am','7:10am'),(1,3,'8:00am','8:10am'),
	(2,1,'5:50am','6:00am'),						(2,3,'17:00','17:10'),
	(3,1,'10:00am','10:10am'), (3,2,'7:05am','7:15am')
GO

SELECT * FROM TrainTypes
SELECT * FROM Trains
SELECT * FROM Stations
SELECT * FROM [Routes]
SELECT * FRom RoutesStations
GO

-- b)
-- The procedure that receive a station, a route, Arrival time, departure time and insert it into the database
ALTER PROC uspStaionOnRoute @RName VARCHAR(100), @SName VARCHAR(100), @Arrival TIME, @Departure TIME
AS
	DECLARE @RID SMALLINT = (SELECT RID FROM [Routes] WHERE RName = @RName),
	@SID SMALLINT = (SELECT [SID] FROM Stations WHERE SName = @SName)
	--optional ... @RID IS NOT NULL
	IF EXISTS (SELECT * FROM RoutesStations WHERE RID = @RID AND [SID] = @SID)
		UPDATE RoutesStations
		SET Arrival = @Arrival, Departure = @Departure
		WHERE RID = @RID AND [SID] = @SID
	ELSE
		INSERT RoutesStations(RID,[SID],Arrival,Departure)
		VALUES(@RID,@SID,@Arrival,@Departure)
GO

--SELECT * FROM RoutesStations
--EXEC uspStaionOnRoute @RName = 'r2', @SName = 's2', @Arrival = '15:00', @Departure = '15:10' 
--this one will add

--EXEC uspStaionOnRoute @RName = 'r2', @SName = 's2', @Arrival = '15:10', @Departure = '15:20'
--SELECT * FROM RoutesStations
--this one will update

--c) create the view 
ALTER VIEW vRoutesWithAllStations
AS

SELECT RName
FROM [Routes] R
WHERE NOT EXISTS
	(SELECT S.[SID]
	FROM Stations S
	EXCEPT
	SELECT RS.[SID]
	FROM RoutesStations RS
	WHERE RS.RID = R.RID) -- if instead of r.rid you put like 1,2,3 to study why the view has only r1, r2
GO

SELECT * FROM vRoutesWithAllStations
GO

--d) some function
ALTER FUNCTION ufStationWithAlLeast2Routes()
RETURNS TABLE
AS
RETURN SELECT S.SName
	FROM Stations S
	WHERE S.[SID] IN
		(SELECT RS1.[SID]
			FROM RoutesStations RS1 INNER JOIN RoutesStations RS2
			ON RS1.[SID] = RS2.[SID] AND RS1.RID < RS2.RID
			AND RS1.Arrival <= RS2.Departure AND RS1.Departure >= RS2.Arrival
		)
GO
SELECT * FROM ufStationWithAlLeast2Routes()

