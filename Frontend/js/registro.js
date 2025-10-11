document.addEventListener('DOMContentLoaded', () => {
    const registroForm = document.getElementById('registroForm');

    if (registroForm) {
        registroForm.addEventListener('submit', (event) => {            event.preventDefault(); 
            const nombreInput = document.getElementById('nombre');
            const passwordInput = document.getElementById('password');
            const confirmPasswordInput = document.getElementById('confirmPassword');

            const username = nombreInput.value.trim();
            const password = passwordInput.value;
            const confirmPassword = confirmPasswordInput.value;

            if (password !== confirmPassword) {
                alert('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.');
                return; 
            }

            if (username) {
                localStorage.setItem('loggedInUser', username);

                alert(`¡Bienvenido, ${username}! Tu cuenta ha sido creada.`);
                window.location.href = 'index.html';
            }
        });
    }
});