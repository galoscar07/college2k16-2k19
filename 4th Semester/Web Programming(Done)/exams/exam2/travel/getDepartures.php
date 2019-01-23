<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "exam";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM city";

$stmt = $conn->prepare($sql);
$stmt->execute();
$stmt->bind_result($id, $name, $county);

$cities = array();

while ($stmt->fetch()) {
    $city = new StdClass();
    $city->id = $id;
    $city->name = $name;
    $city->county = $county;

    array_push($cities, $city);
}

echo json_encode($cities);

$stmt->close();
$conn->close();
?>

