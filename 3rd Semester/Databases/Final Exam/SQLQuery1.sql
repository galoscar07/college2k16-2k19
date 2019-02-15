-- DATABASE PRACTICLE EXAM !!!!!!!!!!!!!!!!!!!

--Droping the tables if they already exists:
IF OBJECT_ID('Products','U') IS NOT NULL
	DROP TABLE Products
IF OBJECT_ID('EmployeesDeposits','U') IS NOT NULL
	DROP TABLE EmployeesDeposits 
IF OBJECT_ID('Deposits','U') IS NOT NULL
	DROP TABLE Deposits
IF OBJECT_ID('Employees','U') IS NOT NULL
	DROP TABLE Employees
GO

--Creating the tables:
CREATE TABLE Deposits
	(depoName VARCHAR(50) PRIMARY KEY,
	typeDepo VARCHAR(500))
CREATE TABLE Employees
	(empId SMALLINT PRIMARY KEY IDENTITY(1,1),
	empName VARCHAR(50),
	salary INT)
CREATE TABLE Products
	(prodId SMALLINT PRIMARY KEY IDENTITY(1,1),
	prodName VARCHAR(50),
	startDate DATE,
	endDate DATE,
	empId SMALLINT REFERENCES Employees(empId))
CREATE TABLE EmployeesDeposits
	(empId SMALLINT REFERENCES Employees(empId),
	depoName VARCHAR(50) REFERENCES Deposits(depoName),
	job VARCHAR(50),
	PRIMARY KEY (empId,depoName))

--Insert values into the database
INSERT Employees VALUES ('Oscar Gal', 670), ('Comsa Mihai', 160), ('Limbean Anamaria', 400)
INSERT Deposits VALUES ('Alba Iulia','sell'), ('Cluj Napoca', 'order'), ('Iasi', 'buy')
INSERT Products VALUES('Coca Cola','2018-02-02' , '2018-02-10', 1), ('Dunhill', '2018-02-08', '2018-02-20', 1), ('Clear', '2018-02-02', '2019-02-02', 2), ('OMO', '2018-02-02','2019-02-02',3)
INSERT EmployeesDeposits(empId, depoName, job) VALUES(1,'Alba Iulia', 'manager'), (1, 'Cluj Napoca', 'administrator'), (3, 'Iasi', 'cleaning')
GO

-- Print everything that is in the database
SELECT * FROM Employees
--SELECT * FROM Deposits
SELECT * FROM Products
--SELECT * FROM EmployeesDeposits
GO

-- b) Procedure that add a new job for an employee and a deposit given. If the job exists, update the position
ALTER PROC uspAddNewJob @DepoName VARCHAR(50), @JobName VARCHAR(100), @EmpId SMALLINT
AS
	DECLARE @Depo VARCHAR(50) = (SELECT DepoName FROM Deposits WHERE depoName = @DepoName),
	@Emp SMALLINT = (SELECT empId FROM Employees WHERE empId = @EmpId)
	IF EXISTS (SELECT * FROM EmployeesDeposits WHERE empId = @Emp AND depoName = @Depo)
		UPDATE EmployeesDeposits
		SET job = @JobName
		WHERE empId = @Emp AND depoName = @Depo
	ELSE
		INSERT EmployeesDeposits(empId,depoName,job)
		VALUES(@EmpId,@DepoName,@JobName)
GO

--The procedure that will add the position
--SELECT * FROM EmployeesDeposits
--EXEC uspAddNewJob @DepoName = 'Mures', @JobName = 'admin', @EmpId = 2
--SELECT * FROM EmployeesDeposits
--GO

--The procedure that update a position
--SELECT * FROM EmployeesDeposits
--EXEC uspAddNewJob @DepoName = 'Cluj Napoca', @JobName = 'admin', @EmpId = 1 
--SELECT * FROM EmployeesDeposits
--GO

--c) The view
ALTER VIEW vProductsEmployeesSalaryBiggerThan
AS
SELECT prodName AS "Product Name:"
FROM Products P
INNER JOIN Employees E ON E.empId = P.empId
WHERE E.salary > 500
GO
--SELECT * FROM vProductsEmployeesSalaryBiggerThan
--GO


--d) the function
ALTER FUNCTION numberOfProductsForEachDeposit(@Year INT)
RETURNS TABLE
AS
RETURN SELECT  D.depoName, D.typeDepo AS 'Type' , COUNT(P.prodId) AS Number
		FROM Products P
		INNER JOIN Employees E ON P.empId=E.empId
		INNER JOIN EmployeesDeposits ED ON E.empId=ED.empId
		INNER JOIN Deposits D ON ED.depoName=D.depoName
		WHERE P.endDate < DATEFROMPARTS ( @Year, 12, 31 ) 
		GROUP BY D.depoName, D.typeDepo
GO

SELECT * FROM numberOfProductsForEachDeposit(2018)
GO