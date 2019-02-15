$(document).ready(function() {
    var selectedRow = 0;
    var selectedCity = null;
    var finalRoute = [];
    var allRoutes = [];

    getDepartures();
    $("#route").css("display", "none");

    function renderTable(data) {
        var trHTML = '';
        $.each(data, function(i, item) {
            trHTML += '<tr><td>' + item.id + '</td><td>' + item.name + '</td><td>' + item.county + '</td></tr>';
        });

        $('#tableBody').html(trHTML);
        $('#cities').show();
    }

    function renderLinks(data) {
        var trHTML = '';
        $.each(data, function(i, item) {
            trHTML += '<tr><td>' + item.idlink + '</td><td>' + item.city1 + '</td><td>' + item.city2 + '</td><td>' + item.duration + '</td><td>' + item.distance + '</td></tr>';
        });

        $('#linkBody').html(trHTML);
        $('#links').show();
    }

    function getDepartures() {
        $.getJSON(
            "getDepartures.php",
            renderTable,
        );
        $("#back").css("display", "none");
        $("#final").css("display", "none");
        $("#links").css("display", "none");
        $("#order").css("display", "none");
        $("#delete").css("display", "none");
    }

    $("#tableBody").on("click", "tr", function() {
        selectedCity = $(this).find("td").eq(1).html();
        $("#selectedCity").text(selectedCity);
    });

    $("#linkBody").on("click", "tr", function() {
        selectedRow = $(this).index();
        selectedCity = $(this).find("td").eq(2).html();
        $("#selectedCity").text(selectedCity);
        // $("#order").show();
    });


    $("#next").click(function() {
        $.getJSON(
            "getIntermediary.php", { name: selectedCity },
            renderLinks
        );
        finalRoute.push(selectedCity);
        // allRoutes.push(selectedCity);
        $("#back").show();
        $("#final").show();
        $("#cities").css("display", "none");
        $("#order").show();
        $("#delete").show();
    });

    $("#back").click(function() {
        console.log("Back");
        var newRoute = finalRoute.slice(0);
        allRoutes.push(newRoute);
        if (finalRoute.length === 1) {
            finalRoute.splice(-1, 1);
            getDepartures();
        } else {
            selectedCity = finalRoute[finalRoute.length - 2];
            finalRoute.splice(-2, 2);
            $("#next").trigger("click");
        }
    });

    $("#final").click(function() {
        finalRoute.push(selectedCity);
        allRoutes.push(finalRoute);
        $("#route").show();
    });

    $("#route").click(function() {
        $('body > :not(#finalRoute,#allRoutes,#header)').hide();
        var fin = "<b>Final route: </b>";
        for (var r of finalRoute)
            fin += r + '\n';
        var all = "<b>All routes: </b><br>";
        for (var r of allRoutes)
            all += r + '<br>';
        $("#finalRoute").html(fin);
        $("#allRoutes").html(all);
    });

    $("#order").click(function() {
        var table = document.getElementById("links");
        var tb = table.tBodies[0];
        var rows = Array.prototype.slice.call(tb.rows, 0),
            i;
        rows = rows.sort(function(a, b) {
            return (0.6 * parseInt(a.cells[3].textContent) + 0.4 * parseInt(a.cells[4].textContent) <
                0.6 * parseInt(b.cells[3].textContent) + 0.4 * parseInt(b.cells[4].textContent) ? 1 : -1);
        });

        for (i = 0; i < rows.length; ++i) {
            tb.appendChild(rows[i]);
        }
    });

    $("#delete").click(function() {
        document.getElementById("links").deleteRow(selectedRow + 1);
    });

});