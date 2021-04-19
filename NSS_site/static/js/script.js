$("#submitbtn").click(function () {
    let firstName, lastName;
    console.log("Ajax request received");
    firstName = $("#first_name").val();
    lastName = $("#last_name").val();
    address = $("#address").val();
    contact = $("#contact").val();
    items = $("#items").val();
    const formData = {
        "firstName": firstName,
        "lastName": lastName,
        "address": address,
        "contact": contact,
        "items": items,
    };

    $.ajax({
        type: "POST",
        url: "/submitrequest/",
        dataType: "json",
        data: {
            'formData': JSON.stringify(formData),
            id: $(this).val()
        },
        beforeSend : () => {},
        success: (data, _textStatus) => {
            console.log("Sucess!!")
            console.log(data)
            window.location.href = data.redirect;
        },
        error: (result) => {
            // console.log(JSON.stringify(result));
            alert('Server Error!');
        },
        complete: () => {
            console.log("Ajax request completed");
        }
    })
})

$("#volunteer_submitbtn").click(function () {
    let firstName, lastName;
    console.log("Ajax request received (volunteer)");
    firstName = $("#first_name").val();
    lastName = $("#last_name").val();
    idno = $("#idno").val();
    contact = $("#contact").val();
    date = $("#pickdate").val();
    starttime = $("#starttime").val();
    endtime = $("#endtime").val();
    // date = $("#pickdate").val().toString();
    // starttime = $("#starttime").val().toString();
    // endtime = $("#endtime").val().toString();
    // calendly_link = $("#calendly_link").val();
    const formData = {
        "firstName": firstName,
        "lastName": lastName,
        "idno": idno,
        "contact": contact,
        "date": date,
        "starttime": starttime,
        "endtime": endtime,
    };
    console.log(formData);
    $.ajax({
        type: "POST",
        url: "/volunteer_submitrequest/",
        dataType: "json",
        data: {
            'formData': JSON.stringify(formData),
            id: $(this).val()
        },
        beforeSend : () => {},
        success: (data, _textStatus) => {
            alert(`Dear ${formData["firstName"]},\nYour slot details have been registered successfully.`)
            window.location.href = redirectSite;
        },
        error: (result) => {
            // console.log(JSON.stringify(result));
            alert('Server Error!');
        },
        complete: () => {
            console.log("Ajax request completed");
        }
    })
})