
var input = document.querySelector('.mail__form--pass-ip')
var eye = document.querySelector('.eye')



eye.addEventListener("click", function () {
    const type = input.getAttribute("type")

    type === "password" ? "text" : "password";
    input.setAttribute("type", type);

    this.classList.toggle("fa-eye");
});