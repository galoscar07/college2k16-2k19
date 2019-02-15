<?php
  function update_car($id, $model, $power, $fuel, $price, $color, $age) {
      include_once '../config/database.php';

        try {
              $connect = new PDO($DB_DSN, $DB_USER, $DB_PASSWORD);
              $connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

              $connect->query("USE " . $DB_NAME);

              $stmt = $connect->prepare("UPDATE cars SET model=:model, power=:power, fuel=:fuel, price=:price, color=:color, age=:age WHERE id=:id");
              $stmt->execute(array(":model" => $model, ":power" => $power, ":fuel" => $fuel, ":price" => $price, ":color" => $color, ":age" => $age, ":id" => $id));

        }
        catch (PDOException $pikachu) {
            $_SESSION['error'] = "Error: " . $pikachu->getMessage();
        }
    }

?>