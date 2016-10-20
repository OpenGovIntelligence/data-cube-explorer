var pivotTableView = pivotTableView || {};
pivotTableView.data = [];

pivotTableView.update = function() {
    var dataset = $('#select-dataset').val();
    if (dataset < 0) {
        $("#ds-name").html("");
        $("#ds-description").html("");
        $("#output").html("");
        return;
    }
    numnberOfRecords = $("#select-numrecords").val();
    var url = "/api/listdataofLqb?dsuri=" + encodeURIComponent(pivotTableView.data[$('#select-dataset').val()].dataset) + "&fuseki=8080&limit=" + numnberOfRecords;
    console.log(url)
    $("#ds-name").html(pivotTableView.data[dataset].title);
    $("#ds-description").html(pivotTableView.data[dataset].description);
    $("#output").html("loading...");
    var renderers = $.extend(
            $.pivotUtilities.renderers,
            $.pivotUtilities.c3_renderers,
            $.pivotUtilities.d3_renderers,
            $.pivotUtilities.export_renderers
            );
    $.getJSON(url, function(mps) {
        $("#output").pivotUI(mps["result"], {
            renderers: renderers,
            cols: [], rows: []
        });
    });
};
$(function() {
    $('#select-dataset').on('change', function() {
        pivotTableView.update();
    });
    $('#select-numrecords').on('change', function() {
        pivotTableView.update();
    });
    $("#select-dataset").append($("<option></option>").attr("value", -1).text("None"));
    $.getJSON("/api/listLqbs?limit=10&fuseki=8080", function(_data) {
        pivotTableView.data = _data["result"];
        for (i = 0; i < pivotTableView.data.length; i++) {
            $("#select-dataset").append($("<option></option>").attr("value", i).text(pivotTableView.data[i].title));
        }
    });

});