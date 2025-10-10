(() => {
  const LS_KEY = 'bm_email';
  const emailInput  = document.getElementById('inputEmail');
  const passwordInput = document.getElementById('inputPassword'); // Agregado
  const rememberChk = document.getElementById('rememberCheck');
  const form        = document.querySelector('.form-signin');

  // 1. Al cargar la página, recuperar e-mail si existe
  const saved = localStorage.getItem(LS_KEY);
  if (saved) {
    emailInput.value = saved;
    rememberChk.checked = true;
  }

  // 2. Al enviar el formulario, guardar o borrar según el check
  form.addEventListener('submit', e => {
  e.preventDefault();

  const email = emailInput.value.trim();
  const pwd   = document.getElementById('inputPassword').value.trim();

  const users = JSON.parse(localStorage.getItem('bm_users') || '[]');
  const match = users.find(u => u.email === email && u.password === pwd);

  if (match) {
    // ---------  Recuérdame  ----------
    if (rememberChk.checked) localStorage.setItem(LS_KEY, email);
    else localStorage.removeItem(LS_KEY);
    // ---------  Redirige  ------------
    location.href = 'index.html';   // o la página que quieras
  } else {
    alert('Credenciales incorrectas');
  }
});

// Agregado: Inicializar el array de usuarios
localStorage.setItem('bm_users', JSON.stringify([{email: "tucorreo@ejemplo.com", password: "tucontraseña"}]));
})();