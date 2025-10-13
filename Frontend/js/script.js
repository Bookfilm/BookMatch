// Botón Hamburguer

document.addEventListener('DOMContentLoaded', () => {
  const hamburgerBtn = document.getElementById('hamburger-btn');
  const sidebar = document.getElementById('sidebar-menu');
  const body = document.body;

  if (!hamburgerBtn || !sidebar) {
    console.error("No se encontraron los elementos del menú (hamburger o sidebar).");
    return;
  }

  const toggleMenu = () => {
    const isOpen = sidebar.classList.toggle('open');
    hamburgerBtn.classList.toggle('open', isOpen);
    hamburgerBtn.setAttribute('aria-expanded', isOpen);
    body.classList.toggle('menu-open', isOpen);
  };

  hamburgerBtn.addEventListener('click', toggleMenu);

  document.addEventListener('click', (e) => {
    if (sidebar.classList.contains('open') && !sidebar.contains(e.target) && !hamburgerBtn.contains(e.target)) {
      toggleMenu();
    }
  });
});

// Nombre de perfil en el sidebar

document.addEventListener('DOMContentLoaded', () => {
    const profileText = document.getElementById('profile-text');
    const profileLink = document.getElementById('profile-link');
    const loggedInUser = localStorage.getItem('loggedInUser');

    if (loggedInUser && profileText) {
        profileText.textContent = loggedInUser;
        if (profileLink) profileLink.href = 'index.html';
    }
});

// Registro de user

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

// login hardcodeado

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