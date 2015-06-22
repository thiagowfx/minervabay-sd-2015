$(document).ready(function () {
    $("#buttonSearch").click(doButtonSearch);
    $("#buttonClearTable").click(doButtonClearTable);
});

function doPopulateTable(json) {
    clearTable();
    var tbody = $("#tableSearch>tbody");

    $.each(json.data, function (index, value) {
        var columns = "";
        columns += '<td>' + value.title + '</td>';
        columns += '<td>' + value.author + '</td>';
        columns += '<td>' + value.publisher + '</td>';
        columns += '<td>' + value.category + '</td>';
        columns += '<td>' + value.isbn + '</td>';
        columns += '<td><input type="image" src="assets/img/delete.png" width="13%" height="13%" onclick="doButtonDelete(' + parseInt(value.id, 10) + ')"></td>';

        var row = '<tr id="row' + value.id + '">' + columns + '</tr>';
        tbody.append(row);
    });
}

function doButtonSearch() {
    var data = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "searchBook",
        "params": [
            {
                "search_string": $("#idSearchTitle").val(),
                "search_criteria": $('#idSelectSearch :selected').val()
            }
        ]
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8081');

    xhr.onload = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            doPopulateTable(JSON.parse(xhr.responseText).result);
        } else {
            window.alert("Ocorreu um erro ao tentar procurar livros no banco de dados.");
        }
    };

    xhr.send(JSON.stringify(data));
}

function doButtonSubmit() {
    var data = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "addBook",
        "params": [
            {
                title: $("#title").val(),
                author: $("#author").val(),
                publisher: $("#publisher").val(),
                category: $("#autocomplete").val(),
                isbn: $("#isbn").val()
            }
        ]
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8081');

    xhr.onload = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.result) {
                $("#messageSubmit").html('Dados submetidos com sucesso.');
                $("#contact-form button[type=reset]").click();
            } else {
                $("#messageSubmit").html('Erro ao adicionar o novo registro.');
            }
        } else {
            $("#messageSubmit").html('Ocorreu um erro na submissão dos dados.');
        }
    };

    xhr.send(JSON.stringify(data));
}

function clearTable() {
    $("#tableSearch>tbody").html('');
}

function doButtonClearTable() {
    $("#idSearchTitle").val('');
    $("#tableSearch>tbody").html('<tr class="no-records-found"><td colspan="5">No matching records found</td></tr>');
}

function doButtonDelete(id) {
    var data = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "deleteBook",
        "params": [
            {
                "id": parseInt(id, 10)
            }
        ]
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8081');

    xhr.onload = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.result) {
                window.alert("Registro deletado com sucesso do banco de dados.");
                $("#row" + id).remove();
            } else {
                window.alert("Ocorreu um erro ao tentar deletar o livro do banco de dados.");
            }
        } else {
            window.alert("Ocorreu um erro ao tentar se comunicar com o banco de dados para deletar o livro.");
        }
    };

    xhr.send(JSON.stringify(data));
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
        submitHandler: function (form) {
            doButtonSubmit();
        },
        highlight: function (element) {
            $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
        },
        success: function (element) {
            element.text('OK!').addClass('valid').closest('.form-group').removeClass('has-error').addClass('has-success');
        }
    });
});