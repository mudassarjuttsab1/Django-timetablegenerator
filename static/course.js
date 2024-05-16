
console.log("javascript is running")
$("#id_department").change(function () {
    console.log("js is running")
    var url = $("#courseForm").attr("data-teachers-url");  // get the url of the `load_cities` view
    var departmentId = $(this).val();  // get the selected country ID from the HTML input
    console.log(departmentId)
    $.ajax({                       // initialize an AJAX request
      url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      data: {
        'department': departmentId       // add the country id to the GET parameters
      },
      success: function (data) {   // `data` is the return of the `load_cities` view function
        $("#id_teacher").html(data);  // replace the contents of the city input with the data that came from the server
      }
    });

  });