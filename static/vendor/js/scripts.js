
//  ===========================================================================================
//  ================================Vendor-Signup===================================================

$().ready(function (){
    
    console.log('d')
    $("#vendorsignupform").validate({
        rules:{
            username:{
                required:true, minlength: 4
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
                data:$("#vendorsignupform").serialize(),
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
//  ================================Vendor-Login===================================================

$().ready(function (){
    
    console.log('d')
    $("#vendorloginform").validate({
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
        submitHandler: (vendorloginform, e) => {
            
            e.preventDefault()
            $.ajax({
                url: "login",
                data:$("#vendorloginform").serialize(),
                method: "post",
        
                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('/vendor/')
                    }
                    if(response == 'false'){
                        $("#error1").html(" Incorrect username OR password")
                    }
                },

            })
        }
    });
});
