<?php
    session_start();

    
    include_once '../functions/add.php';
    include_once '../lib/utils.php';

    $model = test_input($_POST["model"]);
    $power = test_input($_POST["power"]);
    $fuel = test_input($_POST["fuel"]);
    $price = test_input($_POST["price"]);
    $age = test_input($_POST["age"]);
    $color = test_input($_POST["color"]);

    if ($model == "" || $model == null || $power == "" || $power == null || $fuel == "" || $fuel == null || $price == "" || $price == null || $age == "" || $age == null) {
        $_SESSION['error'] .= "Add car failed. All required fields must be filled correctly.";
        header("Location: ../add.php");
    }

    add_car($model, $power, $fuel, $price, $color, $age);

    header("Location: ../index.php");
?>
