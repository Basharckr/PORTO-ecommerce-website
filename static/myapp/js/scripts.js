//  ===========================================================================================
//  ================================User-Signup===================================================

$().ready(function () {

    console.log('d')
    $("#signupform").validate({
        rules: {
            firstname: {
                required: true,
                minlength: 3
            },
            lastname: {
                required: true,
                minlength: 1
            },
            username: {
                required: true,
                minlength: 5
            },
            email: {
                required: true,
                email: true
            },
            number: {
                required: true,
                minlength: 10,
                maxlength: 10
            },
            password: {
                required: true,
                minlength: 5
            },
            cpassword: {
                required: true,
                minlength: 5,
                equalTo: '#password',
            },
        },
        messages: {
            firstname: "Please enter your first name",
            lastname: "Please enter your last name",
            username: {
                required: "Please enter your username",
                minlength: "Your username must consist of at least 5 characters"
            },
            email: {
                required: "Please enter your email",
            },
            number: {
                required: "Please enter your Mobile number",
            },
            password: {
                required: "Please enter your password",
                minlength: "Your password must consist of at least 5 characters"
            },
            cpassword: {
                required: "Please enter your password",
                minlength: "Your password must consist of at least 5 characters",
                equalTo: "Please enter same password as above"
            },
        },
        submitHandler: (signupform, e) => {

            e.preventDefault()
            $.ajax({
                url: "signup",
                data: $("#signupform").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('login')
                    }
                    if (response == 'false1') {
                        $("#error1").html(" Username already taken!!!!")
                    }
                    if (response == 'false2') {
                        $("#error1").html(" Email already taken!!!!")
                    }
                    if (response == 'false3') {
                        $("#error1").html(" Mobile number already taken!!!!")
                    }
                },

            })
        }
    });
});


//  ===========================================================================================
//  ================================User-Login===================================================

$().ready(function () {

    console.log('d')
    $("#loginform").validate({
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
        submitHandler: (loginform, e) => {

            e.preventDefault()
            $.ajax({
                url: "login",
                data: $("#loginform").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('landing')
                    }
                    if (response == 'false') {
                        $("#block").html('<div class="alert alert-warning text-center" id="block">Incorrect<strong>Password</strong> </div>')

                    }
                    if (response == 'blocked') {
                        $("#block").html('<div class="alert alert-danger text-center" id="block">Sorry!! <strong>You are Blocked!!</strong> </div>')

                    }
                    if (response == 'nouser') {
                        $("#block").html('<div class="alert alert-warning text-center" id="block">Sorry!!This mobile number not exist!! <strong>You dont have an account..? Please SignUp!!</strong> </div>')

                    }
                },

            })
        }
    });
});

//  ===========================================================================================
//  ================================User-otp-Login===================================================

$().ready(function () {

    console.log('hi')
    $("#otplogin").validate({
        rules: {
            number: {
                required: true,
                minlength: 10,
                maxlength: 10
            },

        },
        messages: {
            number: {
                required: "Please enter your registered mobile number",
                minlength: "Number must be 10 digits"
            },


        },
        submitHandler: (otplogin, e) => {

            e.preventDefault()
            $.ajax({
                url: "otp-login",
                data: $("#otplogin").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('/enter-otp')
                    }
                    if (response == 'blocked') {
                        $("#block").html('<div class="alert alert-danger text-center" id="block">Sorry!! <strong>You are Blocked!!</strong> </div>')

                    }
                    if (response == 'nouser') {
                        $("#block").html('<div class="alert alert-warning text-center" id="block">Sorry!!This username not exist!! <strong>You dont have an account..? Please SignUp!!</strong> </div>')

                    }
                },

            })
        }
    });
});
//  ===========================================================================================
//  ================================User-Enter-otp===================================================

$().ready(function () {

    console.log('d')
    $("#enterotp").validate({
        rules: {
            otp: {
                required: true
            },
        },
        messages: {
            otp: {
                required: "Please enter otp",
            },
        },
        submitHandler: (enterotp, e) => {

            e.preventDefault()
            $.ajax({
                url: "enter-otp",
                data: $("#enterotp").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('landing')
                    }
                    if (response == 'false') {
                        $("#block").html('<div class="alert alert-warning text-center" id="block">Invalid OTP!!</div>')
                    }

                },

            })
        }
    });
});


//  ===========================================================================================
//  ================================Add to cart===================================================

function addToCart(id) {
    let qty = $('#quantity').val()
    data = {
        'count': qty,
    }
    $.ajax({
        url: '/add-to-cart/' + id + '/',
        data: data,
        method: 'post',
        success: function (response) {
            if (response == 'true') {
                window.location.replace('/')
            }
            if (response == 'nothing') {
                window.location.replace('/')
            }
        }
    })
}

//  ===========================================================================================
//  ================================remove product from cart===================================================
function removeProduct(id) {

    data = {

    }
    $.ajax({
        url: '/remove-from-cart/' + id + '/',
        data: data,
        method: 'get',
        success: function (response) {
            if (response == 'true') {
                window.location.replace('/cart')
            }

        }
    })
}

//  ===========================================================================================
//  ================================Edit product Quantity===================================================
function editQuantity(id, cou) {
    console.log(id)
    var newquantity = $('#newquantity-' + cou).val()
    data = {
        'quantity': newquantity,
    }
    $.ajax({
        url: '/edit-quantity/' + id + '/',
        data: data,
        method: 'post',
        success: function (response) {
            if (response == 'true') {
                window.location.replace('/cart')
            }
            if (response == 'nothing') {
                console.log('no change in quantity')
            }
        }
    })
};



//  ===========================================================================================
//  ================================Shipping address===================================================
$(document).ready(function () {

    $("#shippaddress").validate({
        rules: {
            firstname: {
                required: true,
                minlength: 3
            },
            lastname: {
                required: true,
                minlength: 1
            },
            street: {
                required: true,
                minlength: 3
            },
            city: {
                required: true,
                minlength: 3
            },
            state: {
                required: true,
                minlength: 3
            },
            pincode: {
                required: true,
                minlength: 6
            },
            number: {
                required: true,
                minlength: 10,
                maxlength: 12
            },
        },
        messages: {
            firstname: "Please enter your first name",
            lastname: "Please enter your last name",
            street: "Please enter your street name",
            city: "Please enter your city",
            state: "Please enter your state",
            pincode: {
                required: "Please enter your postal code",
                minlength: "Must have 6 digit"
            },
            number: {
                required: "Please enter your mobile number",
                minlength: "Must have 10 digit"
            },

        },
        submitHandler: (shippaddress, e) => {

            e.preventDefault()
            $.ajax({
                url: "add-address",
                data: $("#shippaddress").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('checkout')
                    }
                    if (response == 'false') {
                        window.location.replace('checkout')
                    }

                },

            })
        }
    });
});

$(document).ready(function () {


    $("#editaddress").validate({
        rules: {
            firstname1: {
                required: true,
                minlength: 3
            },
            lastname1: {
                required: true,
                minlength: 1
            },
            street1: {
                required: true,
                minlength: 3
            },
            city1: {
                required: true,
                minlength: 3
            },
            state1: {
                required: true,
                minlength: 3
            },
            pincode1: {
                required: true,
                minlength: 6
            },
            number1: {
                required: true,
                minlength: 10,
                maxlength: 12
            },
        },
        messages: {
            firstname1: "Please enter your first name",
            lastname1: "Please enter your last name",
            street1: "Please enter your street name",
            city1: "Please enter your city",
            state1: "Please enter your state",
            pincode1: {
                required: "Please enter your postal code",
                minlength: "Must have 6 digit"
            },
            number1: {
                required: "Please enter your mobile number",
                minlength: "Must have 10 digit"
            },

        },
        submitHandler: (editaddress, e) => {

            e.preventDefault()
            console.log($("#editaddress").data("id"));
        }
    });
});

//  ===========================================================================================
//  ================================Shipping here===================================================
function shipHere(id) {
    $.ajax({
        url: "/set-address/" + id + "/",
        method: 'post',
        success: function (response) {
            if (response == 'true') {
                $("div").removeClass("active");
                var element = document.getElementById("set-add-" + id);
                element.classList.add("active");
                document.getElementById('show').style.display = "block";
            }
        }

    })
}


//  ===========================================================================================
//  ================================Edi user account===================================================

$().ready(function () {

    console.log('d')
    $("#editaccount").validate({
        rules: {
            firstname: {
                required: true,
                minlength: 3
            },
            lastname: {
                required: true,
                minlength: 1
            },
            username: {
                required: true,
                minlength: 5
            },
            email: {
                required: true,
                email: true
            },
            number: {
                required: true,
                minlength: 10,
                maxlength: 12
            },
            image1: {
                extension: "jpg|jpeg|png"
            },
            orginalpassword: {
                required: true
            },
        },
        messages: {
            firstname: "Please enter your first name",
            lastname: "Please enter your last name",
            username: {
                required: "Please enter your username",
                minlength: "Your username must consist of at least 5 characters"
            },
            email: {
                required: "Please enter your email",
            },
            number: {
                required: "Please enter your Mobile number",
                minlength: "At least 10 digit required",
                maxlength: "At most 12 digit",

            },
            image1: {
                extension: "Only accept jpg/jpeg/png formats!!"
            },
        },
    });
});

//  ===========================================================================================
//  ================================Change user password===================================================

$().ready(function () {

    $("#changuserpassword").validate({
        rules: {
            orginalpassword: {
                required: true
            },
            password: {
                required: true,
                minlength: 5
            },
            cpassword: {
                required: true,
                minlength: 5,
                equalTo: '#password',
            },
        },
        messages: {
            password: {
                required: "Please enter your password",
                minlength: "Your password must consist of at least 5 characters"
            },
            cpassword: {
                required: "Please enter your password",
                minlength: "Your password must consist of at least 5 characters",
                equalTo: "Please enter same password as above"
            },
        },
        submitHandler: (changuserpassword, e) => {

            e.preventDefault()
            $.ajax({
                url: "change-user-password",
                data: $("#changuserpassword").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        $("#block").html('<div class="alert alert-success text-center" id="block"><strong>Password changed successfully.</strong> </div>')
                    }
                    if (response == 'false') {
                        $("#block").html('<div class="alert alert-danger text-center" id="block"><strong>Old password is incorrect..!!</strong> </div>')
                    }

                },

            })
        }
    });
});

//  ===========================================================================================
//  ================================Cancel order===================================================
function cancelOrder(id) {
    data = {

    }
    $.ajax({
        url: '/cancel-order/' + id + '/',
        data: data,
        method: 'get',
        success: function (response) {
            if (response == 'true') {
                window.location.replace('/my-orders')
            }

        }
    })
}


//  ===========================================================================================
//  ================================Apply coupon===================================================
$().ready(function () {
    console.log('hiiiiiiiiiiiiii')
    $("#applycoupon1").validate({
        rules: {
            coupon_code: {
                required: true
            }
        },
        messages: {
            coupon_code: {
                required: "Please enter your coupon code",
            }
        },
        submitHandler: (applycoupon1, e) => {

            e.preventDefault()
            $.ajax({
                url: "cart",
                data: $("#applycoupon1").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('cart')
                        $("#cmsg").html('<span id="success1">Valid Coupon..Discount added to total amount</span>')
                    }
                    if (response == 'false') {
                        $("#cmsg").html('<span id="fail">Invalid coupon..Try again..</span>')

                    }

                },

            })
        }
    });
});


//  ===========================================================================================
//  ================================message-hide===================================================


var message_ele = document.getElementById("fail");
setTimeout(function () {
    message_ele.style.display = "none";
}, 3000);
