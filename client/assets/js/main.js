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

// messageSubmit

function doPopulateTable() {
    // TODO
}

function doButtonSearch() {
    // TODO
}

function doButtonSubmit() {
    // TODO
}

function doButtonClearTable() {
    $("#tableSearch>tbody").html('<tr class="no-records-found"><td colspan="5">No matching records found</td></tr>');
}