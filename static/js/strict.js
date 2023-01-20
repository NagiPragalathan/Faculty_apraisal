(function () {
    'use strict'
    
    var form = document.querySelectorAll("#inputs")

    Array.prototype.slice.call(form).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if(!form.checkValidity()) {
                event.preventDefault()
                event.stopPropogation()
            }

            form.classList.add('was-validated')
        }, false)
    })

})()