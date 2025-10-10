document.addEventListener('DOMContentLoaded', () => {
    const profileText = document.getElementById('profile-text');
    const profileLink = document.getElementById('profile-link');

    // Simulación: Suponemos que el nombre de usuario se guarda en localStorage al iniciar sesión.
    const loggedInUser = localStorage.getItem('loggedInUser');

    if (loggedInUser && profileText) {
        profileText.textContent = loggedInUser;
        // Cambiamos el enlace para que vaya a la página principal en lugar de al registro.
        if (profileLink) profileLink.href = 'index.html';
    }
});