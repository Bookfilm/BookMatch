(() => {
        const form = document.getElementById('registerForm');
        const emailInput = document.getElementById('regEmail');
        const passInput  = document.getElementById('regPassword');

        // Lee array de usuarios o crea uno vacío
        const users = JSON.parse(localStorage.getItem('bm_users') || '[]');

        form.addEventListener('submit', e => {
          e.preventDefault();               // evita recargo

          const email = emailInput.value.trim();
          const pwd   = passInput.value.trim();

          // Validación súper básica
          if (!email || !pwd) return alert('Completa los campos');

          // Evita duplicados
          if (users.some(u => u.email === email))
            return alert('Este email ya está registrado');

          // Añade nuevo usuario
          users.push({ email, password: pwd });
          localStorage.setItem('bm_users', JSON.stringify(users));

          alert('Usuario creado');
          location.href = 'formlogin.html'; // lleva al login
        });
      })();