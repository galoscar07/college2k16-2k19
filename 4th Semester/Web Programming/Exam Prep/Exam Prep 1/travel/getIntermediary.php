<?php

$orName = $_GET["name"];

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

$sql = "SELECT IDLink, (SELECT Name FROM city WHERE ID=IDCity1), (SELECT name FROM city WHERE id=idcity2), duration, distance FROM link WHERE IDCity1=(select ID from city where Name=?)";

$stmt = $conn->prepare($sql);
$stmt->bind_param("s", $orName);
$stmt->execute();
$stmt->bind_result($idlink, $city1, $city2, $duration, $distance);

$routes = array();

while ($stmt->fetch()) {
    $route = new StdClass();
    $route->idlink = $idlink;
    $route->city1 = $city1;
    $route->city2 = $city2;
    $route->duration = $duration;
    $route->distance = $distance;

    array_push($routes, $route);
}

echo json_encode($routes);

$stmt->close();
$conn->close();
?>

