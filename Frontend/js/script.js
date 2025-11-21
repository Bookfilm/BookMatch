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
        if (profileLink) profileLink.href = 'perfil.html';
    }
});

// Registro de usuario

document.addEventListener('DOMContentLoaded', () => {
    const registroForm = document.getElementById('registroForm');

    if (registroForm) {
        registroForm.addEventListener('submit', (event) => { event.preventDefault(); 
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

// Lógica de la página de Perfil
document.addEventListener('DOMContentLoaded', () => {
    const profileInfoDiv = document.getElementById('profile-info');
    const logoutBtn = document.getElementById('logout-btn');
    const loggedInUser = localStorage.getItem('loggedInUser');
    if (profileInfoDiv && logoutBtn) {
        if (loggedInUser) {
            profileInfoDiv.innerHTML = `
                <p style="font-size: 1.1rem;"><strong>Nombre de Usuario:</strong> ${loggedInUser}</p>
                <p style="font-size: 1.1rem;"><strong>Estado:</strong> Conectado</p>
            `;

            logoutBtn.addEventListener('click', () => {
                localStorage.removeItem('loggedInUser');
                alert('Has cerrado sesión.');
                window.location.href = 'index.html';
            });
        } else {
            alert('No has iniciado sesión.');
            window.location.href = 'login.html'; 
        }
    }
});

// login hardcodeado

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('.form-container');

    if (loginForm) {
        loginForm.addEventListener('submit', (event) => {            event.preventDefault(); 
            const emailInput = document.getElementById('email');
            const passwordInput = document.getElementById('password');

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

// Formulario de Contacto con EmailJS

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contact-form');

    if (contactForm) {
        const serviceID = 'service_myft9xe';
        const templateID = 'template_a4jodpi';
        const publicKey = 'CztM52XuoUpJieW4H';

        emailjs.init({ publicKey });

        contactForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const submitButton = this.querySelector('.enviar-button');
            const formMessage = document.getElementById('form-message');

            submitButton.textContent = 'Enviando...';
            submitButton.disabled = true;
            formMessage.textContent = '';
            const templateParams = {
                asunto: this.asunto.value,
                nombre: this.nombre.value,
                email: this.email.value,
                mensaje: this.mensaje.value,
            };

            emailjs.send(serviceID, templateID, templateParams)
                .then(() => {
                    submitButton.textContent = 'Enviar Mensaje';
                    submitButton.disabled = false;
                    formMessage.textContent = '¡Mensaje enviado con éxito!';
                    formMessage.style.color = 'green';
                    this.reset();
                }, (error) => {
                    submitButton.textContent = 'Enviar Mensaje';
                    submitButton.disabled = false;
                    formMessage.textContent = 'Error al enviar el mensaje: ' + error.text;
                    formMessage.style.color = 'red';
                });
        });
    }
});

// Modal para el botón "Comprar"

document.addEventListener('DOMContentLoaded', () => {
    const buyButtons = document.querySelectorAll('.comprar-btn');
    const successModal = document.getElementById('successModal');
    const closeModalBtn = document.querySelector('#successModal .close-button');
    const modalOkBtn = document.querySelector('#successModal .modal-ok-button');

    if (buyButtons.length > 0 && successModal) {
        buyButtons.forEach(button => {
            button.addEventListener('click', (event) => {
                event.preventDefault();
                successModal.style.display = 'flex'; 
            });
        });

        const hideModal = () => {
            successModal.style.display = 'none';
        };

        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', hideModal);
        }
        if (modalOkBtn) {
            modalOkBtn.addEventListener('click', hideModal);
        }
    }
});