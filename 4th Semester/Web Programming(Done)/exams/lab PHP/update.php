<?php
  session_start();
  include 'partials/header.php';
  include 'functions/read.php';

  $id = $_GET['id'];

  if ($id == "" || $id == null || !is_numeric($id)) {
    $_SESSION['error'] = "Car not found";
    header('Location: add.php');
  }

  $car = get_car_by_id($id);

  if ($car == null) {
    $_SESSION['error'] = "Car not found";
    header('Location: add.php');
  }

  $model = $car["model"];
  $power = $car["power"];
  $fuel = $car["fuel"];
  $price = $car["price"];
  $age = $car["age"];
  $color = $car["color"];
?>


  <form method="post" action="forms/update.php">
    <input name="id" hidden value=<?php echo '"' . $id . '"'; ?>>
    Model: <br> <input type="text" name="model" value=<?php echo '"' . $model . '"'; ?>> <br><br>
        Horse Power: <br> <input type="text" name="power" value=<?php echo '"' . $power . '"'; ?>> <br><br>
    Fuel: <br> <input type="text" name="fuel" value=<?php echo '"' . $fuel . '"'; ?>> <br><br>
    Price: <br> <input type="text" name="price" value=<?php echo '"' . $price . '"'; ?>> <br><br>
    Color: <br> <input type="text" name="color" value=<?php echo '"' . $color . '"'; ?>> <br><br>
    Age: <br> <input type="text" name="age" value=<?php echo '"' . $age . '"'; ?>> <br><br>
    <input type="submit" name="submit" value="Update car">
  </form>
  <br>
    <span>
            <?php
            echo $_SESSION['error'];
            $_SESSION['error'] = null;
            ?>
    </span>


<?php
  include 'partials/footer.php';
?>
