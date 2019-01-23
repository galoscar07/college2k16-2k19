ALTER PROCEDURE add_actors(@Number INT)
AS
BEGIN
DECLARE @Cnt INT
SET @Cnt=1
WHILE @Cnt <= @Number
BEGIN
	INSERT INTO Actors(name) VALUES ('Actor ' + CAST(@Cnt AS nvarchar))
	SET @cnt = @cnt + 1
END;
END
GO

ALTER PROCEDURE add_movies(@Number INT)
AS
BEGIN
DECLARE @Cnt INT
SET @Cnt=1
WHILE @Cnt <= @Number
BEGIN
	INSERT INTO movies(title,year,short_description) VALUES ('Movie ' + CAST(@Cnt AS nvarchar),2007,'Short Description')
	SET @Cnt = @Cnt + 1
END;
END
GO

ALTER PROCEDURE add_actors_movies(@Number INT)
AS
BEGIN
DECLARE @Cnt INT
SET @Cnt=1
WHILE @Cnt <= @Number
BEGIN
	INSERT INTO ActorsMovies(actor_id,movie_id) VALUES (@Cnt,@Cnt)
	SET @Cnt = @Cnt + 1
END;
END
GO

ALTER PROCEDURE empty_all(@TestID INT)
AS
BEGIN

DECLARE TableCursor CURSOR
FOR
	SELECT T.Name 
	FROM dbo.Tables T 
	INNER JOIN TestTables TestT ON TestT.TableID=T.TableID
	WHERE TestT.TestID=@TestID
	ORDER BY TestT.Position DESC

OPEN TableCursor

DECLARE @TableName VARCHAR(100)
FETCH NEXT FROM TableCursor
	INTO @TableName

WHILE @@FETCH_STATUS=0
BEGIN
	EXEC ('DELETE FROM '+@TableName)
	IF EXISTS (SELECT * from syscolumns where id = Object_ID(@TableName) and colstat & 1 = 1)
	BEGIN
		EXEC ('DBCC CHECKIDENT('+@TableName+', RESEED, 0)')
	END
	FETCH NEXT FROM TableCursor
	INTO @TableName
END

CLOSE TableCursor
DEALLOCATE TableCursor
END
GO


ALTER PROCEDURE execute_test(@TestID INT)
AS
BEGIN

EXEC empty_all @TestID

INSERT INTO TestRuns (Description,StartAt,EndAt)
VALUES (NULL,GETDATE(),GETDATE())

DECLARE @TestRunID INT
SET @TestRunID=SCOPE_IDENTITY()


DECLARE TableCursor CURSOR
FOR
	SELECT TestT.TableID 
	FROM TestTables TestT 
	WHERE TestT.TestID=@TestID
	ORDER BY TestT.Position

OPEN TableCursor

DECLARE @TableID INT	
DECLARE @ViewID INT	
DECLARE @NumberOfRows INT
DECLARE @TableName VARCHAR(100)
DECLARE @ViewName VARCHAR(100)

FETCH NEXT FROM TableCursor
	INTO @TableID


WHILE @@FETCH_STATUS=0
BEGIN
	
	SET @NumberOfRows=(SELECT TestT.NoOfRows FROM TestTables TestT WHERE TestT.TestID=@TestID AND TestT.TableID=@TableID)

	INSERT INTO TestRunTables (TestRunID,TableID,StartAt,EndAt)
	VALUES (@TestRunID,@TableID,GETDATE(),GETDATE())

	SET @TableName=(SELECT T.Name FROM Tables T WHERE T.TableID=@TableID)

	EXEC ('add_'+@TableName+' '+@NumberOfRows)

	UPDATE TestRunTables
	SET EndAt=GETDATE()
	WHERE TestRunID=@TestRunID AND TableID=@TableID

	FETCH NEXT FROM TableCursor
	INTO @TableID
END

DECLARE ViewCursor CURSOR
FOR
	SELECT TestV.ViewID 
	FROM TestViews TestV 
	WHERE TestV.TestID=@TestID

OPEN ViewCursor

FETCH NEXT FROM ViewCursor
	INTO @ViewID

WHILE @@FETCH_STATUS=0
BEGIN
	INSERT INTO TestRunViews (TestRunID,ViewID,StartAt,EndAt)
	VALUES (@TestRunID,@ViewID,GETDATE(),GETDATE())
	
	SET @ViewName=(SELECT V.Name FROM Views V WHERE V.ViewID=@ViewID)

	EXEC('SELECT * FROM '+@ViewName)

	UPDATE TestRunViews
	SET EndAt=GETDATE()
	WHERE TestRunID=@TestRunID AND ViewID=@ViewID

	UPDATE TestRuns
	SET EndAt=GETDATE()
	WHERE TestRunID=@TestRunID
		
	FETCH NEXT FROM ViewCursor
	INTO @ViewID
END
CLOSE TableCursor
DEALLOCATE TableCursor
CLOSE ViewCursor
DEALLOCATE ViewCursor
END
GO


EXEC execute_test 3