document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('.form-signin');

    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {            event.preventDefault(); 
            const emailInput = document.getElementById('inputEmail');
            const passwordInput = document.getElementById('inputPassword');

            const email = emailInput.value;
            const password = passwordInput.value;

            const adminEmail = 'admin@gmail.com';
            const adminPassword = 'admin123';

            if (email === adminEmail && password === adminPassword) {
                localStorage.setItem('loggedInUser', 'Admin');
                alert('¡Bienvenido, Admin!');
                window.location.href = 'index.html'; 
            } else {
                alert('Email o contraseña incorrectos. Por favor, inténtalo de nuevo.');
            }
        });
    }
});