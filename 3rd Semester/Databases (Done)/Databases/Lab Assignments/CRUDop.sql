
/* reseteaza la tabelul dintre paranteze patrate indexul la numarul dat ca parametru */
/*
DBCC CHECKIDENT ('[Role]', RESEED, 0);
GO
*/

USE [CSGO League Database]
GO

/*Mi-am facut functii care verifica existenta unor id-uri in baza de date*/
/* FUNCTION TO CHECK IF A COUNTRY EXISTS */

IF OBJECT_ID('dbo.checkCountry') IS NOT NULL
BEGIN
DROP FUNCTION checkCountry
END
GO
CREATE FUNCTION [dbo].[checkCountry] (@id int)
RETURNS INT
AS
BEGIN
DECLARE @country_id_counter int
DECLARE @return int
DECLARE @varloc int
/*SET @return = 0
DECLARE CURS 
CURSOR FOR */
SELECT @varloc=COUNT(*) FROM Country WHERE country_id = @id
/*SELECT country_id FROM Country WHERE country_id = @id*/
return @varloc
END
OPEN CURS
FETCH NEXT FROM CURS INTO @country_id_counter
WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @return = 1
		FETCH NEXT FROM CURS INTO @country_id_counter
	END
CLOSE CURS
DEALLOCATE CURS
RETURN @return
END
GO

/* FUNCTION TO CHECK IF A SPONSOR EXISTS */

IF OBJECT_ID('dbo.checkSponsor') IS NOT NULL
BEGIN
DROP FUNCTION checkSponsor
END
GO
CREATE FUNCTION [dbo].[checkSponsor] (@id int)
RETURNS BIT
AS
BEGIN
DECLARE @sponsor_id_counter int
DECLARE @return bit
SET @return = 0
DECLARE CURS2
CURSOR FOR 
SELECT sponsor_id FROM Sponsors WHERE sponsor_id = @id
OPEN CURS2
FETCH NEXT FROM CURS2 INTO @sponsor_id_counter
WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @return = 1
		FETCH NEXT FROM CURS2 INTO @sponsor_id_counter
	END
CLOSE CURS2
DEALLOCATE CURS2
RETURN @return
END
GO


/* FUNCTION TO CHECK IF A CASTER EXISTS */

IF OBJECT_ID('dbo.checkCaster') IS NOT NULL
BEGIN
DROP FUNCTION checkCaster
END
GO
CREATE FUNCTION [dbo].[checkCaster] (@id int)
RETURNS BIT
AS
BEGIN
DECLARE @caster_id_counter int
DECLARE @return bit
SET @return = 0
DECLARE CURS3
CURSOR FOR 
SELECT caster_id FROM Casters WHERE caster_id = @id
OPEN CURS3
FETCH NEXT FROM CURS3 INTO @caster_id_counter
WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @return = 1
		FETCH NEXT FROM CURS3 INTO @caster_id_counter
	END
CLOSE CURS3
DEALLOCATE CURS3
RETURN @return
END
GO


/* FUNCTION TO CHECK IF A DIVISION EXISTS */

IF OBJECT_ID('dbo.checkDivision') IS NOT NULL
BEGIN
DROP FUNCTION checkDivision
END
GO
CREATE FUNCTION [dbo].checkDivision (@id int)
RETURNS BIT
AS
BEGIN
DECLARE @division_id_given int
DECLARE @return bit
SET @return = 0
DECLARE CURS4
CURSOR FOR 
SELECT division_id FROM Division WHERE division_id = @id
OPEN CURS4
FETCH NEXT FROM CURS4 INTO @division_id_given
WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @return = 1
		FETCH NEXT FROM CURS4 INTO @division_id_given
	END
CLOSE CURS4
DEALLOCATE CURS4
RETURN @return
END
GO

/* FUNCTION TO CHECK IF A ROLE EXISTS */

IF OBJECT_ID('dbo.checkRole') IS NOT NULL
BEGIN
DROP FUNCTION checkRole
END
GO
CREATE FUNCTION [dbo].checkRole (@id int)
RETURNS BIT
AS
BEGIN
DECLARE @role_id_given int
DECLARE @return bit
SET @return = 0
DECLARE CURS5
CURSOR FOR 
SELECT role_id FROM Role WHERE role_id = @id
OPEN CURS5
FETCH NEXT FROM CURS5 INTO @role_id_given
WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @return = 1
		FETCH NEXT FROM CURS5 INTO @role_id_given
	END
CLOSE CURS5
DEALLOCATE CURS5
RETURN @return
END
GO

/* FUNCTION TO CHECK IF A TEAM EXISTS */

IF OBJECT_ID('dbo.checkTeam') IS NOT NULL
BEGIN
DROP FUNCTION checkTeam
END
GO
CREATE FUNCTION [dbo].checkTeam (@id int)
RETURNS BIT
AS
BEGIN
DECLARE @team_id_given int
DECLARE @return bit
SET @return = 0
DECLARE CURS6
CURSOR FOR 
SELECT team_id FROM Teams WHERE team_id = @id
OPEN CURS6
FETCH NEXT FROM CURS6 INTO @team_id_given
WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @return = 1
		FETCH NEXT FROM CURS6 INTO @team_id_given
	END
CLOSE CURS6
DEALLOCATE CURS6
RETURN @return
END
GO

/* FUNCTION TO CHECK IF A SPONSOR AND TEAM EXIST IN THE TABLE*/

IF OBJECT_ID('dbo.checkST') IS NOT NULL
BEGIN
DROP FUNCTION checkST
END
GO
CREATE FUNCTION [dbo].checkST (@team int, @sponsor int)
RETURNS BIT
AS
BEGIN
DECLARE @team_id_given int
DECLARE @sponsor_id_given int
DECLARE @return bit
SET @return = 0
DECLARE CURS7
CURSOR FOR 
SELECT team_id, sponsor_id FROM SponsorTeam WHERE team_id = @team AND sponsor_id=@sponsor
OPEN CURS7
FETCH NEXT FROM CURS7 INTO @team_id_given, @sponsor_id_given
WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @return = 1
		FETCH NEXT FROM CURS7 INTO @team_id_given, @sponsor_id_given
	END
CLOSE CURS7
DEALLOCATE CURS7
RETURN @return
END
GO


/* De aici incep cele 20 de proceduri care trebuie facute */

/* CRUD _ ROLE _ CREATE */


IF OBJECT_ID('CRUD_RoleCreate') IS NOT NULL
BEGIN
DROP PROC CRUD_RoleCreate
END
GO
CREATE PROCEDURE CRUD_RoleCreate
			@name_role nvarchar(50)
AS
BEGIN
DECLARE @role_id int
INSERT INTO Role(name_role)
	VALUES (@name_role)
SET @role_id = SCOPE_IDENTITY()
SELECT
		role_id = @role_id,
		name_role = @name_role
FROM Role
WHERE role_id = @role_id
END

/*CRUD _ ROLE _ READ */

GO
IF OBJECT_ID('CRUD_RoleRead') IS NOT NULL
BEGIN
DROP PROC CRUD_RoleRead
END
GO
CREATE PROCEDURE CRUD_RoleRead
	@role_id int
AS
BEGIN
BEGIN TRY
IF(dbo.checkRole(@role_id)=1)
	BEGIN
		SELECT name_role, role_id
		FROM Role
		WHERE (role_id = @role_id)
	END
ELSE
	THROW 50000, 'The Role does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/* CRUD _ ROLE _ UPDATE */

GO
IF OBJECT_ID('CRUD_RoleUpdate') IS NOT NULL
BEGIN
DROP PROC CRUD_RoleUpdate
END
GO
CREATE PROCEDURE CRUD_RoleUpdate
	@name_role nvarchar(50),
	@role_id_given int
AS
BEGIN
BEGIN TRY
IF (dbo.checkRole(@role_id_given)=1)
	BEGIN
		UPDATE Role
		SET name_role = @name_role
		WHERE (role_id = @role_id_given)
	END
ELSE
	THROW 50000, 'The Role does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END


/* CRUD _ ROLE _ DELETE */

GO
IF OBJECT_ID('CRUD_RoleDelete') IS NOT NULL
BEGIN
DROP PROC CRUD_RoleDelete
END
GO
CREATE PROCEDURE CRUD_RoleDelete
	@role_id_given int
AS
BEGIN
BEGIN TRY
IF (dbo.checkRole(@role_id_given)=1)
	BEGIN
		DELETE FROM Role
		WHERE (role_id = @role_id_given)
	END
ELSE
	THROW 50000, 'The Role does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END


/*
DBCC CHECKIDENT ('[Casters]', RESEED, 7);
GO
*/
/* CRUD _ CASTERS _ CREATE */

GO
IF OBJECT_ID('CRUD_CastersCreate') IS NOT NULL
BEGIN
DROP PROC CRUD_CastersCreate
END
GO
CREATE PROCEDURE CRUD_CastersCreate
			@name_caster nvarchar(50),
			@country_id int,
			@salary int
AS
BEGIN
DECLARE @caster_id int
DECLARE @okc int
DECLARE @country_id_counter int
BEGIN TRY
IF (dbo.checkCountry(@country_id)=1)
	BEGIN 
	INSERT INTO Casters(name_caster, country_id, salary)
		VALUES (@name_caster, @country_id, @salary)
	SET @caster_id = SCOPE_IDENTITY()
	SELECT
			caster_id = @caster_id,
			name_caster = @name_caster,
			country_id = @country_id,
			salary = @salary
	FROM Casters
	WHERE caster_id = @caster_id
	END
ELSE
	THROW 50000, 'The country does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/*CRUD _ CASTERS _ READ */

GO
IF OBJECT_ID('CRUD_CastersRead') IS NOT NULL
BEGIN
DROP PROC CRUD_CastersRead
END
GO
CREATE PROCEDURE CRUD_CastersRead
	@caster_id int
AS
BEGIN
BEGIN TRY
IF (dbo.checkCaster(@caster_id)=1)
	BEGIN
	SELECT caster_id, name_caster, country_id, salary
	FROM Casters
	WHERE (caster_id = @caster_id)
	END
ELSE
	THROW 50000, 'The caster does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/* CRUD _ CASTERS _ UPDATE */

GO
IF OBJECT_ID('CRUD_CastersUpdate') IS NOT NULL
BEGIN
DROP PROC CRUD_CastersUpdate
END
GO
CREATE PROCEDURE CRUD_CastersUpdate
	@caster_id_given int,
	@name_caster nvarchar(50),
	@country_id int,
	@salary int
AS
BEGIN
BEGIN TRY
IF (dbo.checkCountry(@country_id)=1 AND dbo.checkCaster(@caster_id_given)=1)
	BEGIN
		UPDATE Casters
		SET name_caster = @name_caster,
			country_id = @country_id,
			salary = @salary
		WHERE (caster_id = @caster_id_given)
	END
ELSE
	THROW 50000, 'The caster or country does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/* CRUD _ CASTERS _ DELETE */

GO
IF OBJECT_ID('CRUD_CastersDelete') IS NOT NULL
BEGIN
DROP PROC CRUD_CastersDelete
END
GO
CREATE PROCEDURE CRUD_CastersDelete
	@caster_id_given int
AS
BEGIN
BEGIN TRY
IF(dbo.checkCaster(@caster_id_given)=1)
	BEGIN
	DELETE FROM Casters
	WHERE (caster_id = @caster_id_given)
	END
ELSE
	THROW 50000, 'The caster does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/*
DBCC CHECKIDENT ('[Division]', RESEED, 5);
GO
*/
/* CRUD _ DIVISION _ CREATE */

GO
IF OBJECT_ID('CRUD_DivisionCreate') IS NOT NULL
BEGIN
DROP PROC CRUD_DivisionCreate
END
GO
CREATE PROCEDURE CRUD_DivisionCreate
			@name_division nvarchar(50),
			@sponsor_id int
AS
BEGIN
DECLARE @division_id int
BEGIN TRY
IF(dbo.checkSponsor(@sponsor_id)=1)
	BEGIN
	INSERT INTO Division(name_division, sponsor_id)
		VALUES (@name_division, @sponsor_id)
	SET @division_id = SCOPE_IDENTITY()
	SELECT
			division_id = @division_id,
			name_division = @name_division,
			sponsor_id = @sponsor_id
	FROM Division
	WHERE division_id = @division_id
	END
ELSE
	THROW 50000, 'The Sponsor does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/*CRUD _ DIVISION _ READ */

GO
IF OBJECT_ID('CRUD_DivisionRead') IS NOT NULL
BEGIN
DROP PROC CRUD_DivisionRead
END
GO
CREATE PROCEDURE CRUD_DivisionRead
	@division_id int
AS
BEGIN
BEGIN TRY
IF (dbo.checkDivision(@division_id)=1)
BEGIN
	SELECT division_id, name_division, sponsor_id
	FROM Division
	WHERE (division_id = @division_id)
END
ELSE
	THROW 50000, 'The Division does not exist',1;
END TRY
BEGIN CATCH
	PRINT ERROR_MESSAGE()
END CATCH
END
GO

/* CRUD _ DIVISION _ UPDATE */

GO
IF OBJECT_ID('CRUD_DivisionUpdate') IS NOT NULL
BEGIN
DROP PROC CRUD_DivisionUpdate
END
GO
CREATE PROCEDURE CRUD_DivisionUpdate
	@division_id_given int,
	@name_division nvarchar(50),
	@sponsor_id int
AS
BEGIN
DECLARE @division_id int
BEGIN TRY
IF(dbo.checkSponsor(@sponsor_id)=1 AND dbo.checkDivision(@division_id_given)=1)
	BEGIN
		UPDATE Division
		SET name_division = @name_division,
				sponsor_id = @sponsor_id
		WHERE (division_id = @division_id_given)
	END
ELSE
	THROW 50000, 'The Sponsor or Division does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/* CRUD _ DIVISION _ DELETE */

GO
IF OBJECT_ID('CRUD_DivisionDelete') IS NOT NULL
BEGIN
DROP PROC CRUD_DivisionDelete
END
GO
CREATE PROCEDURE CRUD_DivisionDelete
	@division_id_given int
AS
BEGIN
BEGIN TRY
IF (dbo.checkDivision(@division_id_given)=1)
	BEGIN	
		DELETE FROM Division
		WHERE (division_id = @division_id_given)
	END
ELSE
	THROW 50000, 'The Division does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END
/*
DBCC CHECKIDENT ('[SPONSORS]', RESEED, 0);
GO
*/
/* CRUD _ SPONSORS _ CREATE */

GO
IF OBJECT_ID('CRUD_SponsorsCreate') IS NOT NULL
BEGIN
DROP PROC CRUD_SponsorsCreate
END
GO
CREATE PROCEDURE CRUD_SponsorsCreate
			@name_sponsor nvarchar(50),
			@country_id int
AS
BEGIN
DECLARE @sponsor_id int
BEGIN TRY
IF(dbo.checkCountry(@country_id)=1)
	BEGIN
	INSERT INTO Sponsors(name_sponsor, country_id)
		VALUES (@name_sponsor, @country_id)
	SET @sponsor_id = SCOPE_IDENTITY()
	SELECT
			sponsor_id = @sponsor_id,
			name_sponsor = @name_sponsor,
			country_id = @country_id
	FROM Sponsors
	WHERE sponsor_id = @sponsor_id
	END
ELSE
	THROW 50000, 'The Country does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/*CRUD _ SPONSORS _ READ */

GO
IF OBJECT_ID('CRUD_SponsorsRead') IS NOT NULL
BEGIN
DROP PROC CRUD_SponsorsRead
END
GO
CREATE PROCEDURE CRUD_SponsorsRead
	@sponsor_id int
AS
BEGIN
BEGIN TRY
IF (dbo.checkSponsor(@sponsor_id)=1)
	BEGIN
		SELECT sponsor_id, name_sponsor, country_id
		FROM Sponsors
		WHERE (sponsor_id = @sponsor_id)
	END
ELSE
	THROW 50000, 'The Sponsor does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/* CRUD _ SPONSORS _ UPDATE */

GO
IF OBJECT_ID('CRUD_SponsorsUpdate') IS NOT NULL
BEGIN
DROP PROC CRUD_SponsorsUpdate
END
GO
CREATE PROCEDURE CRUD_SponsorsUpdate
	@sponsor_id_given int,
	@name_sponsor nvarchar(50),
	@country_id int
AS
BEGIN
BEGIN TRY
IF(dbo.checkSponsor(@sponsor_id_given)=1 AND dbo.checkCountry(@country_id)=1)
	BEGIN
		UPDATE Sponsors
		SET name_sponsor = @name_sponsor,
		country_id = @country_id
			WHERE (sponsor_id = @sponsor_id_given)
	END
ELSE
	THROW 50000, 'The Sponsor or country does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END


/* CRUD _ SPONSORS _ DELETE */

GO
IF OBJECT_ID('CRUD_SponsorsDelete') IS NOT NULL
BEGIN
DROP PROC CRUD_SponsorsDelete
END
GO
CREATE PROCEDURE CRUD_SponsorsDelete
	@sponsor_id_given int
AS
BEGIN
BEGIN TRY
IF (dbo.checkSponsor(@sponsor_id_given)=1)
	BEGIN
		DELETE FROM Sponsors
		WHERE (sponsor_id = @sponsor_id_given)

	END
ELSE
	THROW 50000, 'The Sponsor does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/*
DBCC CHECKIDENT ('[SPONSORTEAM]', RESEED, 0);
GO
*/

/* CRUD _ SPONSORTEAM _ CREATE */


/* [personal comment] Ai de verificat daca exista Sponsor_id, daca exista Team_id, daca a mai fost pana acum o legatura intre ele. Daca nu => create */

GO
IF OBJECT_ID('CRUD_STCreate') IS NOT NULL
BEGIN
DROP PROC CRUD_STCreate
END
GO
CREATE PROCEDURE CRUD_STCreate
			@team_id_given int,
			@sponsor_id_given int
AS
BEGIN
BEGIN TRY
IF (dbo.checkTeam(@team_id_given)=1 AND dbo.checkSponsor(@sponsor_id_given)=1 AND dbo.checkST(@team_id_given,@sponsor_id_given)=0)
	BEGIN
		INSERT INTO SponsorTeam
		VALUES(@team_id_given, @sponsor_id_given)
		SELECT team_id = @team_id_given,
			sponsor_id = @sponsor_id_given
		FROM SponsorTeam
		WHERE sponsor_id = @sponsor_id_given 
			AND team_id = @team_id_given
	END
ELSE IF (dbo.checkTeam(@team_id_given)=1 AND dbo.checkSponsor(@sponsor_id_given)=1 AND dbo.checkST(@team_id_given,@sponsor_id_given)=1)
	THROW 50000, 'The Team is already sponsored by this company',1;
ELSE 
	THROW 50000, 'The Sponsor or Team does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END	

/* CRUD _ SPONSORTEAM _ READ */

GO
IF OBJECT_ID('CRUD_STRead') IS NOT NULL
BEGIN
DROP PROC CRUD_STRead
END
GO
CREATE PROCEDURE CRUD_STRead
	@team_id int,
	@sponsor_id int
AS
BEGIN
BEGIN TRY
IF (dbo.checkST(@team_id, @sponsor_id)=1)
	BEGIN
		SELECT team_id, sponsor_id
		FROM SponsorTeam
		WHERE (sponsor_id = @sponsor_id AND team_id = @team_id)
	END
ELSE
	THROW 50000, 'The sponsorship does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/* CRUD _ SPONSORTEAM _ UPDATE */

GO
IF OBJECT_ID('CRUD_STUpdate') IS NOT NULL
BEGIN
DROP PROC CRUD_STUpdate
END
GO
CREATE PROCEDURE CRUD_STUpdate
	@team_id_given int,
	@sponsor_id_given int,
	@new_sponsor_id int
AS
BEGIN
BEGIN TRY
IF(dbo.checkST(@team_id_given,@sponsor_id_given)=1 AND dbo.checkSponsor(@new_sponsor_id)=1)
	BEGIN
		UPDATE SponsorTeam
		SET sponsor_id = @new_sponsor_id
		WHERE (sponsor_id = @sponsor_id_given AND team_id = @team_id_given)
	END
ELSE IF(dbo.checkST(@team_id_given,@sponsor_id_given)=0)
	THROW 50000, 'The Sponsorship does not exist',1;
ELSE
	THROW 50000, 'The new sponsor does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/* CRUD _ SPONSORTEAM _ DELETE */

GO
IF OBJECT_ID('CRUD_STDelete') IS NOT NULL
BEGIN
DROP PROC CRUD_STDelete
END
GO
CREATE PROCEDURE CRUD_STDelete
	@team_id_given int,
	@sponsor_id_given int
AS
BEGIN
BEGIN TRY
IF (dbo.checkST(@team_id_given,@sponsor_id_given)=1)
	BEGIN
		DELETE FROM SponsorTeam
		WHERE (sponsor_id = @sponsor_id_given AND team_id = @team_id_given)
	END
ELSE
	THROW 50000, 'The sponsorship does not exist',1;
END TRY
BEGIN CATCH 
	PRINT ERROR_MESSAGE();
END CATCH
END

/* Mai departe trebuie facute doar view-urile care sa foloseasca non-clustered index-ul, pe care-l creati in functie de ce puneti la WHERE */


/* VIEW 1 */

GO
ALTER VIEW CRUD_VIEW1
AS
SELECT C.salary
FROM Casters C
WHERE C.salary > 3000
GO



/* SELECT SALARY NON-CLUSTERED INDEX - CASTERS */

SELECT C.salary
FROM Casters C
WHERE C.salary > 3000


/* VIEW 2 */

GO
ALTER VIEW CRUD_VIEW2
AS
SELECT S.country_id
FROM Sponsors S
WHERE S.country_id=9
GO

/* script care-ti da un tabel cu toate informatiile care trebuie verificate de profa */
/* SELECT COUNTRY_ID NON-CLUSTERED INDEX - SPONSORS */

SELECT COUNT( S.country_id)
FROM Sponsors S
WHERE S.country_id=9

SELECT * FROM CRUD_VIEW1
SELECT * FROM CRUD_VIEW2

SELECT   OBJECT_NAME(S.[OBJECT_ID]) AS [OBJECT NAME], 
         I.[NAME] AS [INDEX NAME], 
         USER_SEEKS, 
         USER_SCANS, 
         USER_LOOKUPS, 
         USER_UPDATES 
FROM     SYS.DM_DB_INDEX_USAGE_STATS AS S 
         INNER JOIN SYS.INDEXES AS I 
           ON I.[OBJECT_ID] = S.[OBJECT_ID] 
              AND I.INDEX_ID = S.INDEX_ID 
WHERE    OBJECTPROPERTY(S.[OBJECT_ID],'IsUserTable') = 1 
