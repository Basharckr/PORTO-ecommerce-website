
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
        url: 'change-offervalidity/' + id + '/',
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

//  ===========================================================================================
// ================================Add Coupon=================================================== -->

$().ready(function () {

    console.log('cou')
    $("#addcoupon").validate({
        rules: {
            couponcode: {
                required: true, minlength: 4, maxlength: 6
            },
            couponoffer: {
                required: true, max: 40
            }
        },
        messages: {
            couponcode: {
                required: "Enter Coupon code..",


            },
            couponoffer: {
                required: "Enter Coupon offer in price",
                max: "maximum coupon offer is 40"
            },
        },
        submitHandler: (addcoupon, e) => {

            e.preventDefault()
            $.ajax({
                url: "add-coupon",
                data: $("#addcoupon").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('add-coupon')
                    }
                    if (response == 'false') {
                        $("#error1").html("This Coupon already exist!!")
                    }
                },

            })
        }
    });
});

//  ===========================================================================================
// ================================Change coupon validity=================================================== -->
function couponValidity(id) {
    $.ajax({
        url: 'change-couponvalidity/' + id + '/',
        method: 'get',
        success: function (response) {
            if (response == 'true') {
                $("#valid" + id).removeClass("btn-success")
                $("#valid" + id).addClass("btn-danger")

            }
            if (response == 'false') {
                $("#valid" + id).removeClass("btn-danger")
                $("#valid" + id).addClass("btn-success")

            }
        }
    })
}
//  ===========================================================================================
//  ================================message-hide===================================================


var message_ele = document.getElementById("success1");
setTimeout(function () {
    message_ele.style.display = "none";
}, 3000);



//  ===========================================================================================
//  ================================message-hide===================================================


$("#valid" + id).addClass("btn-success")
var message_ele = document.getElementById("success1");
setTimeout(function () {
    message_ele.style.display = "none";
}, 3000);
