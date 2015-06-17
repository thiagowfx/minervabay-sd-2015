$(document).ready(function () {
    $("#buttonSearch").click(doButtonSearch);
    $("#buttonSubmit").click(doButtonSubmit);
    $("#buttonClearTable").click(doButtonClearTable);
});

//<tr>
//                    <td>Romeu</td>
//                    <td>Julieta</td>
//                    <td>UFRJ</td>
//                    <td>Drama</td>
//                    <td>123123</td>
//                </tr>

1 // messageSubmit

function doPopulateTable(json) {
    //    TEST:
    //    json = {
    //        data: [
    //            {
    //                title: "t",
    //                author: "a",
    //                publisher: "p",
    //                autocomplete: "c",
    //                isbn: "i"
    //            },
    //            {
    //                title: "t2",
    //                author: "a2",
    //                publisher: "p2",
    //                autocomplete: "c2",
    //                isbn: "i2"
    //            }
    //        ]
    //    };

    clearTable();
    var tbody = $("#tableSearch>tbody");

    $.each(json.data, function (index, value) {
        var columns = "";
        columns += '<td>' + value.title + '</td>';
        columns += '<td>' + value.author + '</td>';
        columns += '<td>' + value.publisher + '</td>';
        columns += '<td>' + value.autocomplete + '</td>';
        columns += '<td>' + value.isbn + '</td>';

        var row = '<tr>' + columns + '</tr>';
        tbody.append(row);
    });
}

function doButtonSearch() {
    // TODO
}

function doButtonSubmit() {
    // TODO
}

function clearTable() {
    $("#tableSearch>tbody").html('');
}

function doButtonClearTable() {
    $("#tableSearch>tbody").html('<tr class="no-records-found"><td colspan="5">No matching records found</td></tr>');
}