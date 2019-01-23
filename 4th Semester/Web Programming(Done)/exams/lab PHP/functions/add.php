<?php

    function add_car($model, $power, $fuel, $price, $color, $age) {
      include_once '../config/database.php';

        try {
              $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
              $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

              $connect->query("USE " . $DB_NAME);

              $stmt = $connect->prepare("INSERT INTO cars (model, power, fuel, price, color, age) VALUES (:model, :power, :fuel, :price, :color, :age)");
              $stmt->execute(array(":model" => $model, ":power" => $power, ":fuel" => $fuel, ":price" => $price, ":color" => $color, ":age" => $age));

        }
        catch (PDOException $pikachu) {
            $_SESSION['error'] = "Error: " . $pikachu->getMessage();
        }
    }

?>
