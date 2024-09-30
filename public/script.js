document.addEventListener('DOMContentLoaded', function () {
    // Load navbar
    fetch('/navbar')
        .then(response => response.text())
        .then(data => {
            document.getElementById('navbar').innerHTML = data;

            // Add event listeners for nav links and buttons
            addNavLinkListeners();
            addButtonListeners();
            // Load the default content (home)
            loadContent('home');
        })
        .catch(error => console.error('Error loading navbar:', error));
});

// Prevent F12 key
document.onkeydown = function (e) {
    if (e.key === "F12") {
        e.preventDefault();
    }
};

// Prevent right-click to show copy/paste widget instead
document.addEventListener("contextmenu", function (e) {
    e.preventDefault();
});

// Function to add event listeners to nav links
function addNavLinkListeners() {
    const navLinks = document.querySelectorAll('.btn-menu'); // Use .btn-menu for main items
    navLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default link behavior
            const page = this.getAttribute('data-page'); // Get the page to load
            loadContent(page); // Load the content
        });
    });
}

// Function to add event listeners for buttons in the sidebar
function addButtonListeners() {
    document.querySelectorAll('.btn-toggle').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default link behavior

            // Check if the button toggles a collapse
            const expanded = this.getAttribute('aria-expanded') === 'true' || false;
            this.setAttribute('aria-expanded', !expanded);
        });
    });

    // Add event listeners for sub-items
    document.querySelectorAll('.btn-toggle-nav .link-dark').forEach(subItem => {
        subItem.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default link behavior
            const page = this.getAttribute('data-page'); // Get the page to load
            loadContent(page); // Load the content
        });
    });
}

// Function to load content into the main tag
function loadContent(page) {
    fetch(page)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            // Load content into main
            document.getElementById('content').innerHTML = data;

            // Remove previously loaded CSS if it exists
            const existingCSS = document.getElementById('dynamic-css');
            if (existingCSS) existingCSS.remove();

            // Append new CSS
            const parser = new DOMParser();
            const doc = parser.parseFromString(data, 'text/html');
            const newCSS = doc.getElementById('dynamic-css');
            if (newCSS) {
                document.head.appendChild(newCSS);
            }

            // Load new JS scripts
            const newScripts = doc.querySelectorAll('script[id="dynamic-js"]');
            newScripts.forEach(script => {
                const newScript = document.createElement('script');
                newScript.src = script.src;
                newScript.defer = true;
                document.body.appendChild(newScript);
            });
        })
        .catch(error => console.error('Error loading content:', error));
}