
//  ===========================================================================================
//  ================================Vendor-Signup===================================================

$().ready(function () {

    console.log('d')
    $("#vendorsignupform").validate({
        rules: {
            username: {
                required: true, minlength: 4
            },
            email: {
                required: true, email: true
            },
            password: {
                required: true, minlength: 5
            },
            cpassword: {
                required: true, minlength: 5, equalTo: '#password',
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
                        window.location.replace('/vendor/')
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
//  ================================ADD-product===================================================

$().ready(function () {

    console.log('d')
    $("#addproduct").validate({
        rules: {
            product_id: {
                required: true, minlength: 4
            },
            product_name: {
                required: true, minlength: 4
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
                required: true, minlength: 6
            },
            image1: {
                required: true,
            },
            image2: {
                required: true,
            },
            image3: {
                required: true,
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
            image1: {
                required: "Please upload the product image",
            },
            image2: {
                required: "Please upload the alternate product image",
            },
            image3: {
                required: "Please upload the alternate product image",
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
                required: true, minlength: 4
            },
            product_name: {
                required: true, minlength: 4
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
                required: true, minlength: 6
            },
            image1: {
                required: true,
            },
            image2: {
                required: true,
            },
            image3: {
                required: true,
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
            image1: {
                required: "Please upload the product image",
            },
            image2: {
                required: "Please upload the alternate product image",
            },
            image3: {
                required: "Please upload the alternate product image",
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

