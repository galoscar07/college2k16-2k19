DROP PROCEDURE version_1
DROP PROCEDURE revert_1
DROP PROCEDURE version_2
DROP PROCEDURE revert_2
DROP PROCEDURE version_3
DROP PROCEDURE revert_3
DROP PROCEDURE version_4
DROP PROCEDURE revert_4
DROP PROCEDURE version_5
DROP PROCEDURE revert_5
DROP PROCEDURE go_to_version
GO

CREATE PROCEDURE version_1
AS
BEGIN
	ALTER TABLE Actors
		ALTER COLUMN [name] varchar(80)

	UPDATE Version
		SET number = 1
END
GO

CREATE PROCEDURE revert_1
AS
BEGIN
	ALTER TABLE Actors
		ALTER COLUMN [name] nvarchar(MAX)


	UPDATE Version
		SET number = 0
END
GO


CREATE PROCEDURE version_2
AS
BEGIN
	ALTER TABLE Actors
		ADD CONSTRAINT default_name
		DEFAULT '900'
		FOR [name]

	UPDATE Version
		SET number = 2
END
GO


CREATE PROCEDURE revert_2
AS
BEGIN
	ALTER TABLE Actors
		DROP CONSTRAINT default_name

	UPDATE Version
		SET number = 1
END
GO


CREATE PROCEDURE version_3
AS
BEGIN
	CREATE TABLE Something(
		id INT PRIMARY KEY,
		value int DEFAULT 0)

	UPDATE Version
		SET number = 3
END
GO


CREATE PROCEDURE revert_3
AS
BEGIN
	DROP TABLE Something

	UPDATE version
		SET number = 3
END
GO


CREATE PROCEDURE version_4
AS
BEGIN
	ALTER TABLE Actors
		ADD sid int

	UPDATE Version
		SET number = 4
END
GO


CREATE PROCEDURE revert_4
AS
BEGIN
	ALTER TABLE Actors
		DROP COLUMN sid

	UPDATE Version
		SET number = 3
END
GO

CREATE PROCEDURE version_5
AS
BEGIN
	ALTER TABLE Actors
		ADD CONSTRAINT sid
		FOREIGN KEY (sid) REFERENCES Movies(movie_id)

	UPDATE Version
		SET number = 5
END
GO


CREATE PROCEDURE revert_5
AS
BEGIN
	ALTER TABLE Actors
		DROP CONSTRAINT sid

	UPDATE Version
		SET number = 4
END
GO


CREATE PROCEDURE go_to_version
	@Target int
AS
BEGIN
	DECLARE @Current INT
	SET @Current = (SELECT TOP 1 number FROM VERSION)
	PRINT 'Current version: '+CAST(@Current AS VARCHAR(10))
	PRINT 'Target version: '+CAST(@Target AS VARCHAR(10))
	
	IF @Target < 0 OR @Target > 5
		BEGIN
		RAISERROR('Invalid target version.',16,1)
		RETURN
		END

	DECLARE @f VARCHAR(10)

	WHILE @Current<@Target
	BEGIN
		SET @f = 'version_'+CAST(@Current+1 AS VARCHAR(10))
		EXECUTE @f
		SET @Current = @Current+1
	END

	WHILE @Current>@Target
	BEGIN
		SET @f = 'revert_'+CAST(@Current AS VARCHAR(10))
		EXECUTE @f
		SET @Current = @Current-1
	END
END
GO

EXECUTE go_to_version 0

SELECT * FROM VERSION