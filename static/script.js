$(() => {
  // function will get executed
  // on click of submit button
  $("#source_city").on("change", function (ev) {
    var form = $("#search_flight_form");
    $.ajax({
      type: "POST",
      url: "/flight/get_cities",
      data: form.serialize(),
      success: function (data) {
        console.log(data);
        $("#dest_city").removeAttr("disabled");
        let a = [
          ["a", "b"],
          ["as", "fd"],
        ];
        a.map((data) => {
          $("#dest_city").append(new Option(data[0], data[1]));
        });
      },
      error: function (data) {
        // Some error in ajax call
        alert("Error while searching for a flight");
      },
    });
  });
});
