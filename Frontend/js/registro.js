(() => {
  const form = document.getElementById('registroForm');

  form.addEventListener('submit', e => {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value.trim();
    const apellido = document.getElementById('apellido').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirmPassword').value.trim();

    if (password !== confirmPassword) {
      alert('Las contraseñas no coinciden.');
      return;
    }

    const users = JSON.parse(localStorage.getItem('bm_users') || '[]');

    const userExists = users.some(user => user.email === email);
    if (userExists) {
      alert('El correo electrónico ya está registrado.');
      return;
    }

    users.push({ nombre, apellido, email, password });
    localStorage.setItem('bm_users', JSON.stringify(users));

    alert('¡Registro exitoso! Ahora puedes iniciar sesión.');
    location.href = 'formlogin.html';
  });
})();