$(() => {
    // function will get executed
    // on click of submit button
    $("#source-city").change(function(ev) {
        var form = $("#search_flight_form");
        var url = form.attr('action');
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(),
            success: function(data) {

                // Ajax call completed successfully
                alert("Form Submited Successfully");
            },
            error: function(data) {

                // Some error in ajax call
                alert("Error while searching for a flight");
            }
        });
    });
});