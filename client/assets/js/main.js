$(document).ready(function () {
    $("#buttonSearch").click(doButtonSearch);
    $("#buttonClearTable").click(doButtonClearTable);
});

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
    $.ajax({
        url: 'rpc',
        method: 'POST',
        data: {
            title: $("#title").val(),
            author: $("#author").val(),
            publisher: $("#publisher").val(),
            autocomplete: $("#autocomplete").val(),
            isbn: $("#isbn").val()
        },
        success: function (data, status, jqxhr) {
            $("#messageSubmit").html('Dados submetidos com sucesso.');
        },
        error: function () {
            $("#messageSubmit").html('Ocorreu um erro na submissão dos dados.');
        }
    });
}

function clearTable() {
    $("#tableSearch>tbody").html('');
}

function doButtonClearTable() {
    $("#tableSearch>tbody").html('<tr class="no-records-found"><td colspan="5">No matching records found</td></tr>');
}


//////////////////////// THIRD-PARTY CODE ////////////////////////////////

$(document).ready(function () {
    /* 
     * Validate
     * http://bassistance.de/jquery-plugins/jquery-plugin-validation/
     * http://docs.jquery.com/Plugins/Validation/
     * http://docs.jquery.com/Plugins/Validation/validate#toptions
     */

    $('#contact-form').validate({
        rules: {
            title: {
                minlength: 2,
                required: true
            },
            autocomplete: {
                required: true
            },
            password: {
                required: true,
                password: true
            },
            publisher: {
                minlength: 2,
                required: true
            },
            username: {
                minlength: 2,
                username: true,
                required: true
            },
            author: {
                minlength: 2,
                required: true
            },
            isbn: {
                isbn: true,
                required: true
            },
            name: {
                minlength: 2,
                required: true
            },
            email: {
                required: true,
                email: true
            },
            subject: {
                minlength: 2,
                required: true
            },
            message: {
                minlength: 2,
                required: true
            }
        },
        submitHandler: doButtonSubmit,
        highlight: function (element) {
            $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
        },
        success: function (element) {
            element.text('OK!').addClass('valid').closest('.form-group').removeClass('has-error').addClass('has-success');
        }
    });

});