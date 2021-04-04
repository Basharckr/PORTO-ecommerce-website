//  ===========================================================================================
//  ================================Vendor-Signup===================================================

$().ready(function () {

    console.log('d')
    $("#vendorsignupform").validate({
        rules: {
            username: {
                required: true,
                minlength: 4
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
            username: {
                required: "Please enter your username",
                minlength: "Your username must consist of at least 4 characters"
            },
            email: {
                required: "Please enter your company email",
            },
            number: {
                required: "Enter your phone number"
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
        submitHandler: (vendorsignupform, e) => {

            e.preventDefault()
            $.ajax({
                url: "signup",
                data: $("#vendorsignupform").serialize(),
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
                        $("#error1").html("This phone number already taken!!!!")
                    }
                },

            })
        }
    });
});


//  ===========================================================================================
//  ================================Vendor-Login===================================================

$().ready(function () {

    console.log('d')
    $("#vendorloginform").validate({
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
        submitHandler: (vendorloginform, e) => {

            e.preventDefault()
            $.ajax({
                url: "login",
                data: $("#vendorloginform").serialize(),
                method: "post",

                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('/vendor')
                    }
                    if (response == 'false') {
                        $("#block").html('<div class="alert alert-info text-center" id="block"><strong>Incorrect password!!</strong> </div>')

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
//  ================================ADD-product===================================================

$().ready(function () {

    console.log('d')
    $("#addproduct").validate({
        rules: {
            product_id: {
                required: true,
                minlength: 4
            },
            product_name: {
                required: true,
                minlength: 4
            },
            product_categorie: {
                required: true,
            },
            product_price: {
                required: true,
            },
            quantity: {
                required: true,
            },
            product_weight: {
                required: true,
            },
            product_description: {
                required: true,
                minlength: 6
            },
            thumbnail: {
                required: true,
                extension: "jpg|jpeg|png"
            },
            thumbnail2: {
                required: true,
                extension: "jpg|jpeg|png"
            },
            thumbnail3: {
                required: true,
                extension: "jpg|jpeg|png"
            },
        },
        messages: {
            product_id: {
                required: "Please enter Product id",
                minlength: "Product ID should be minimum 4 digit number"
            },
            product_name: {
                required: "Please enter Product name",
            },
            product_categorie: {
                required: "Please select any category",
            },
            product_price: {
                required: "Please Enter product price",
            },

            quantity: {
                required: "Please Enter the available quantity",
            },
            product_weight: {
                required: "Please enter the product weight",
            },
            product_description: {
                required: "Please enter the product description",
                minlength: "Product description should be minimum 6 character"

            },
            thumbnail: {
                required: "Please upload the product image",
                extension: "Only accept jpg/jpeg/png formats!!"
            },
            thumbnail2: {
                required: "Required",
                extension: "Only accept jpg/jpeg/png formats!!"
            },
            thumbnail3: {
                required: "Required",
                extension: "Only accept jpg/jpeg/png formats!!"
            },
        },

        // submitHandler: (addproduct, e) => {

        //     e.preventDefault()
        //     $.ajax({
        //         url: "add-product",
        //         data: $("#addproduct").serialize(),
        //         method: "post",


        //         success: function (response) {
        //             if (response == 'true') {
        //                 window.location.replace('add-product')
        //                 $("#success1").html("The product success fully added")
        //             }
        //             if (response == 'false1') {
        //                 $("#error1").html(" This product ID already taken!!!!")
        //             }
        //             if (response == 'false2') {
        //                 $("#error1").html(" This product name already taken!!!!")
        //             }
        //         },

        //     })
        // }
    });
});

//  ===========================================================================================
//  ================================Product name checking===================================================
$(document).ready(function () {
    // catch the form's submit event

    $('#product_name').on("change", function () {
        // create an AJAX call
        $.ajax({
            data: $(this).serialize(), // get the form data
            url: "check-product-name",
            // on success
            success: function (response) {
                if (response.is_taken == true) {
                    $('#product_name').removeClass('is-valid').addClass('is-invalid');
                    $('#product_name').after('<div class="invalid-feedback d-block" id="productnameError">This Product name available!</div>')
                } else {
                    $('#product_name').removeClass('is-invalid').addClass('is-valid');
                    $('#productnameError').remove();

                }

            },
            // on error
            error: function (response) {
                // alert the error if any error occured
                console.log(response.responseJSON.errors)
            }
        });

        return false;
    });
})

//  ===========================================================================================
//  ================================Product ID checking===================================================

$(document).ready(function () {
    // catch the form's submit event
    $('#productidError').remove();
    $('#product_id').on("change", function () {
        // create an AJAX call
        $.ajax({
            data: $(this).serialize(), // get the form data
            url: "check-product-id",
            // on success
            success: function (response) {
                if (response.is_taken == true) {
                    $('#product_id').removeClass('is-valid').addClass('is-invalid');
                    $('#product_id').after('<div class="invalid-feedback d-block" id="productidError">This Product ID available!</div>')
                } else {
                    $('#product_id').removeClass('is-invalid').addClass('is-valid');
                    $('#productidError').remove();

                }

            },
            // on error
            error: function (response) {
                // alert the error if any error occured
                console.log(response.responseJSON.errors)
            }
        });

        return false;
    });
})


//  ===========================================================================================
//  ================================message-hide===================================================


var message_ele = document.getElementById("success1");
setTimeout(function () {
    message_ele.style.display = "none";
}, 3000);


//  ===========================================================================================
//  ================================Edit-Product===================================================

$().ready(function () {

    console.log('d')
    $("#editproduct").validate({
        rules: {
            product_id: {
                required: true,
                minlength: 4
            },
            product_name: {
                required: true,
                minlength: 4
            },
            product_categorie: {
                required: true,
            },
            product_price: {
                required: true,
            },
            quantity: {
                required: true,
            },
            product_weight: {
                required: true,
            },
            product_description: {
                required: true,
                minlength: 6
            },
            thumbnail: {
                required: true,
                extension: "jpg|jpeg|png"

            },
            thumbnail2: {
                required: true,
                extension: "jpg|jpeg|png"

            },
            thumbnail3: {
                required: true,
                extension: "jpg|jpeg|png"

            },
        },
        messages: {
            product_id: {
                required: "Please enter Product id",
                minlength: "Product ID should be minimum 4 digit number"
            },
            product_name: {
                required: "Please enter Product name",
            },
            product_categorie: {
                required: "Please select any category",
            },
            product_price: {
                required: "Please Enter product price",
            },

            quantity: {
                required: "Please Enter the available quantity",
            },
            product_weight: {
                required: "Please enter the product weight",
            },
            product_description: {
                required: "Please enter the product description",
                minlength: "Product description should be minimum 6 character"

            },
            thumbnail: {
                required: "Please upload the product image",
                extension: "Only accept jpg/jpeg/png formats!!"

            },
            thumbnail2: {
                required: "Please upload the alternate product image",
                extension: "Only accept jpg/jpeg/png formats!!"
            },
            thumbnail3: {
                required: "Please upload the alternate product image",
                extension: "Only accept jpg/jpeg/png formats!!"
            },
        },
        // submitHandler: (addproduct, e) => {

        //     e.preventDefault()
        //     $.ajax({
        //         url: "add-product",
        //         data: $("#addproduct").serialize(),
        //         method: "post",


        //         success: function (response) {
        //             if (response == 'true') {
        //                 window.location.replace('add-product')
        //                 $("#success1").html("The product success fully added")
        //             }
        //             if (response == 'false1') {
        //                 $("#error1").html(" This product ID already taken!!!!")
        //             }
        //             if (response == 'false2') {
        //                 $("#error1").html(" This product name already taken!!!!")
        //             }
        //         },

        //     })
        // }
    });
});


//  ===========================================================================================
//  ================================ship-status===================================================

function shipStatus(id) {
    $.ajax({
        url: 'change-ship-status/' + id + '/',
        method: 'get',
        success: function (response) {
            if (response == 'shipped') {
                window.location.replace('vendor-orders')
            }
            if (response == 'ship') {

                window.location.replace('vendor-orders')
            }
        }
    })
}


// Start upload preview image
$(".gambar").attr("src", "https://user.gadjian.com/static/images/personnel_boy.png");
var $uploadCrop,
    tempFilename,
    rawImg,
    imageId;

function readFile(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('.upload-demo').addClass('ready');
            $('#cropImagePop').modal('show');
            rawImg = e.target.result;

        }
        reader.readAsDataURL(input.files[0]);

    } else {
        swal("Sorry - you're browser doesn't support the FileReader API");
    }
}


//  ===========================================================================================
//  ================================Report customers===================================================

function reportCustomers(id) {
    console.log(id)
    var txt = $("#txtArea-" + id).val();
    var a = $('[name=csrfmiddlewaretoken]').first().val()
    console.log(a)
    var data = {
        'csrfmiddlewaretoken': a,
        'message': txt
    }
    console.log("txtArea-" + id)
    console.log(txt)
    $.ajax({
        url: 'report-customer/' + id + '/',
        method: 'post',
        data: data,
        success: function (response) {
            if (response == 'true') {

                alert("Reportted successfully")
            }
        }
    })
}

