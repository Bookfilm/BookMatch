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