
//  ===========================================================================================
 // ================================Admin-Login=================================================== -->

$().ready(function (){
    
    console.log('d')
    $("#ownerloginform").validate({
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
        submitHandler: (ownerloginform, e) => {
            
            e.preventDefault()
            $.ajax({
                url: "login",
                data:$("#ownerloginform").serialize(),
                method: "post",
        
                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('/owner')
                    }
                    if(response == 'false'){
                        $("#error1").html(" Incorrect username OR password")
                    }
                },

            })
        }
    });
});

//  ===========================================================================================
 // ================================Add category=================================================== -->

 $().ready(function (){
    
    console.log('d')
    $("#addcategory").validate({
        rules:{
            category:{
                required:true, minlength:3
             
            },
        },
        messages: {
            category: {
                required: "Enter category name..",
                minlength: "Category name should be 3 charecter"
            },
        },
        submitHandler: (addcategory, e) => {
            
            e.preventDefault()
            $.ajax({
                url: "create-category",
                data:$("#addcategory").serialize(),
                method: "post",
        
                success: function (response) {
                    if (response == 'true') {
                        window.location.replace('create-category')
                    }
                    if(response == 'false'){
                        $("#error1").html("This Category already added!!")
                    }
                },

            })
        }
    });
});
