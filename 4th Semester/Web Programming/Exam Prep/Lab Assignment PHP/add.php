<?php
  session_start();
    include 'lib/includes.php';
  include 'partials/header.php';
?>


  <form method="post" action="forms/add.php">
    Model: <br> <input type="text" name="model" required> <br><br>
        Horse Power: <br> <input type="text" name="power" required> <br><br>
    Fuel: <br> <input type="text" name="fuel" required> <br><br>
    Price: <br> <input type="text" name="price" required> <br><br>
    Color*: <br> <input type="text" name="color"> <br><br>
    Age: <br> <input type="text" name="age" required> <br><br>
    <input type="submit" name="submit" value="Add car">
  </form>
  <br>
  <p>(*) - Optional field</p>
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
