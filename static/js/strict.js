(function () {
    'use strict'
    
    var form = document.querySelectorAll("#inputs")
    var label = document.querySelector(".append")
    var input = document.querySelector(".mail__form--user__ip")

    Array.prototype.slice.call(form).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if(!form.checkValidity()) {
                event.preventDefault()
                event.stopPropogation()
            }
            
            label.value += input.innerHTML

            form.classList.add('was-validated')
        }, false)
    })

})()