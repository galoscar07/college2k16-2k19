<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Travel</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="script.js">
    </script>
</head>
<body>
<table id="cities" border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>County</th>
    </tr>
    <tbody id="tableBody">
    </tbody>
</table>
<table id="links" border="1">
    <thead>
        <th>ID</th>
        <th>City1</th>
        <th>City2</th>
        <th>Duration</th>
        <th>Distance</th>
    </thead>
    <tbody id="linkBody">
    </tbody>
</table>
<div id="sel">
    <input id="order" type="button" value="Order" style="" />
    <input id="delete" type="button" value="Delete selected" style="" />
    Selected city: <span id="selectedCity"></span>
</div>
<div>
    <input id="back" type="button" value="Back"/>
    <input id="next" type="button" value="Next"/>
    <input id="final" type="button" value="Set Final Destination"/>
    <input id="route" type="button" value="Show Route"/>
</div>
<div id="finalRoute"></div>
<div id="allRoutes"></div>
</body>
</html>