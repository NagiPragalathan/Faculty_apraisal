
// $('.eye').on('click', (){
//     $(this).toggleClass('fa-eye').toggleClass('fa-eye-slash');

//     $('.mail__form--pass-ip').togglePassword();
// })

    
function toggle() {

    var input = document.querySelector('.mail__form--pass-ip')
    var eye = document.querySelector('.eye')

    if(input.type === "password"){

        input.type = "text"; 
        eye.classList.toggle("fa-eye");

    }
    else {
        input.type = "password";
        eye.classList.toggle("fa-eye-slash");
    }

}