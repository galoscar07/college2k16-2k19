<?php
  // Connect to the database server

  $connect = NULL;

  try {
    $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
    $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  }
  catch (PDOException $pikachu) {
    echo "DB connection failed: " . $pikachu->getMessage();
  }

  // Create the database

  try {
    $sql = "CREATE DATABASE IF NOT EXISTS " . $DB_NAME;
    $connect->query($sql);
  }
  catch (PDOException $pikachu) {
    echo "DB creation faild: " . $pikachu->getMessage();
  }

  $connect->query("USE " . $DB_NAME);

  // Create table cars

  try {
    $sql = "CREATE TABLE IF NOT EXISTS cars (
		  id int(8) NOT NULL,
		  model varchar(255) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
		  power int(4) NOT NULL,
		  fuel varchar(100) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
		  price int(9) NOT NULL,
		  color varchar(50) CHARACTER SET latin1 COLLATE latin1_general_ci DEFAULT NULL,
		  age int(3) NOT NULL
		) ENGINE=MyISAM DEFAULT CHARSET=latin1;
		ALTER TABLE cars
		  ADD PRIMARY KEY (id);
		ALTER TABLE cars
		  MODIFY id int(8) NOT NULL AUTO_INCREMENT;
    	)";
    $connect->query($sql);
  }
  catch (PDOException $pikachu) {
    echo $sql . "<br>" . $pikachu->getMessage();
  }
?>
