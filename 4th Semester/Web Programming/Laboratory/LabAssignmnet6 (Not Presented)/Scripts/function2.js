    $(".dropzone").on("dragover", function(ev) {
        ev.preventDefault();
    });
    $(".dropzone").on("drop", function(ev) {
        ev.preventDefault();
        var data = ev.originalEvent.dataTransfer.getData("text");
        this.appendChild(document.getElementById(data));
    });

    $(".draggable").each(function(i) {
        if ($(this).attr('id') == null) {
            $(this).attr('id', 'draggable' + i);
        }
    });
    $(".draggable").on("dragstart", function(ev) {
        ev.originalEvent.dataTransfer.setData("text", ev.target.id);
    });