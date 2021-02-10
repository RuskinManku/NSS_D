$(document).ready(function () {
    let firstName, lastName;
    console.log("Start");
    $("#almostDone").click(function() {
        $("#confirmationBox").hide();
        firstName = $("first_name").val();
        lastName = $("last_name").val();
    })

    const formData = {
        "firstName": firstName,
        "lastName": lastName
    };

    $.ajax({
        type: "POST",
        url: "placeholder",
        dataType: "json",
        data: {
            'formData': JSON.stringify(formData),
            id: $(this).val()
        },
        beforeSend : () => {},
        success: (result) => {
            console.log(JSON.stringify(result));
        },
        error: (result) => {
            console.log(JSON.stringify(result));
            alert('Server Error!');
        },
        complete: () => {
            console.log("Ajax request completed");
        }
    })
})