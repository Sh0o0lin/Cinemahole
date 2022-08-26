/* navbar */

const button = document.querySelector('#navbar-btn');
const menu = document.querySelector('#navbar-content');
button.addEventListener('click', () => {
    menu.classList.toggle('hidden');
});

/* Dark Switch */

const checkbox = document.querySelector("#darkSwitch");
const html = document.querySelector("html");

const toggleDarkMode = function () {
    checkbox.checked
        ? html.classList.add("dark")
        : html.classList.remove("dark");
}
toggleDarkMode();
checkbox.addEventListener("click", toggleDarkMode);
