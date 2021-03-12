
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
                        $("#error1").html(" Incorrect username OR password")
                    }
                },

            })
        }
    });
});
