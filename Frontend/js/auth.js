document.addEventListener('DOMContentLoaded', () => {
    const profileText = document.getElementById('profile-text');
    const profileLink = document.getElementById('profile-link');
    const loggedInUser = localStorage.getItem('loggedInUser');

    if (loggedInUser && profileText) {
        profileText.textContent = loggedInUser;
        if (profileLink) profileLink.href = 'index.html';
    }
});