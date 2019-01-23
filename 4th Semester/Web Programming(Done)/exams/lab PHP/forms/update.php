<?php
    session_start();

    include_once '../functions/update.php';
    include_once '../lib/utils.php';

    $id = test_input($_POST["id"]);
    $model = test_input($_POST["model"]);
    $power = test_input($_POST["power"]);
    $fuel = test_input($_POST["fuel"]);
    $price = test_input($_POST["price"]);
    $age = test_input($_POST["age"]);
    $color = test_input($_POST["color"]);

    if ($model == "" || $model == null || $power == "" || $power == null || $fuel == "" || $fuel == null || $price == "" || $price == null || $age == "" || $age == null) {
        $_SESSION['error'] .= "Update car failed. All fields must be filled correctly.";
        header("Location: ../update.php?id=" . $id);
    } else {

        update_car($id, $model, $power, $fuel, $price, $color, $age);

        header("Location: ../index.php");
    }
?>