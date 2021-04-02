
//  ===========================================================================================
// ================================Admin-Login=================================================== -->

$().ready(function () {

    console.log('d')
    $("#ownerloginform").validate({
        rules: {
            username: {
                required: true
            },
            password: {
                required: true
            },
        },
        messages: {
            username: {
                required: "Please enter your username",
            },
            password: {
                required: "Please enter your password",
            },

        },
        submitHandler: (ownerloginform, e) => {

            e.preventDefault()
            $.ajax({
                url: "login",
                data: $("#ownerloginform").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('/owner')
                    }
                    if (response == 'false') {
                        $("#error1").html(" Incorrect username OR password")
                    }
                },

            })
        }
    });
});

//  ===========================================================================================
// ================================Add category=================================================== -->

$().ready(function () {

    console.log('d')
    $("#addcategory").validate({
        rules: {
            category: {
                required: true, minlength: 3
            },
            offer: {
                required: true
            }
        },
        messages: {
            category: {
                required: "Enter category name..",
                minlength: "Category name should be 3 charecter"
            },
            offer: {
                required: "Enter category offer in percentage..",
            },
        },
        submitHandler: (addcategory, e) => {

            e.preventDefault()
            $.ajax({
                url: "create-category",
                data: $("#addcategory").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('create-category')
                    }
                    if (response == 'false') {
                        $("#error1").html("This Category already added!!")
                    }
                },

            })
        }
    });
});

//  ===========================================================================================
// ================================Change offer validity=================================================== -->
function changeValidity(id) {
    $.ajax({
        url: 'change-offervality/' + id + '/',
        method: 'get',
        success: function (response) {
            if (response == 'true') {
                $("#valid" + id).removeClass("btn-danger")
                $("#valid" + id).addClass("btn-success")
            }
            if (response == 'false') {
                $("#valid" + id).removeClass("btn-success")
                $("#valid" + id).addClass("btn-danger")
            }
        }
    })
}