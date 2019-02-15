<?php
  session_start();
  include 'lib/includes.php';
  include 'partials/header.php';
?>

<button onclick="addCar()">
  Add a car
</button>

<input id="queryInput" type="text" value=""/>
<button onclick="getCars()">
  Filter model
</button>

<br>

<table id="carsTable">

</table>

<script>
  $('document').ready(function() {
    getCars();
  });

  function getCars() {

    var query = $('#queryInput').val();
    $('#carsTable').empty();
    $.ajax({
      url: "api/cars.php?query=" + query,
      success: function(result) {
        var obj = jQuery.parseJSON(result);
        $.each( obj, function( key, value ) {
          var id = value['id'];
            var model = value['model'];
            var power = value['power'];
            var fuel = value['fuel'];
            var price = value['price'];
            var color = value['color'];
            var age = value['age'];
            $('#carsTable').append('<tr class="row"> <div class="cell"> <td><input class="theInput" type="text" value="' + model + '" readonly></td><td><input class="theInput" type="text" value="' + power + '" readonly></td><td><input class="theInput" type="text" value="' + fuel + '" readonly></td><td><input class="theInput" type="text" value="' + price + '" readonly></td><td><input class="theInput" type="text" value="' + color + '" readonly></td><td><input class="theInput" type="text" value="' + age + '" readonly></td></div><td class="special"><button type="button" class="update" onclick="updateCar(' + id + ')">Update</button></td><td class="special"><button type="button" class="delete" onclick="deleteCar(' + id + ')">Delete</button></td></tr>');
        });
        
      }
    });
  }

  function addCar() {
    window.location = "add.php";
  }

  function deleteCar(id) {
    console.log("I should delete the car with id: " + id);
    window.location = "./forms/delete.php?id=" + id;
  }

  function updateCar(id) {
    window.location = "update.php?id=" + id;
  }
</script>

<?php

  include 'partials/footer.php';
?>
