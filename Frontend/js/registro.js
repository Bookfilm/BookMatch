document.addEventListener('DOMContentLoaded', () => {
    const registroForm = document.getElementById('registroForm');

    if (registroForm) {
        registroForm.addEventListener('submit', (event) => {
            event.preventDefault(); // Evitamos que el formulario se envíe y la página se recargue.

            // Obtenemos los valores de los campos del formulario
            const nombreInput = document.getElementById('nombre');
            const passwordInput = document.getElementById('password');
            const confirmPasswordInput = document.getElementById('confirmPassword');

            const username = nombreInput.value.trim();
            const password = passwordInput.value;
            const confirmPassword = confirmPasswordInput.value;

            // Validamos que las contraseñas coincidan
            if (password !== confirmPassword) {
                alert('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.');
                return; // Detenemos la ejecución si no coinciden
            }

            if (username) {
                // Guardamos el nombre de usuario en localStorage para usarlo en otras páginas
                localStorage.setItem('loggedInUser', username);

                alert(`¡Bienvenido, ${username}! Tu cuenta ha sido creada.`);

                // Redirigimos al usuario a la página principal
                window.location.href = 'index.html';
            }
        });
    }
});