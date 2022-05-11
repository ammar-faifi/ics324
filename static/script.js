
$(() => {
  console.log("enter main script");
  // function will get executed
  // on click of submit button
  $("#source_city").on("change", function (ev) {
    var form = $("#search_flight_form");
    $.ajax({
      type: "POST",
      url: "/flight/get_cities",
      data: form.serialize(),
      success: function (data) {
        $("#dest_city").empty();
        $("#dest_city").append(new Option("Select a city", ""));

        data.map((el) => {
          console.log(el);
          $("#dest_city").append(new Option(el.city, el.code));
        });
      },
      error: function (data) {
        // Some error in ajax call
        alert("Error while searching for a flight");
      },
    });
  });

  // ----------

  $("#book_button").on("click", function (ev) {
    console.log("try to hide");
    ev.preventDefault();
    $("#choose_flight_form").hide();

    
  });
});