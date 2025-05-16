 // Переключение видимости пароля
const toggleLoginPassword =  document.getElementById('toggleLoginPassword');
const toggleRegisterPassword =  document.getElementById('toggleRegisterPassword');

if(toggleLoginPassword){
 document.getElementById('toggleLoginPassword').addEventListener('click', function() {
    const passwordInput = document.getElementById('loginPassword');
    const icon = this.querySelector('i');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        icon.classList.remove('bi-eye');
        icon.classList.add('bi-eye-slash');
    } else {
        passwordInput.type = 'password';
        icon.classList.remove('bi-eye-slash');
        icon.classList.add('bi-eye');
    }
});
}

if(toggleRegisterPassword){
document.getElementById('toggleRegisterPassword').addEventListener('click', function() {
    const passwordInput = document.getElementById('registerPassword');
    const icon = this.querySelector('i');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        icon.classList.remove('bi-eye');
        icon.classList.add('bi-eye-slash');
    } else {
        passwordInput.type = 'password';
        icon.classList.remove('bi-eye-slash');
        icon.classList.add('bi-eye');
    }
});
}
     