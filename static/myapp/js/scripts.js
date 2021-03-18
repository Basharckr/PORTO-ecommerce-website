
//  ===========================================================================================
//  ================================User-Signup===================================================

$().ready(function (){
    
    console.log('d')
    $("#signupform").validate({
        rules:{
            firstname:{
                required:true, minlength: 3
            },
            lastname:{
                required:true, minlength: 1
            },
            username:{
                required:true, minlength: 5
            },
            email:{
                required:true, email:true
            },
            password:{
                required:true, minlength: 5
            },
            cpassword:{
                required:true, minlength: 5, equalTo:'#password',
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
                data:$("#signupform").serialize(),
                method: "post",
        
                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('login')
                    }
                    if(response == 'false1'){
                        $("#error1").html(" Username already taken!!!!")
                    }
                    if(response == 'false2'){
                        $("#error1").html(" Email already taken!!!!")
                    }
                },

            })
        }
    });
});


//  ===========================================================================================
//  ================================User-Login===================================================

$().ready(function (){
    
    console.log('d')
    $("#loginform").validate({
        rules:{
            username:{
                required:true
            },
            password:{
                required:true
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
                data:$("#loginform").serialize(),
                method: "post",
        
                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('landing')
                    }
                    if(response == 'false'){
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
//  ================================Add to cart===================================================

function addToCart(id){
    let qty = $('#quantity').val()
    data={
        'count': qty,     
    }
    $.ajax({
        url: '/add-to-cart/'+id+'/',
        data: data,
        method: 'post',
        success: function(response){
            if(response == 'true'){
                window.location.replace('/cart')
            }
            if(response == 'nothing'){
                window.location.replace('/')
            }
        }
    })
}

//  ===========================================================================================
//  ================================remove product from cart===================================================
function removeProduct(id){
    
    data = {
        
    }
    $.ajax({
        url:'/remove-from-cart/'+id+'/',
        data:data,
        method:'get',
        success: function(response){
        if(response == 'true'){
            window.location.replace('/cart')
        }

    }
    })
}

//  ===========================================================================================
//  ================================Edit product Quantity===================================================
function editQuantity(id,cou){
    console.log(id)
    var newquantity = $('#newquantity-'+cou).val()
    data = {
        'quantity' : newquantity,
    }
    $.ajax({
        url:'/edit-quantity/'+id+'/',
        data: data,
        method: 'post',
        success: function(response){
            if(response == 'true'){
                window.location.replace('/cart')
            }
            if(response == 'nothing'){
                console.log('no change in quantity')
            }
        }
    })
}


//  ===========================================================================================
//  ================================Shipping address===================================================
$().ready(function (){
    
    console.log('d')
    $("#shippaddress").validate({
        rules:{
            firstname:{
                required:true, minlength: 3
            },
            lastname:{
                required:true, minlength: 1
            },
            street:{
                required:true, minlength: 3
            },
            city:{
                required:true, minlength: 3
            },
            state:{
                required:true, minlength: 3
            },
            pincode:{
                required:true, minlength: 6
            },
            number:{
                required:true, minlength: 10, maxlength: 12
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
                data:$("#shippaddress").serialize(),
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
//  ===========================================================================================
//  ================================Edit address===================================================