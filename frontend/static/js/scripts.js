document.addEventListener("DOMContentLoaded", function() {
    const popupMessage = document.getElementById('popupMessage');
    if (popupMessage && popupMessage.innerText.trim() !== "") {
        // Show the popup message
        popupMessage.style.display = 'block';

        // Hide it after 3 seconds
        setTimeout(() => {
            popupMessage.style.display = 'none';
        }, 3000);
    }

    // Example: Form validation for login and registration
    const loginForm = document.querySelector('#loginForm');
    const registerForm = document.querySelector('#registerForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            const email = document.querySelector('#loginEmail').value;
            const password = document.querySelector('#loginPassword').value;
            if (!email || !password) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            const username = document.querySelector('#registerUsername').value;
            const email = document.querySelector('#registerEmail').value;
            const password = document.querySelector('#registerPassword').value;
            const gender = document.querySelector('#registerGender').value;

            if (!username || !email || !password || !gender) {
                event.preventDefault();
                alert('Please fill in all fields.');
            }
        });
    }
});
